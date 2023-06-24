from dotenv import load_dotenv
import os
import requests, json 

load_dotenv()

WEATHER_FORECASET_API = os.getenv("WEATHER_FORECASET_API")

MONGO_DB_API = os.getenv("MONGO_DB_API")

base_url = "http://api.openweathermap.org/data/2.5/weather?"

def weatherforecastusingopenweatherapi(city_name):

    URL = base_url + "appid=" + WEATHER_FORECASET_API + "&q=" + city_name

    response = requests.get(URL)

    return response.json()


city_name = input("Enter city name : ")

weatherforecast = weatherforecastusingopenweatherapi(city_name)

# print(type(weatherforecast))
# print(weatherforecast)

def kelvinToCelsius(kelvin):
    return kelvin - 273.15

def metertokilometer(visibility):
    return visibility / 1000

if weatherforecast["cod"] != "404":

    main = weatherforecast["main"]

    temperature = main["temp"]

    temperature_celsius = kelvinToCelsius(temperature)

    humidity = main["humidity"]

    pressure = main["pressure"]

    report = weatherforecast["weather"]

    description = report[0]["description"]

    visibility_km = metertokilometer(weatherforecast["visibility"])



    print(f"{city_name:_^30}")

    print(f"main: {report[0]['main']}")
    print(f"Temperature: {round(temperature_celsius, 2)} °C")
    print(f"Weather Report: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")  
    print(f"Visibility: {visibility_km} km")

    

else:
    print("City Not Found")

# city_vis = requests.get(f'http://wttr.in/{city_name}', headers={'user-agent':'curl'})
# print(city_vis.text)