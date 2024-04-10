# open Wetrhe = b59d4dea9e9c04f44236dd4348f57d7e

import requests
from dotenv import load_dotenv # type: ignore
import os
from pprint import pprint
load_dotenv()

def get_weather():
    print('\n*** Get current weather conditions***')
    city = input("\n enter city name:")


    requet_url =f'https://api.openweathermap.org/data/2.5/weather?appid=b59d4dea9e9c04f44236dd4348f57d7e&q={city}&units=metric'

    # print(requet_url)

    weather = requests.get(requet_url).json()
    # pprint(weather)
    print(f'\n Current weather for {weather["name"]}')
    print(f'\n Temprature is  {weather["main"]["temp"]}')
    print(f'\n feels like {weather["main"]["feels_like"]} and {weather["weather"][0]["description"]}')


if __name__ == "__main__":
    get_weather()