import speech_recognition as sr
import pyttsx3
import requests
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
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
def get_weather(city):
    api_key = "your_openweather_api_key"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response["cod"] != "404":
        main = response["main"]
        weather = response["weather"][0]["description"]
        temp = main["temp"]
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    return "City not found."
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
    elif "weather" in command:
        city = command.replace("weather", "").strip()
        weather_report = get_weather(city)
        speak(weather_report)
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break
    else:
        speak("I'm sorry, I can only respond to simple commands.")

