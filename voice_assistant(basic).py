import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
        except:
            print("Sorry, I did not catch that.")
        return command
while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break
    else:
        speak("I am sorry, I can only respond to simple commands.")
