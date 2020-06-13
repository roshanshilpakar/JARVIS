import pyttsx3
import datetime
import speech_recognition as sr

name="roshan"
engine = pyttsx3.init()


#using the function
def speaking(audio):
    engine.say(audio)
    engine.runAndWait()
    
#audiotaking=input('Please tye what you want to say :-\n')

#speaking(audiotaking)

#adding thetime function
def time():
    Time= datetime.datetime.now().strftime("%I%M%S")
    speaking(Time)

#time()

#adding the date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speaking(year)
    speaking(month)
    speaking(day)
    
#date()  #calling the function
    
    
#Greeting function telling date and time
def wishme():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speaking("Good morning"  + name)
    elif hour>=12 and hour<18:
        speaking("Good afternoon" + name)
    elif hour>=18 and hour<24:
        speaking("Good evening" + name)
    else:
        speaking("Good noght"  + name)
    speaking("Hello" + name  + "Welcome to our world")
    speaking("the current time is")
    time()
    speaking("The current date is")
    date()
    speaking("I am always at your service. How may i Assist you sir?")

#wishme()
    
#taking command from the user
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        
    except Exception as e:
        print(e)
        speaking("will you say that again")
    
        return "None"
    return query

takeCommand()


    

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate