import pyttsx3
import pygame
import RPi.GPIO as GPIO
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import pygame
import time
import webbrowser

GPIO.setwarnings(False)
channel = 17                  #Setup pin for motor A
channel2 = 4

channel3 = 22                 # Setup for motor B
channel4 = 27
# GPIO setup for motors
GPIO.setmode(GPIO.BCM)

GPIO.setup(channel, GPIO.OUT)       #  ....A1
GPIO.setup(channel2, GPIO.OUT)      #......A2

GPIO.setup(channel3, GPIO.OUT)      #...B1
GPIO.setup(channel4, GPIO.OUT)      #...B2

# initially making motors off

GPIO.output(17, GPIO.LOW)  
GPIO.output(4, GPIO.LOW)

GPIO.output(22, GPIO.LOW)  
GPIO.output(27, GPIO.LOW)

# Gpio setup  for Hi

GPIO.setup(2, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(2, 50)
p1 = GPIO.PWM(26, 50)

# Speak setup
engine = pyttsx3.init()

client = wolframalpha.Client('PU3GTH-4G7HXTA5T3')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)












def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak(' Welcome Prathamesh s creation')
time.sleep(0.5)
speak('Hi , this is polly')
speak('How may i assist you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        #r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get it please try again')
        query = myCommand();

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'start walking' in query:
            
            
            print("robot is moving forward", query)
            speak('yes sir moving fordward')
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel, GPIO.OUT)
            GPIO.setup(channel2, GPIO.OUT)
            GPIO.setup(channel3, GPIO.OUT)
            GPIO.setup(channel4, GPIO.OUT)

            
            GPIO.output(17, GPIO.HIGH)  # Turn motor A ford 
            GPIO.output(4, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)  # Turn motor B ford
            GPIO.output(22, GPIO.LOW) 
            time.sleep(2)
            
           
            
            GPIO.cleanup()
            speak('Task Completed')
            
        elif 'back' in query:
            print("Robot moving back")
            speak('Ya sure moving back')
            
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel, GPIO.OUT)
            GPIO.setup(channel2, GPIO.OUT)
            GPIO.setup(channel3, GPIO.OUT)
            GPIO.setup(channel4, GPIO.OUT)
            
            GPIO.output(17, GPIO.LOW)  # Turn motor A REverse
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)  # Turn motor B reverse
            GPIO.output(22, GPIO.HIGH)
            
            
            time.sleep(1)        
            
            GPIO.cleanup()
            speak('Task completed')



        elif 'turn left' in query:
            print("Robot moving left")
            speak('Ya sure moving left')
            
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel, GPIO.OUT)
            GPIO.setup(channel2, GPIO.OUT)
            GPIO.setup(channel3, GPIO.OUT)
            GPIO.setup(channel4, GPIO.OUT)
            
            GPIO.output(17, GPIO.LOW)  # Turn motor A off
            GPIO.output(4, GPIO.LOW)

            GPIO.output(27, GPIO.HIGH)  # Turn motor B on in frd
            GPIO.output(22, GPIO.LOW)
            time.sleep(5)
            speak('Task completed')
            time.sleep(1)        
            
            GPIO.cleanup()




        elif 'turn right' in query:
            print("Robot moving right")
            speak('Ya sure moving right')
            
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel, GPIO.OUT)
            GPIO.setup(channel2, GPIO.OUT)
            GPIO.setup(channel3, GPIO.OUT)
            GPIO.setup(channel4, GPIO.OUT)
            
            GPIO.output(17, GPIO.HIGH)  # Turn motor A off
            GPIO.output(4, GPIO.LOW)

            GPIO.output(27, GPIO.LOW)  # Turn motor B on in frd
            GPIO.output(22, GPIO.LOW)
            time.sleep(5)
            
            time.sleep(1)        
            
            GPIO.cleanup()
            speak('Task completed')
            

            
        elif "hi" in query or "hello" in query:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(2, GPIO.OUT)
            GPIO.setup(26, GPIO.OUT)
            p.start(0)
            time.sleep(1)
            p.ChangeDutyCycle(12.5)   # turn towards 180 degree
            print("ok")
            time.sleep(1)   # sleep

            p1.start(0)
            time.sleep(1)
            p1.ChangeDutyCycle(7.5) # servo 2 by 90 deg
            speak('Hi Sir')
            time.sleep(1)          # sleep
            print("ok sir")
            p1.ChangeDutyCycle(2.5) #back 2 0
            time.sleep(2)



            
            p.ChangeDutyCycle(2.5)   # Zero degree
            print("TNK U")
            GPIO.cleanup()

            

        elif 'nothing' in query or 'go to sleep' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye polly' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        
           
            
        elif 'who is your creator' in query:
            speak('your name')


        elif 'play song' in query:
             speak('ya sure')
             pygame.mixer.init()

             pygame.mixer.music.load("upload your song")
             pygame.mixer.music.play()
             time.sleep(50)
             pygame.mixer.music.stop()

        
        else:
            query = query
            speak('Should I use google it ?')
            recipient = myCommand()
            if 'yes' in recipient or 'ok' in recipient: 
                speak('Searching...')
                try:
                     try:
                          res = client.query(query)
                          results = next(res.results).text
                          speak('Got it.')
                          speak('it means  - ')
                          speak(results)
                    
                     except:
                           results = wikipedia.summary(query, sentences=2)
                           speak('Got it.')
                           speak('Google says - ')
                           speak(results)
        
                except:
                         speak('thank you')
                         #webbrowser.open('www.google.com')
                         
            elif 'no' in recipient:
                 speak('thank you sir!!')
                  
                  
                  
                  
        speak('Next Command! Sir!')
