'''
File containing the views of the app
'''
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'holobotwebapi'))
from rest_framework.decorators import api_view
from rest_framework.response import Response
from holobotimplementation import holoborchatbot


# Function that a response to a question request
@api_view(['POST'])
def get_response_view(request):
    response_from_bot = holoborchatbot.get_answer_to_question(request.data['question'])
    print(request.data)
    print(request.data['question'])
    print(response_from_bot)
    return Response({'answer': str(response_from_bot)})


@api_view(['POST'])
def train_bot(request):
    train_data = request.data['conversation']
    holoborchatbot.train_model(train_data)
    return Response("Successfully trained the bot with the new data")

@api_view(['GET'])
def train_test(request):
    holoborchatbot.script_to_train(10000)
    return Response("Done")

@api_view(['GET'])
def get_benchmarcks_results(request):
    results, nr_of_questions_for_test = holoborchatbot.benchmarks()
    response_text = "The results of the benchmarks made no " + str(nr_of_questions_for_test) + " is a similarity between the given responses and the real response of " + str(results)
    return Response({"results": str(response_text), "nr_of_questions_responded": str(nr_of_questions_for_test)})
