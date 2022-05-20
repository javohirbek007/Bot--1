from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.til1 import inline_menu
from loader import dp


@dp.message_handler(commands='lang')
async def bot_start(message: types.Message):
    await message.answer(text='Tilni tanlang👇',reply_markup=inline_menu)
