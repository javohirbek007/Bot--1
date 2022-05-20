import requests
from aiogram import types



from loader import dp,bot
@dp.message_handler(commands='start1')
async def bot_echo(message: types.Message):
 url = "https://aladhan.p.rapidapi.com/timingsByCity"

 querystring = {"country": "Uzbekistan", "city": "Fergana"}

 headers = {
  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
 }

 responsee = requests.request("GET", url, headers=headers, params=querystring, )
 kun = responsee.json()['data']['date']['readable']

 link = "https://v6.exchangerate-api.com/v6/4fd9995dd7aa8c9bfdff90f1/latest/USD"
 response = requests.request('GET',link)
 Kurs = response.json() ['conversion_rate']
 base = response.json()['base_code']
 target =response.json()['target_code']
 bugungi_kun = response.json()['time_next_update_utc']
 user_id = message.from_user.id
 print(response.text)
 await message.answer(f'Sana  {kun}\n🇺🇿{Kurs} som,\n{base}')
 print(response.text)