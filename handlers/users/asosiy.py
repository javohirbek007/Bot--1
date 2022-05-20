import requests
from aiogram import types

from loader import dp,bot
@dp.message_handler(commands='valyut')
async def bot_echo(message: types.Message):
 link = "https://v6.exchangerate-api.com/v6/4fd9995dd7aa8c9bfdff90f1/latest/USD"
 response = requests.request('GET', link)
 UZS=response.json()['conversion_rates']['UZS']
 rubl=response.json()['conversion_rates']['RUB']
 yevro=response.json()['conversion_rates']['EUR']
 await message.answer(f'{UZS}🇺🇿\n{rubl}🇷🇺\n{yevro}💴')



 print(response.text)