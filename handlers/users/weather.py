import requests
from loader import dp,bot
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
open_weather_token='d539db765863110016b27d8e1998f082'






@dp.callback_query_handler(text='eng🇺🇸')
async def bot_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name} Send me the name of the city and I will send you a weather report!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Lighting \U00002600",
        "Clouds": "cloudy \U00002601",
        "Rain": " Rain\U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunder \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look in the window, do not see what is there for the weather!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"City weather: {city}\nTemperature: {cur_weather}C° {wd}\n"
              f"Humidity: {humidity}%\nPressure: {pressure} мм.рт.ст\nThe wind: {wind} м/с\n"
              f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of day: {length_of_the_day}\n"
              f"***Good day!***"
              )

    except:
        await message.reply("\U00002620 Check the city name \U00002620")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
