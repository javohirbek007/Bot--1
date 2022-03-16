import requests
from loader import dp,bot
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
open_weather_token='d539db765863110016b27d8e1998f082'






@dp.message_handler(commands=["weather"])
async def start_command(message: types.Message):
    await message.reply("Salom Menga shahar nomini yuboring, men sizga ob-havo hisobotini yuboraman!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Yorug'lik \U00002600",
        "Clouds": "bulutli \U00002601",
        "Rain": " Yomg'ir\U00002614",
        "Drizzle": "Yomg'ir \U00002614",
        "Thunderstorm": "Momaqaldiroq \U000026A1",
        "Snow": "Qor \U0001F328",
        "Mist": "Tuman \U0001F32B"
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
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Shahar ob-havosi: {city}\nHarorat: {cur_weather}C° {wd}\n"
              f"Namlik: {humidity}%\nBosim: {pressure} мм.рт.ст\nShamol: {wind} м/с\n"
              f"Quyosh chiqishi: {sunrise_timestamp}\nQuyosh botishi: {sunset_timestamp}\nKun uzunligi: {length_of_the_day}\n"
              f"***Yaxshi kun!***"
              )

    except:
        await message.reply("\U00002620 Shahar nomini tekshiring \U00002620")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
