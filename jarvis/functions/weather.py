import requests
import asyncio
from jarvis.needs.audio import text_to_speech, play_audio
from jarvis.config import Config
# Function to get current weather for a specific city
def get_weather(city="Salem"):
    API_KEY = Config.get_openweather_api_key()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        air_pressure = data['main']['pressure']
        
        # Creating a weather summary
        weather_report = (f"The current temperature in {city} is {temp} degrees Celsius "
                          f"with a humidity of {humidity}%. The weather is described as {weather_description}. "
                          f"The air pressure is {air_pressure} hPa.")
        return weather_report
    else:
        return f"Unable to fetch weather data for {city}."

# Function to get tomorrow's weather forecast
def get_weather_tomorrow(city="Salem"):
    API_KEY = Config.get_openweather_api_key()
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tomorrow_forecast = data['list'][8]  # Typically, this is 3-hour intervals, 8 is around 24 hours
        weather_description = tomorrow_forecast['weather'][0]['description']
        temp = tomorrow_forecast['main']['temp']
        
        return f"The weather in {city} tomorrow will be {weather_description} with a temperature of {temp}°C."
    else:
        return f"Unable to fetch weather forecast for {city}."

# Function to get the current temperature only
def get_current_temperature(city="Salem"):
    API_KEY = Config.get_openweather_api_key()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        
        return f"The temperature in {city} is {temp}°C."
    else:
        return f"Unable to fetch temperature data for {city}."

async def speak_weather(city="Salem"):
    weather_report = get_weather(city)
    print(weather_report)  # Optional: Print the weather report to the console
    await text_to_speech(weather_report, "weather.mp3")
    play_audio("weather.mp3")

async def speak_weather_tomorrow(city="Salem"):
    weather_report = get_weather_tomorrow(city)
    print(weather_report)  # Optional: Print the weather report to the console
    await text_to_speech(weather_report, "weather_tomorrow.mp3")
    play_audio("weather_tomorrow.mp3")

async def speak_temperature(city="Salem"):
    temperature_report = get_current_temperature(city)
    print(temperature_report)  # Optional: Print the temperature report to the console
    await text_to_speech(temperature_report, "temperature.mp3")
    play_audio("temperature.mp3")

def process_weather_command(command):
    if "weather" in command.lower():
        if "tomorrow" in command.lower():
            asyncio.run(speak_weather_tomorrow())
        else:
            asyncio.run(speak_weather())
        return True
    elif "temperature" in command.lower():
        asyncio.run(speak_temperature())
        return True
    return False

# This main function can be used for testing purposes
async def main():
    city = "Salem"  # or any other city you want
    await speak_weather(city)
    await speak_weather_tomorrow(city)
    await speak_temperature(city)

if __name__ == "__main__":
    asyncio.run(main())
