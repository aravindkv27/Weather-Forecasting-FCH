from dotenv import load_dotenv
import os
import requests, json 
from pymongo import MongoClient

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
print(weatherforecast)

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
 
    try:
        conn = MongoClient(MONGO_DB_API)
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
    db=conn.database
    collection= db.WEATHER_FORECAST
    weather={
        "city": city_name,
        "temperature_celsius": temperature_celsius,
        "humidity": humidity,
        "pressure": pressure,
        "weather"  : report,
        "description": description
    }

    filter = {'city':city_name}
    
    update_values = {"$set":weather}

    checkCityName=collection.find_one({'city':city_name})
    if(checkCityName==None):
       collection.insert_one(weather)
    else:
        collection.update_one(filter, update_values)
        print("Updated")
    #print(checkCityName)
    #collection.insert_one(weather)
else:
    print("City Not Found")

city_vis = requests.get(f'http://wttr.in/{city_name}', headers={'user-agent':'curl'})
print(city_vis.text)