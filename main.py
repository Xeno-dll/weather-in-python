# weather app

import requests

# OpenWeatherMap API
API_KEY = "GET_YOUR_OWN_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # Send Request to API
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric',  # For Celsius
            'lang': 'tr'  # For Turkish language
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check if API Request is Successful
        if response.status_code == 200:
            main = data.get('main')
            weather = data.get('weather', [{}])[0]
            wind = data.get('wind', {})
            temp = main.get('temp')
            feels_like = main.get('feels_like')
            humidity = main.get('humidity')
            description = weather.get('description', 'No description available')
            wind_speed = wind.get('speed', 'No wind speed available')

            # Weather Condition
            print(f"\n{city} Weather Condition:")
            print(f"Temp: {temp}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Description: {description.capitalize()}")
        else:
            # Unknown Error for API
            print(f"Couldn't find city: {city}")
            print(f"Error Code: {response.status_code}")
            print(f"Error Message: {data.get('message', 'Unknown Error')}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")

def main():
    while True:
        city = input("\nThe city where you want to know the weather: ")
        if not city.strip():
            print("Invalid login. Please enter a valid city name.")
            continue
        get_weather(city)
        
        # Ask if you want to query for another city
        while True:
            again = input("\nWould you like to query the weather forecast for another city? (Y/N): ").strip().lower()
            if again in ['y', 'n']:
                break
            print("Invalid input. Please enter 'Y' or 'N'.")
        
        if again == 'n':
            print("Thanks for using the weather app!")
            break

if __name__ == "__main__":
    main()
