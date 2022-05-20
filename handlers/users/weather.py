import requests
from aiogram import types

from loader import dp,bot
@dp.message_handler(commands='start2')
async def bot_echo(message: types.Message):

 url = "https://aladhan.p.rapidapi.com/timingsByCity"




 querystring = {"country":"Uzbekistan","city":"Fergana"}

 headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

 responsee = requests.request("GET", url, headers=headers, params=querystring,)
 kun = responsee.json()['data']['date']['readable']
 await message.answer(f'Bugungi Kun {kun}')
 print(responsee.text)
