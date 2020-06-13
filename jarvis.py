import pyttsx3

engine = pyttsx3.init()

#using the function
def speaking(audio):
    engine.say(audio)
    engine.runAndWait()
    
audiotaking=input('Please tye what you want to say :-\n')

speaking(audiotaking)

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate