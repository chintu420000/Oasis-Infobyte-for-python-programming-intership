import requests
import tkinter as tk
def get_weather(location):
    api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        return f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWeather: {weather_description.capitalize()}"
    else:
        return "City not found."
def command_line_weather():
    location = input("Enter city name or ZIP code: ")
    weather_info = get_weather(location)
    print(weather_info)
def gui_weather():
    def display_weather():
        location = location_entry.get()
        weather_info = get_weather(location)
        result_text.set(weather_info)
    root = tk.Tk()
    root.title("Weather App")
    location_label = tk.Label(root, text="Enter city name or ZIP code:")
    location_label.pack()
    location_entry = tk.Entry(root)
    location_entry.pack()
    get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
    get_weather_button.pack()
    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text)
    result_label.pack()
    root.mainloop()
