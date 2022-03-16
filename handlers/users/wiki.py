# import wikipedia
# from aiogram import types
# from loader import dp
# @dp.message_handler(commands='wiki')
# async def bot_echo(message: types.Message):
#     await message.answer(text='maqola kiritng')
#
#
# wikipedia.set_lang('uz')
# @dp.message_handler()
#
# async def wikiPedia(message: types.Message):
#     try:
#         repsond = wikipedia.summary(message.text)
#         await message.answer(repsond)
#     except:
#         await message.answer("Siz izlagan maqola mavjud emas")
#
