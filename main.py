import random
import json
import re
import torch
from model import NeuralNet
from nltk_imp import bag_of_words, tokenize
import datetime as dt
from record import listen
from talk import say
from record import listen
from talk import say 
from functions import blagues, heure, date, journal, localisation, meteo, recherche, alarme, wishMe

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'r') as json_data:
    intents=json.load(json_data)
FILE="data.pth"
data=torch.load(FILE)

input_size=data["input_size"]
hidden_size=data["hidden_size"]
output_size=data["output_size"]
all_words=data["all_words"]
tags=data["tags"]
model_state=data["model_state"]
model= NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def main():
    sentence=listen()
    if sentence == "quitter":
        say("Au revoir")
        exit()
    if "météo" in sentence:
        meteo()
    elif "actualité du jour" in sentence:
        journal()
    sentence=tokenize(sentence)
    X= bag_of_words(sentence,all_words)
    X=X.reshape(1,X.shape[0])
    X=torch.from_numpy(X).to(device)
    output = model(X)
    _ , predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output,dim=1)
    prob=probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag==intent["tag"]:
                reply=random.choice(intent["responses"])
                if "heure" in reply:
                    heure()
                elif "date" in reply:
                    date()
                elif "blague" in reply:
                    blagues()
                elif "recherche" in reply:
                    recherche()
                elif "localisation" in reply:
                    localisation()    
                elif "alarme" in reply:
                    alarme()
                else:    
                    say(reply)
    else:
        say("Je ne sais pas comment répondre à cela")
                
wishMe()
while True:
    main()
