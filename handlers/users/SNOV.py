from aiogram import types
from loader import dp,bot
import requests





@dp.message_handler(commands='vaqt')
async def bot(message:types.Message):
  url = "https://dailyprayer.abdulrcs.repl.co/api/Tashkent"
  response = requests.request('GET',url)
  shaxar = response.json()['city']
  Fajr = response.json()['today']['Fajr']
  Quyosh = response.json()['today']['Sunrise']
  Dhuhr = response.json()['today']['Dhuhr']
  Asr = response.json()['today']['Asr']
  Maghrib = response.json()['today']['Maghrib']
  Ishaa = response.json()["today"]["Isha'a"]
  await message.answer(f'Viloyat  {shaxar}\nTong {Fajr}\nQuyosh {Quyosh}\nPeshin  {Dhuhr}\nASR {Asr}\nShom  {Maghrib}\nHufton  {Ishaa}')
  print(response.text)
  user_id = message.from_user.id















