import speech_recognition as sr
from talk import say

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez...")
        r.pause_threshold = 1
        audio= r.listen(source,0,2)
    try:
        print("Traitement en cours..")
        query= r.recognize_google(audio, language="fr-FR")
        print(f"Vous: {query}")
    except:
        say("Je n'ai pas bien compris")
    query=str(query)
    return query.lower()