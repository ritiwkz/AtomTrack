import requests as rq

# Function to fetch weather data from OpenWeather API
def get_weather(api_key, city_name):
    # Construct the API URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    try:
        # Send GET request to the API
        response = rq.get(url)

        if response.status_code == 200:
            data = response.json()
            return data  # Return the retrieved data
        else:
            return None  # Return None in case of error
    except rq.exceptions.RequestException:
        return None  # Return None if request fails

# Function to display weather data to the user
def display_weather_data(data):
    if data:
        print("\nWeather Information:")
        print(f"Location: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}K")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data. Please check your API key and city name.")

def main():
    print("Welcome to Weather Checker!")

    # Get user input for API key and city name
    api_key = input("Enter Your API key")
    city_name = input("Enter the city name: ")

    # Get weather data using the API key and city name
    weather_data = get_weather(api_key, city_name)

    # Display weather data to the user
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
