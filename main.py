from dotenv import load_dotenv
import os
import requests, json 

load_dotenv()

WEATHER_FORECASET_API = os.getenv("WEATHER_FORECASET_API")

base_url = "http://api.openweathermap.org/data/2.5/weather?"

def weatherforecastusingopenweatherapi(city_name):

    URL = base_url + "appid=" + WEATHER_FORECASET_API + "&q=" + city_name

    response = requests.get(URL)

    return response.json()


city_name = input("Enter city name : ")

weatherforecast = weatherforecastusingopenweatherapi(city_name)

# print(type(weatherforecast))
# print(weatherforecast)

if weatherforecast["cod"] != "404":

    main = weatherforecast["main"]

    temperature = main["temp"]

    humidity = main["humidity"]

    pressure = main["pressure"]

    report = weatherforecast["weather"]


    print(f"{city_name:_^30}")

    print(f"main: {report[0]['main']}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")  

else:
    print("City Not Found")

city_vis = requests.get(f'http://wttr.in/{city_name}', headers={'user-agent':'curl'})
print(city_vis.text)