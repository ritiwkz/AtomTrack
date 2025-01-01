#!/usr/bin/python3
import requests as rq

# Function to fetch weather data from OpenWeather API
def get_weather(api_key, city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    try:
        response = rq.get(url)
        response.raise_for_status()  # Raise error for non-200 responses
        return response.json()
    except rq.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except rq.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None  # Return None in case of any exception

# Function to convert temperature from Kelvin
def convert_temperature(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius:.2f}°C / {fahrenheit:.2f}°F"

# Function to display weather data
def display_weather_data(data):
    if data:
        print("\nWeather Information:")
        print(f"Location: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {convert_temperature(data['main']['temp'])}")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Unable to retrieve weather data. Please try again.")

def main():
    print("Welcome to Weather Checker!")

    api_key = input("Enter your OpenWeather API key: ")
    
    # Loop to ensure a valid city is entered
    while True:
        city_name = input("Enter the city name: ")
        weather_data = get_weather(api_key, city_name)
        
        if weather_data and weather_data.get('cod') == 200:
            display_weather_data(weather_data)
            break
        else:
            print("Invalid city name or API key. Please try again.")

if __name__ == "__main__":
    main()
