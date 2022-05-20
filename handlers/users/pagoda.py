import requests
from aiogram import types

from loader import dp,bot
@dp.message_handler(commands='start')
async def bot_echo(message: types.Message):


  url = "https://aladhan.p.rapidapi.com/timingsByCity"




  querystring = {"country":"Uzbekistan","city":"Fergana"}

  headers = {
	  "X-RapidAPI-Host": "aladhan.p.rapidapi.com",
	  "X-RapidAPI-Key": "97b85ad4bamshc8d26e874eace29p17b6b1jsn2ce1c74f607b"
  }

  responsee = requests.request("GET", url, headers=headers, params=querystring,)

  link = "https://islomapi.uz/api/present/day?region=Farg'оna"

  response = requests.request('GET',link)
  print(response.text)

  kun = responsee.json()['data']['date']['readable']
  hijri_vaqt = responsee.json()['data']['date']['hijri']['date']
  hijr_oyn = responsee.json()['data']['date']['hijri']['month']['number']
  hijr_oy = responsee.json()['data']['date']['hijri']['month']['en']

  hafta_kuni_hijri = responsee.json()['data']['date']['hijri']['weekday']['en']

  kun = response.json()['date']
  hafta_kuni = response.json()['weekday']

  bomdod = response.json()['times']['tong_saharlik']
  quyosh_chiqishi = response.json()['times']['quyosh']
  peshin = response.json()['times']['peshin']
  asr = response.json()['times']['asr']
  shom = response.json()['times']['shom_iftor']
  xufton = response.json()['times']['hufton']

  user_id = message.from_user.id
  await message.answer(text='🔻 Namoz vaqtlari: Farg\'ona\n\n'+'🌅Quyosh - '+quyosh_chiqishi+
                      '\n🕰Tong - '+bomdod+'\n🕰Peshin vaqti - '+peshin
                       +'\n🕰Asr vaqti - '+asr+'\n🕰Shom vaqti - '+shom+'\n🕰Xufton vaqti - '+xufton+'\nBugun - '+kun+'\nHaftaning '+hafta_kuni +' kuni'
                       + 'Hijri')



