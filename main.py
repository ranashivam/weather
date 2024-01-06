import requests

API_KEY = "f838eb899c5e1212b99cd41ae15161ad"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input('Enter a city: ')
requestUrl = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(requestUrl)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]['description']
    print(f"weather at {city} is {weather}")

    #converting to celcius and rounding upto 2 digits
    temperature = (data["main"]["temp"] -273.15).__round__(2)
    print(f"Temperature at {city} is {temperature} celcius")

else:
    print('An Error Occurred!!')
