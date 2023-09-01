# Checker Weather with AtmoTrack

This Python project demonstrates how to use the OpenWeather API to check the weather for a specific location. By following the instructions below, you'll be able to retrieve current weather data and display it in your Python application.


## Features

- Retrieve current weather information using the OpenWeather API.
- Display key weather details such as temperature, humidity, and description.
- Easily customizable to fit into your own applications.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x installed
- OpenWeather API Key (sign up at [OpenWeather](https://home.openweathermap.org/users/sign_up))
- Requests = 2.31.0

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-weather-project.git

2. Navigate to the project directory:

    ```bash
    cd your-weather-project

3. Install the required dependencies:

    ```bash
    pip install requirements.txt

### Usage

1. Open the config.py file and replace 'YOUR_API_KEY_HERE' with your OpenWeather API key:

    ```python
    API_KEY = 'YOUR_API_HERE'

2. Run the 'main.py' script

    ```bash
    python3 main.py

3. Enter the location you want to check the weather for when prompted.

4. The script will fetch and display the current weather information for the specified location.

### Example

Let's see an example of how you can use the Weather Checker with OpenWeather API to get current weather information for a specific location.

1. **Input**

    ```bash
    Welcome to Weather Checker!
    Enter your OpenWeather API key: YOUR_API_KEY_HERE
    Enter the city name: New York

2. **Output**


    ```bash
    Weather Information:
    Location: New York, US
    Temperature: 290.34K
    Description: Clear sky
    Pressure: 1012 hPa
    Humidity: 58%
    Wind Speed: 2.48 m/s.


### Contributing

Contributions are welcome! If you have any improvements or feature suggestions, feel free to create a pull request.

