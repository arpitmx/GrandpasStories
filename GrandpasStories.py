import pyttsx3
import datetime
import webbrowser
import requests

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)
engine.setProperty("rate", 165)
engine.setProperty("volume", 500)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour <= 12):
        speak("Hello,Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon!")
    else:
        speak("Hello,Good Evening!")

    speak("Let me tell you a story!")

    def processInput(string):

        if (string.find("story")):
            res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
            type(res)
            print("Loading")
            print(res.text)
            speak(res.text)


def merchant():
    file1 = open("mov.txt", "r")
    for line in file1:
        print(line)
        speak(line)


def chetanbhagat():
    file1 = open("3MistakesofMyLife.txt", "r")
    for line in file1:
        print(line)
        speak(line)


if __name__ == "__main__":
    wishMe()
    chetanbhagat()
    # t ="true"
    # while(t):
    # inputUser = str(input(">"))
    # processInput(inputUser)




