import datetime as dt
import webbrowser
import time
from talk import say
import requests
import os
from record import listen
from hashlib import new
import newsapi
import json
from bs4 import BeautifulSoup
import BlaguesApi
from playsound import playsound

def date():
    now=dt.datetime.now()
    week_now=int(dt.datetime.now().strftime("%w"))
    month_now=now.month
    day_now=dt.datetime.now().strftime("%d")
    year_now=now.year
    months=["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    days=["dim", "lun", "mar", "mer", "jeu", "vend", "sam"]
    r="Nous sommes le: " + days[week_now]  +" " + day_now +" "+ str(months[month_now-1]) + " " + str(year_now) 
    say(r)
def heure():
    t=dt.datetime.now().strftime("%H:%M")
    q="Il est: " + str(t)
    say(q)
def meteo():
    say("Pour quelle ville? ")
    ville=listen()
    complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&appid="+"YOUR-API-KEY"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    temp_city = ((api_data['main']['temp']) - 273.15) 
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = dt.datetime.now().strftime("%H:%M")
    m="Meteo pour - {}  || {}".format(ville.upper(), date_time)
    say(m)
    t="Température est:  {:.2f} degré Celsius".format(temp_city)
    say(t)
    d="Description est: " + weather_desc
    say(d)
    h="L'humidité est de " + str(hmdt) +' pourcent'
    say(h)
    v="Et la vitesse du vent est de "+ str(wind_spd) +' kilomètre par heure'
    say(v)

def journal():
    top_headlines = "https://newsapi.org/v2/top-headlines?country=fr&apiKey=YOUR-API-KEY"
    try:
        api_link = requests.get(top_headlines)
    except:
        say("Verifiez votre connexion")
    news=json.loads (api_link.text)
    for new in news["articles"]:
        say(str(new["title"]))
        say(str(new["description"]))
    
def blagues():
    Jokes = BlaguesApi.Jokes('YOUR-API-KEY')
    response = Jokes.random_categorized('global')   
    say(response["joke"]) 
    say(response["answer"])

def recherche():
    say("Que souhaitez vous cherchez?")
    r=listen()
    url='http://google.com/search?q=' + r
    webbrowser.get().open(url)
    say("Voici ce que j'ai trouvé sur le web pour: " + r)

def localisation():
    say("Quelle est la localisation?")
    location=listen()
    url= 'http://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    say("Voici la localisation de " +location)

def alarme():
    say ("A quelle heure? ")
    h=listen()
    say ("Minutes? ")  
    m=listen()
    a=h+":"+m
    say ('Rappel pour ' + h +" h" + m + ' activé')
    while True:
        t=dt.datetime.now()
        now=time.strftime("%H:%M")
        if now == a:
            say("Temps écoulé!")
            playsound('alarm.mp3')
            time.sleep(2)
            exit()
        elif now>a:
            break

def wishMe():
    hour=int(dt.datetime.now().hour)
    if hour>=0 and hour<13:
        say("Bonjour")
    elif hour>=13 and hour<18:
        say("Bonne après midi")
    else:
        say("Bonsoir")
    say ("Je suis votre assistant virtuelle, dites moi comment je peux vous aider")