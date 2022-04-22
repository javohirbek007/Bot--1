from aiogram import types
from aiogram.types import ContentType

from loader import dp, bot
from filters import Guruh





# Echo bot
@dp.message_handler(Guruh(),content_types=ContentType.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].first_name
    await message.answer(text=f"Guruhga hush kelibsiz{ism}")
    await message.delete()
@dp.message_handler(Guruh(),content_types=ContentType.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.username
    user_id = message.from_user.id
    message_id = message.message_id
    await message.answer(text=f"Guruhni tark etdi {ism}")
    await message.delete()

@dp.message_handler(Guruh(),content_types=ContentType.STICKER)
async def bot_echo(message: types.Message):
    await message.delete()

@dp.message_handler(Guruh(),content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.delete()

@dp.message_handler(Guruh(),content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.delete()

@dp.message_handler(Guruh(),content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.delete()

@dp.message_handler(Guruh(),content_types=ContentType.UNKNOWN)
async def bot_echo(message: types.Message):
    await message.delete()






