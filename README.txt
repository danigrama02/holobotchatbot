Deci ca sa facem sa functioneze acest minunat server, cum chatterbot are fite 90% din timp trebuie 
respectate urmatoarele cerinte extrem de strict :

Versiune de python : obligatoriu 3.8.0
Instalat requirements : 
pip install -r requirements.txt

Ide folosit : neaparat VISUAL STUDIO CODE fara nici o extensie, rularea se va face din terminal
orice alt ide care creaza un venv pentru rulare nu este bun doarece chatterbot e scris cu stanga de un 
itist care a terminat cursuri cum sa devi itist in 3 ore si e foarte foarte sensibil la orice schimbare
are o baza de date care daca nu o gaseste salut s a dus

cum rulam :
din terminal ne asiguram ca python 3.8 este pus in path env 
intram in folderul in care se gaseste manage.py, acesta este holobotwebapi 
si scriem urmatoarea comanda 
python manage.py runserver

si se porneste pe portul 8000 serverul local de django unde este botul
requesturi si raspunsuri : 

Base url : http:/127.0.0.1:8000/ 

Url pentru raspunsuri la intrebari :  

http://127.0.0.1:8000/get-response/ 

Request de POST cu body :  

{ 

    "question" : "how can i create sql querry ?" 

} 

Si raspuns de forma : 

{ 

    "answer": "Like Rob Allen, I use SQL Compare / Data Compare by Redgate. I also use the Database publishing wizard by Microsoft. I also have a console app I wrote in C# that takes a sql script and runs it on a server. This way you can run large scripts with 'GO' commands in it from a command line or in a batch script. I use Microsoft.SqlServer.BatchParser.dll and Microsoft.SqlServer.ConnectionInfo.dll libraries in the console application." 

} 

 

 

Url pentru training : 

http://127.0.0.1:8000/train/ 

Cu request :  

{ 

    "conversation" :  

    ["hello", 

    "hi there", 

    "what s up?", 

    "Nothing new wbu ?"] 

} 

Si raspuns:  

"Successfully trained the bot with the new data" 

Url pentru benchmarck: 

http://127.0.0.1:8000/benchmark/ 

Cu request de GET si raspuns : 

{"results":"The results of the benchmarks made no 131 is a similarity between the given responses and the real response of 0.78569238957705648","nr_of_questions_responded":"131"}

de preferat sa nu se foloseasca requestul de train deoarece se poate sa il strice de cap daca e rulat de pe server,
ceva cu threaduri si chestii foarte delicate cand vrea merge cand nu se supara
in cazul in care se strica ceva luati din nou fisierul db.sqlite3, stergeti cel de pe pc si pune ti l iar 
acela e fisierul in care are chatterbot baza de date cu grafurile de conversatie si se poate defecta foarte random 

inca o problema importanta, deoarece codistu din spatele chatterbot e la fel de bun ca si noi a hardcodat o tampenie si trebuie modificata asa ca in folderul urmator :
C:\Users\dani7\AppData\Local\Programs\Python\Python38\Lib\site-packages\chatterbot
cu userul vostru gasiti fisierul : tagging.py
in acest fisier la linia 13 trebuie sters si pus urmatorul cod 
self.nlp = spacy.load("en_core_web_sm")
altfel va da erroare 
bafta !