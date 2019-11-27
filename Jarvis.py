import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import cv2


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id )
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    #machine speaks
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    #wishing code
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("Hi Sir, this is Jarvis . How can I be of your service ?")

def sendEmail(to , command):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender_email','pwd')
    server.sendmail('sender_email',to,content)
    server.close()

def takeCommand():
    #It takes microphone input from the user and returns string output   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        #r.energy_threshold=100
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing your command , Sir..")
        query = r.recognize_google(audio,language='en-in')
        print("You said:{}".format(query))
        #speak("You said:{}".format(query))
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
         query = takeCommand().lower()
         #exec tasks based on query
         if 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query=query.replace("wikipedia",'')
             try:
                results = wikipedia.summary(query, sentences=2)
             except wikipedia.DisambiguationError as e:
                s = random.choice(e.options)
                results = wikipedia.page(s)
             speak("according to wikipedia")
             print(results)
             speak(results)
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open facebook' in query:
             webbrowser.open("facebook.com")
         elif 'play music' in query:
             music_dir='C:\\Users\\DELL\\Desktop\\New folder\\NEW\\MY SONGS'
             songs = os.listdir(music_dir)
             print(*songs,sep="\n")
             t=random.randint(0,100)
             os.startfile(os.path.join(music_dir , songs[t]))
         elif 'time' in query:
             strTime = datetime.datetime.now().strftime("%I:%M:%S")
             speak("Sir ,the time is {}".format(strTime))
         elif 'open code' in query:
             codePath = '"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"'
             os.startfile(codePath)
         elif 'send email' in query :
              try:
                  speak("Sir , What should I say?")
                  content = takeCommand()
                  to = "recipient_mail"
                  content = content.replace("say that",'')
                  sendEmail(to , content)
                  speak("Email has been sent!")
              except Exception as e:
                 print(e)
                 speak("Sorry sir , I'm unable to send the mail!")
         elif 'shutdown' in query:
             speak("Glad to serve you Boss . Anytime at your service , See you later . Bye Bye")  
             exit(0)
         elif 'camera' in query:
             speak("Get ready to enjoy your charm , Sir")
             cv2.namedWindow("You look handsome , Sir!")
             vc = cv2.VideoCapture(0)

             if vc.isOpened(): # try to get the first frame
                   rval, frame = vc.read()
             else:
                   rval = False

             while rval:
                   cv2.imshow("You look handsome , Sir!", frame)
                   rval, frame = vc.read()
                   key = cv2.waitKey(20)
                   if key == 27: # exit on ESC
                          break
             vc.release()
             cv2.destroyWindow("You look handsome , Sir!")

         elif 'calculator' in query:
              os.startfile('calc.exe')


        
        
            


