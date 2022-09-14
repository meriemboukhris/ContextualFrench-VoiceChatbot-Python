import pyttsx3

def say (Text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 180)
    print("   ")
    print(f"Assistant : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print ("  ")
