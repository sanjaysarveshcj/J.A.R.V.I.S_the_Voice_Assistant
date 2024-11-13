import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('Voice', voices[1].id)
else:
    engine.setProperty('Voice', voices[0].id)
    
def engine_talk(text):
    print(text)
    engine.say (text)
    engine.runAndWait()
    
def user_commands():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print (f"Me: {command}")
                return command 
    except Exception as e:
        print(f"Error: {e}")
    return ""
def run_jarvis():
    command = user_commands()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            engine_talk('Playing' + song + ' sir')
            pywhatkit.playonyt (song)
        elif 'wake up' in command:
            engine_talk('Welcome sir!')
        elif 'time' in command:
            time = datetime.datetime.now().srtftime('%I:%M:%p')
            engine_talk ('The current time is' + time + 'sir')
        elif 'who is' or 'what is' in command:
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk('sir, ' + info)
        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())
            print(joke)
            engine_talk(joke)
        elif 'stop' in command:
            engine_talk('Powering off sir!')
            sys.exit()
        else:
            engine_talk('I could not understand that sir.')
    else:
        engine_talk('I did not catch that sir. Please speak again.')
    
if __name__ == "__main__":
    while True:
        run_jarvis()
