import pyttsx3
import speech_recognition as sr
whatCanYou = ['what you do','mebo what can you do','can you do','you do','what can you do for me','what else you can do for me','what can you do']
stop = ['stop','quit','exit','cancel','bye','bye bye','tata','tata bye bye','tata bye','see you soon','bye see you soon','see you later','i will see you later','goodbye']
talkingMan = pyttsx3.init()
print("Hello I\'m Talking Man, I will repeat whatever you speak :)")
r = sr.Recognizer()
while True:
    userInput=input("\nPress S key to start or else x to Terminate: ")
    if userInput=="s":
        while True:
            with sr.Microphone() as source:
                print("\nHello, Now Say!!.......I will happily repeat it")
                audio = r.listen(source)

            try:
                print("you spoke: " + r.recognize_google(audio))
                talkingMan.say(r.recognize_google(audio))
                talkingMan.runAndWait()
                if r.recognize_google(audio)==stop:
                    print("bye bye")
                    talkingMan.say("bye,see you soon")
                    talkingMan.runAndWait()
                if r.recognize_google(audio)==whatCanYou:
                    print("I will repeat whatever you say!")
                    talkingMan.say("I will repeat whatever you say")
                    talkingMan.runAndWait()
            except sr.UnknownValueError:
                print("Sorry an Error occured")
            except sr.RequestError as e:
                print("cannot obtain result; {0}".format(e))
    elif userInput=="x":
        print("bye bye, Terminating")
        break
    else:
        print("Invalid choice")

print("\n      Created by Rudra shah")
print("talkingMan")