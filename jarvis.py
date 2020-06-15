import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

name="roshan"
engine = pyttsx3.init()
# voices=engine.getProperty('voices')
# print(voices[1].id)
# engine.setProperty('voice',voices[0].id)

#using the function
def speaking(audio):
    engine.say(audio)
    engine.runAndWait()
    
#audiotaking=input('Please tye what you want to say :-\n')

#speaking(audiotaking)

#adding thetime function
def time():
    Time= datetime.datetime.now().strftime("%I%M%S")
    speaking("the current time is")
    speaking(Time)

#time()

#adding the date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speaking("the current date is")
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
    #speaking("the current time is")
    time()
    #speaking("The current date is")
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

#takeCommand()

#send email function
def sendEmail(to,content):
    server = smtplib.SmTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','123password') 
    server.sendmail('abc@gmail.com',to,content)
    server.close()  #enter your gmail account





if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        #using the wikipedia for searching 
        elif 'wikipedia' in query:
            speaking('Searching...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speaking(result)
           


        #sending mail
        elif 'send email' in query:
            try:
                speaking("what should i send?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to,content)
                speaking("Email has benn sent well")
                speaking(content)
            except Exception e:
                print(e)
                speaking("Unable to send email")

        elif 'search in chrome' in query:
            speaking("What should i search sir?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            we.get(chromepath).open_new_tab(search , '.com')
        
        #os applications
        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

#playing songs from the system
        elif 'play songs' in query:
            songs_dir = 'D:\\'   #some location of the songs
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        #remember the function whatever we say
        elif 'remember that' in query:
            speaking("What should i remember")
            remember_data = takeCommand()
            speaking("You said me to remember" + remember_data)
            remember = open('data.txt','w')
            remember.write(remember_data)
            remember.close()

        elif 'offline' in query:
            quit()
    


    

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate