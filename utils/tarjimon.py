# from aiogram import types
# from googletrans import Translator
# from loader import dp
#
# tarjimon=Translator()
#
# # Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     soz =message.text
#     til =tarjimon.detect(soz).lang
#     print(til)
#     if til =='uz':
#
#         english=tarjimon.translate(soz,dest='en',src='uz').text
#         await message.answer(text=f'🇺🇸 {english}')
#         english = tarjimon.translate(soz, dest='ru', src='uz').text
#         await message.answer(text=f'🇷🇺{english}')
#
#     elif til=='ru':
#
#         english = tarjimon.translate(soz, dest='en', src='ru').text
#         await message.answer(text=f'🇺🇸{english}')
#         english = tarjimon.translate(soz, dest='uz', src='ru').text
#         await message.answer(text=f'🇺🇿{english}')
#
#     elif til=='en':
#         english = tarjimon.translate(soz, dest='ru', src='en').text
#         await message.answer(text=f'🇷🇺{english}')
#         english = tarjimon.translate(soz, dest='uz', src='en').text
#         await message.answer(text=f'🇺🇿{english}')














