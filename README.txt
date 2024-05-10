Requirements in order to run the server that hosts the chatbot:

Python Version : 3.8.0
Instalat requirements : 
pip install -r requirements.txt

As an ide if you want to edit it I recomand VS code because other IDEs that make a venv
will not work.
You can also run it from the cmd.

Run guide :
open a cmd in the foler containing the manage.py file
than type the command :
python manage.py runserver

it will start on 127.0.0.1:8000 and this are the api request and response examples:

Base url : http:/127.0.0.1:8000/ 

Url for question answering :  

http://127.0.0.1:8000/get-response/ 

Request POST with example body :  

{ 

    "question" : "how can i create sql querry ?" 

} 

Response : 

{ 

    "answer": "Like Rob Allen, I use SQL Compare / Data Compare by Redgate. I also use the Database publishing wizard by Microsoft. I also have a console app I wrote in C# that takes a sql script and runs it on a server. This way you can run large scripts with 'GO' commands in it from a command line or in a batch script. I use Microsoft.SqlServer.BatchParser.dll and Microsoft.SqlServer.ConnectionInfo.dll libraries in the console application." 

} 

 

 

Training url : 

http://127.0.0.1:8000/train/ 

Request example, it contains a conversation that the bot will remember :  

{ 

    "conversation" :  

    ["hello", 

    "hi there", 

    "what s up?", 

    "Nothing new wbu ?"] 

} 

Answer:  

"Successfully trained the bot with the new data" 

Benchmarking url: 

http://127.0.0.1:8000/benchmark/ 

Get Request and Response : 

{"results":"The results of the benchmarks made no 131 is a similarity between the given responses and the real response of 0.78569238957705648","nr_of_questions_responded":"131"}

