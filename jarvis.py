import pyttsx3
import datetime

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
    speak(year)
    speak(month)
    speak(day)
    
#date()  #calling the function
    
    
#Greeting function telling date and time
def wishme():
    speaking("Hello Roshan, Welcom to our world")
    speaking("the current time is")
    time()
    speaking("The current date is")
    date()
    speaking("I am always at your service. How may i Assist you sir?")

wishme()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate