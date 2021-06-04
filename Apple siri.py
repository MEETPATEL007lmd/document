import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
rate = engine.getProperty("rate")
engine.setProperty("rate",200)
print(rate)
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

    speak("how many i help you")       

def takeCommand():
 
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
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('spatel5720@gmail.com', 'sunita@1980')
    server.sendmail('nkpatel0803@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()

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

        elif 'open SSA' in query:
            webbrowser.open("http://www.ssagujarat.org/")    

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org/#/im")

        elif 'open homework' in query:
            webbrowser.open("https://www.educloud.in/homework/HomeWork.do")

        elif 'open testlink' in query:
            webbrowser.open("https://www.educloud.in/studymaterial/studymaterials.do")           
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\PATEL\\music'
            songs = os.listdir(music_dir)
            print(random.randint(1,28))    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\PATEL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open minecraft' in query:
            minecraftPath = "C:\\Users\\PATEL\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(minecraftPath)

        elif 'email to meet' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nkpatel0803@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend meet. I am not able to send this email")    

