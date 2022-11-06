import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)    
    if hour >= 0 and hour < 12:
        Speak("Good Morning")

    elif hour>= 12 and hour < 18:
        Speak("Good Afternoon")    

    else:
        Speak("Good Evening")    

    Speak("I am Jarvis sir. Please tell me how may I help you")    

def takeCommand():
    '''It takes microphone input from the user and return string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f'User Said: {query}\n')

    except Exception as e:
        # print(e)   

        print("Say that again please...")
        return "None"
    return query    

def sendEmail(to, content): #set less secure apps search in google before this
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here') #written your gamild id and password password should be in textfile also for security purposes.
    server.sendmail("youremail@gmail.com", to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            Speak('Searchig Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Speak("According to wikipedia")
            print(results)
            Speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
               music_dir = 'C:\\Users\\sizen\\Music\\youtube music'
               songs = os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f'Sir, the time is {strTime}')

        elif 'open code' in query:
            codePath = "C:\\Users\\sizen\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)
        
        elif 'email' in query:
            try:
                Speak("What should I say")
                content = takeCommand()
                to = "technical.sizen123@gmail.com"
                sendEmail(to, content)
                Speak("Email has been sent")
            except Exception as e:
                print(e)
                Speak("Sorry sizen bhai. I am not able to send this email")    