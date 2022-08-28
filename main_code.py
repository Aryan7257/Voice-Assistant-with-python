import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib  #for sending the email
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def out():
    speak("thank you for your time sir, have a good day")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("   ,welcome sir,")
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am tom. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    # enable less secure apps in your gmail account.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jainaryan520@gmail.com', 'password')
    server.sendmail('jainaryan520@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    var={"thank you","exit","bye","thankyou"}
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\jaina\\OneDrive\\Pictures\\music'
            songs = os.listdir(music_dir)
            random.shuffle(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'send email to aryan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "19uec078@lnmiit.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")

        elif query in var:
            out()
            break


