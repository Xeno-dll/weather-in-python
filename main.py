# weather app

import requests

# OpenWeatherMap API anahtarınızı buraya ekleyin
API_KEY = "bb8306c119de14cfbc40137c5e13f0de"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # API'ya istek gönder
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Celcius derecesinde sıcaklık için
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # API isteğinin başarılı olup olmadığını kontrol et
        if response.status_code == 200:
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            temp = main['temp']
            feels_like = main['feels_like']
            humidity = main['humidity']
            description = weather['description']
            wind_speed = wind['speed']

            # Hava durumu bilgisini yazdır
            print(f"\n{city} Hava Durumu:")
            print(f"Sıcaklık: {temp}°C")
            print(f"Hissedilen Sıcaklık: {feels_like}°C")
            print(f"Nem: {humidity}%")
            print(f"Rüzgar Hızı: {wind_speed} m/s")
            print(f"Açıklama: {description.capitalize()}")
        else:
            # Hata durumunda API yanıtını ve hata mesajını yazdır
            print(f"Şehir bulunamadı: {city}")
            print(f"Hata kodu: {response.status_code}")
            print(f"Hata mesajı: {data.get('message', 'Bilinmeyen hata')}")
    except requests.exceptions.RequestException as e:
        print(f"API isteği sırasında bir hata oluştu: {e}")

def main():
    while True:
        city = input("\nHava durumunu öğrenmek istediğiniz şehir: ")
        if not city.strip():
            print("Geçersiz giriş. Lütfen geçerli bir şehir adı girin.")
            continue
        get_weather(city)
        
        # Başka bir şehir için sorgu yapmak isteyip istemediğini sor
        again = input("\nBaşka bir şehir için hava durumu sorgulamak ister misiniz? (E/H): ")
        if again.strip().lower() != 'e':
            print("Hava durumu uygulamasını kullandığınız için teşekkürler!")
            break

if __name__ == "__main__":
    main()