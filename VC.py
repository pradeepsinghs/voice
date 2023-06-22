import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import speed_cli
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Voice assistant Sir madded by Pradeeep Singh. Please tell me how may I help you")       

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

if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com") 

        elif "temperature" in query:
            search = "temperature in Bhopal"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{temp}")

        elif "quit" in query:
            speak("good bye sir have a nice day ")
            exit()




        # elif "internet speed" in query:
        #     wifi = speed_cli.speed_cli()
        #     upload_net = wifi.upload()/1048576
        #     download_net = wifi.download()/1048576
        #     print("wifi upload speed is",upload_net)
        #     print("wifi download speed is",download_net)
        #     speak(f"wifi download speed is {download_net}")
        #     speak(f"wifi upload speed is {upload_net}")
                  

        elif 'song play' in query:
            music_dir = 'E:\\D1\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            

        elif 'open code' in query:
            codePath = "C:\\Users\\ABC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs//Visual Studio Code//vscode"
            os.startfile(codePath)
