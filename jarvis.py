import pyttsx3

engine = pyttsx3.init()

#using the function
def speaking(audio):
    engine.say(audio)
    engine.runAndWait()

rate.speaking("I am you AI assistant Rock")

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate