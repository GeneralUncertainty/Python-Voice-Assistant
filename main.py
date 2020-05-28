# Standard library imports

import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import wikipedia # pip install wikipedia

# In built modules
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

"""
    sapi5 - Windows 7 / 8 / 10
    espeak - Linux (Ubuntu, Debian, Kali Linux etc.)
    nsss - MAC OS    
"""

emails = {
            'mother': "mother@gmail.com",
            'father': "father@gmail.com",
            'sister': "sister@gmail.com"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()    

def greeting():
    hour = int(datetime.datetime.now().hour)

    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    elif hour >= 16 and hour < 18:
        speak("Good Pre-evening!")

    elif hour >= 18 and hour < 21:
        speak("Good Evening!")

    else:
        speak("Good Night!")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Taking Command ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}\n") 

    except Exception as e:
        print(e)  

        speak("Pardon?")   

    return query

def sendMail(name):
         
        try:
            str(name)
            speak(f"What should I send to {name}?")
            message = command()
            to = emails[name]

            server = smtplib.SMTP('smtp.gmail.com', 587) # for gmail services
            server.ehlo()
            server.starttls()
            server.login('your-email-address', 'your-password')
            server.sendmail('your-email-address', to, content)
            server.close()



            speak("Your email was successfully sent")

        except Exception as e:
            print(e)
            speak("Unfortunately, your email could not be sent.")

if __name__ == "__main__":
    greeting()

    while True:
        query = command().lower()

    if 'wikipedia' in query:
        speak('Finding on Wikipedia ...')
        query.replace("wikipedia", "")

        result = wikipedia.summary(query, sentences=2)
        
        speak(f"Wikipedia says that {results}")
        print(f"Wikipedia says that {results}")
        
    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")

    elif 'open duckduckgo' in query:
        webbrowser.open("www.duckduckgo.com")

    elif 'open twitter' in query:
        webbrowser.open("www.twitter.com")

    elif 'open netflix' in query:
        webbrowser.open("www.netflix.com/browse")

    elif 'open amazon' in query:
        webbrowser.open("www.amazon.in")  

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The time is {strTime}")
        speak(f"The time is {strTime}")

    sendMail(mother)
