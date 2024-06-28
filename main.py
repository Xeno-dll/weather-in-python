# weather app

import requests

# OpenWeatherMap API
API_KEY = "Secret_KEy"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # Send Request to API
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # For Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check if API Request is Successful
        if response.status_code == 200:
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            temp = main['temp']
            feels_like = main['feels_like']
            humidity = main['humidity']
            description = weather['description']
            wind_speed = wind['speed']

            # Weather Condition
            print(f"\n{city} Hava Durumu:")
            print(f"Sıcaklık: {temp}°C")
            print(f"Hissedilen Sıcaklık: {feels_like}°C")
            print(f"Nem: {humidity}%")
            print(f"Rüzgar Hızı: {wind_speed} m/s")
            print(f"Açıklama: {description.capitalize()}")
        else:
            # Unknown Error for API
            print(f"Şehir bulunamadı: {city}")
            print(f"Hata kodu: {response.status_code}")
            print(f"Hata mesajı: {data.get('message', 'Unknown Error')}")
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
        again = input("\nWould you like to query the weather forecast for another city? (Y/N): ")
        if again.strip().lower() != 'y':
            print("Thanks for using the weather app!")
            break

if __name__ == "__main__":
    main()
