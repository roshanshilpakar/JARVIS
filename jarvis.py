import pyttsx3

engine = pyttsx3.init()
engine.say("My name is JARVIS")
engine.runAndWait()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate