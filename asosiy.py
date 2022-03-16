from aiogram import Bot,Dispatcher,types,executor
from aiogram.types import  Message
kalit ='5158535115:AAEHrvNi-jBobTK0blJ3pgx2Te5x9AsLyyU'
bot =Bot(token=kalit)

dp =Dispatcher(bot)

@dp.message_handler(commands='start')
async def xabar(malumot:Message):
    await malumot.answer(text='salom dasturchilar')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)