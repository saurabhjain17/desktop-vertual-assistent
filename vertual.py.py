from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import wikipedia
import os
import datetime
import speech_recognition as sr
from playsound import playsound
import webbrowser
import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 


import webbrowser 

import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 
import win32com.client as wincl 
 
print("jarvis is starting")
try:
   app=wolframalpha.Client("your api id")
except Exception:
    print("Some feature are not working")


sir = "Your Name"

converter = pyttsx3.init() 
client=wolframalpha.Client('saurabh')
 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
 
engine.setProperty('voice',voices[0].id)

converter.setProperty('rate',100) 
converter.setProperty('volume',.75)




def speak(text):
    engine.say(text)
    engine.runAndWait()
def usrname(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("#####################".center(columns)) 
    print("Welcome Mr.", uname.center(columns)) 
    print("#####################".center(columns)) 
      
    speak("How can i Help you, Sir")
def WishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Jarvis 1 point o") 
    speak("I am your Assistant") 
    speak(assname)

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
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


class Widget:
    def __init__(self):
        root=Tk()
        root.title("jarvis")
        root.geometry("1280x644")

        
        def Exit():
            root.destroy()

        photo =PhotoImage(file="ironman3.png")
        label =Label(image=photo)
        label.pack(side='right' ,fill='both' ,expand='no')

        
        usertext =StringVar()

        usertext.set("Click Run To Give Jarvis Command")

        userFrame =LabelFrame(root ,text="User" ,font="comicsansms 10 bold")
        userFrame.pack(fill=BOTH ,expand='yes')

        message =Message(userFrame ,textvariable=usertext ,bg="#3b9895" ,fg="white")
        message.config(font="comicsansms 10 bold")
        message.pack(fill=BOTH ,expand='yes')

        button =Button(root ,text="Run" ,font="comicsansms 10 bold" ,bg="#4B4B4B" ,fg="white" ,command=self.clicked).pack(fill=X ,expand='no')
        button2 =Button(root ,text="Exit" ,font="comicsansms 10 bold" ,bg="black" ,fg="white" ,command=Exit).pack(fill=X,expand='no')


        root.mainloop()
                                        

    def clicked(self):
        print("Working")
        query=takeCommand().lower()
        self.usertext.set('Listening.....')
        self.usertext.set(query)
        query=query.lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'send email to me' in query: 
           try: 
               speak("What should I say?") 
               content = takeCommand() 
               to = "Receiver email address"    
               sendEmail(to, content) 
               speak("Email has been sent !") 
           except Exception as e: 
               print(e) 
               speak("I am not able to send this email") 
  
        elif 'send a mail' in query: 
           try: 
               speak("What should I say?") 
               content = takeCommand() 
               speak("whome should i send") 
               to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
           except Exception as e: 
               print(e) 
               speak("I am not able to send this email")   
        if 'wikipedia' in query:
           speak('Searching wikipedia...')
           query=query.replace("wikipedia", "")
           results=wikipedia.summary(query,sentences=1)
           speak("According to Wikipedia")
           print(results)
           speak(results)
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query    
        elif "change name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me")    
        elif 'joke' in query: 
            speak(pyjokes.get_joke())    
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
           webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
           webbrowser.open('stackoverflow.com') 
        elif 'open facebook' in query:
           webbrowser.open("facebook.com") 
        elif 'open twitter' in query:
           webbrowser.open("twitter.com")     
        elif 'open instagram' in query:
           webbrowser.open("instagram.com")  
        elif 'open galgotia cloud' in query:
           webbrowser.open('https://gu.icloudems.com/corecampus/index.php')  
        elif 'play music' in query:
           music_dir="D:\\songs"
           songs=os.listdir(music_dir)
           os.startfile(os.path.join(music_dir,songs[6]))
        elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak("sir , the time is{}".format(strTime))

        elif 'open vs code'in query:
           codePath="C:\\Users\MAA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
           os.startfile(codePath)
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        elif "why you came to world" in query: 
            speak("Thanks to Saurabh. further It's a secret") 
  

  
        elif 'is love' in query: 
            speak("It is 7th sense that destroy all other senses") 
  
        elif "who are you" in query: 
            speak("I am your virtual assistant created by Saurabh") 
  
        elif 'reason for you' in query: 
            speak("I was created as a mini project by Saurabh ")           

        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
        elif "weather" in query: 
              
            # Google Open weather website 
            # to get API of Open weather  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found ") 
              

        
        elif "calculate" in query:  
              
            app_id = "Wolframalpha api id" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer) 
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e))
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
  
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "Jarvis Camera ", "img.jpg") 
  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
  
        elif "update assistant" in query: 
            speak("After downloading file please replace this file with the downloaded one") 
            url = '# url after uploading file'
            r = requests.get(url, stream = True) 
              
            with open("Voice.py", "wb") as Pypdf: 
                  
                total_length = int(r.headers.get('content-length')) 
                  
                for ch in progress.bar(r.iter_content(chunk_size = 2391975), 
                                       expected_size =(total_length / 1024) + 1): 
                    if ch: 
                      Pypdf.write(ch)                                 
        else:
          try:
            res = client.query(task)
            output = next(res.results).text
            print(output)
            speak(output)
        
          except:
            speak('Okay')
            res = wikipedia.summary(task ,sentences=2)
            print(res)
            speak(res)                      
        

if __name__ == '__main__':
    speak('JARVIS IS STARTING')
    WishMe()
    widget=Widget()
    
    




