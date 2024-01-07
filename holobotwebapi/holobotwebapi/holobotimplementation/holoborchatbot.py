'''
Created on Nov 18, 2023

@author: dani7

this is the python implementantion of our chatbot it will be later used as a part of a server

the model that we train is chatterbot

'''
# Download the English model if you haven't done so already
# python -m spacy download en_core_web_sm

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import csv
from difflib import SequenceMatcher

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path_questions = os.path.join(BASE_DIR, 'Questions.csv')
file_path_answers = os.path.join(BASE_DIR, 'Answers.csv')

import chatterbot.comparisons
import chatterbot.response_selection
import chatterbot.logic
import chatterbot.filters as filters
from chatterbot.conversation import Statement

chatbot = ChatBot("Ron Obvious",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch',
                          'default_response': 'I am sorry, but I do not understand.',
                          'maximum_similarity_threshold': 0.90,
                          "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
                          "response_selection_method": chatterbot.response_selection.get_most_frequent_response
                      }
                  ]
                  ,
                  filters=[filters.get_recent_repeated_responses]
                  )


def read_data_from_csv(filename, nr_of_lines_start, nr_of_lines_end):
    data = []
    with open(filename, encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                if line_count>nr_of_lines_start:
                    data.append(row)
                    print("Appened :" + str(line_count))
            line_count += 1
            if line_count == nr_of_lines_end:
                break
    print("read done")
    return data


def model_script():
    conversation = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome."
    ]
    trainer = ListTrainer(chatbot)
    trainer.train(conversation)


def benchmarks():
    questions_answers = get_questions_and_answers(0,500)
    test = []
    for el in questions_answers:
        if el[0] != "" and el[1] != "":
            test.append(el)

    score = 0

    for question in test:
        response = chatbot.get_response(question[0])
        val = SequenceMatcher(None, str(response), str(question[1])).ratio()
        score += val
        print(
            "real anser-----------------------------------------------------------------------------------------------------")
        print(question[1])
        print(
            "bot anser.....................................................................................................")
        print(response)
        print("-----------------------------------------------------------------------------------------------------")

    return score / len(test), len(test)


def chat():
    # model_script()
    print("enter exit to stop chatting")
    print("That chatting started: ")
    while (True):
        chat = str(input())
        if chat == "exit":
            return
        print(chatbot.get_response(chat))


def train_model(questions_answers):
    trainer = ListTrainer(chatbot)
    for conv in questions_answers:
        conversation = [str(conv[0]), str(conv[1])]
        trainer.train(conversation)


def script_to_train(start,end):
    while (start<end):
        train_model(get_questions_and_answers(start,start+100))
        start=start+100
    #trainer = ChatterBotCorpusTrainer(chatbot)
    #trainer.train('./chatterbot-corpus/data/english')




def get_answer_to_question(question):
    return chatbot.get_response(question)


def get_questions_and_answers(start,end):
    data1 = read_data_from_csv(file_path_questions, start,end)
    print("Data1 read")
    data2 = read_data_from_csv(file_path_answers, start,end)
    print("Data2 read")
    questions_answers_pre = []
    questions_answers = []
    print("start processing")
    for line in data1:
        questions_answers_pre.append([line[5], "", line[0]])
    lineno = 0
    for line in data2:
        text = line[5].replace("<p>", "")
        text = text.replace("</p>", "")
        text = text.replace("<code>", "")
        text = text.replace("</code>", "")
        text = text.replace("<br>", "")
        text = text.replace("<pre>", "")
        text = text.replace("</pre>", "")
        text = text.replace("<blockquote>", "")
        text = text.replace("</blockquote>", "")
        text = text.replace("<em>", "")
        text = text.replace("</em>", "")
        text = text.replace("<strong>", "")
        text = text.replace("</strong>", "")
        lineno+=1
        for qu in questions_answers_pre:
            if qu[2] == line[3]:
                print("processing " + str(lineno))
                qu[1] = text

    # for el in questions_answers:
    #    print(el)
    # print("++++++++++++++++++++++++++++++++==")
    for el in questions_answers_pre:
        if el[1] != '':
            questions_answers.append(el)
    print("done processing")
    return questions_answers

    # trainer = ListTrainer(chatbot)
    # for conv in questions_answers:
    #     conversation = [conv[0],conv[1]]
    #     trainer.train(conversation)


def run():
    cmd = None
    while (True):
        print("=============================")
        print("Meniu holobot:")
        print("=============================")
        print("1. Antreneza modelul")
        print("2. Fa un benchmark la bot")
        print("3. Just chattin...")
        print("4. Bye bye")
        print("=============================")
        try:
            cmd = int(input())
        except Exception:
            print("Nu ai introdus un string valid pt optiune, mai incearca")
        if cmd == 1:
            print("Start training the model")
        elif cmd == 2:
            accuracy, data_len = benchmarks()
            print("Similaritatea raspunsurilor chatbotului la " + str(
                data_len) + " de intrebari selectate cu raspunsurile reale a fost : ")
            print(accuracy)
        elif cmd == 3:
            chat()
        elif cmd == 4:
            print("Have a nice day!")
            return


#script_to_train(0,500000)
# model_script()
#for el in get_questions_and_answers(0,20):
#    print(el)
#run()
'''
19 ian prez proiecte ale celor care avem prooiect al ppi

tre sa facem suport la prezentare 
facem ppt - in care sa apara maxim 6-7 slideuri
    -in ppt sciren cine suntem ce se prob ttre sa rezolvam cum se formealizeaza din pucnnt de vedere al nmachine learning cum am rezolvato si ce am optiunut
 si ce zicem in ele 
 teaser pregatit video in care se sa vada ce face app si ce prob rezolva 
 musai numele si prenumele noustru
 in 13 ian sambata workshop online 
 
'''