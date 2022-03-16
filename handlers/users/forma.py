# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ReplyKeyboardRemove
# from states.holatlar import Forma
# from loader import dp,bot
# from keyboards.default.tasdiqlash import asosiy_tasdiqlash
#
# # Echo bot
# @dp.message_handler(commands='forma')
# async def bot_echo(message: types.Message):
#     await message.answer(text='Ismni kiriting ')
#     await Forma.ism_qabul_qilish.set()
#
# lugat = {}
# @dp.message_handler(state=Forma.ism_qabul_qilish) # if
# async def bot_echo(message: types.Message,state:FSMContext):
#     ism = message.text
#     id = message.from_user.id
#     await state.update_data({'ism':ism})
#     await message.answer(text='Familyani kiriting') # elif
#     await Forma.fam_qabul_qilish.set()
#
#
# @dp.message_handler(state=Forma.fam_qabul_qilish) #elif
# async def bot_echo(message: types.Message,state:FSMContext):
#     familya = message.text
#     id = message.from_user.id
#     await state.update_data({'fam':familya})
#     await message.answer(text='Yoshni kiriting')
#     await Forma.yosh_qabul_qilish.set()
#
# @dp.message_handler(state=Forma.yosh_qabul_qilish) # elif
# async def bot_echo(message: types.Message,state:FSMContext):
#     yosh = message.text
#     id = message.from_user.id
#     await state.update_data({'yosh':yosh})
#     await message.answer(text='Manzilni kiriting')
#     await Forma.manzil_qabul_qilish.set()
#
#
# @dp.message_handler(state=Forma.manzil_qabul_qilish) # elif
# async def bot_echo(message: types.Message,state:FSMContext):
#     manzil = message.text
#     id = message.from_user.id
#     await state.update_data({'manzil':manzil})
#     await message.answer(text='Nomerni kiriting')
#     await Forma.nomer_qabul_qilish.set()
#
#
# @dp.message_handler(state=Forma.nomer_qabul_qilish) # elif
# async def bot_echo(message: types.Message,state:FSMContext):
#     nomer = message.text
#     id = message.from_user.id
#     await state.update_data({'nomer': nomer})
#     await message.answer(text='Murojatni kiriting')
#     await Forma.murojat_qabul_qilish.set()
#
#
# @dp.message_handler(state=Forma.murojat_qabul_qilish) # elif
# async def bot_echo(message: types.Message,state:FSMContext):
#     murojat = message.text
#     id = message.from_user.id
#     await state.update_data({'murojat': murojat})
#
#     data = await state.get_data()
#     ism = data.get('ism')
#     fam = data.get('fam')
#     yosh = data.get('yosh')
#     manzil= data.get('manzil')
#     tel = data.get('nomer')
#     textt = data.get('murojat')
#
#
#
#     matn =f'Ism :{ism} \n' \
#           f'familya :{fam} \n' \
#           f'yosh :{yosh} \n' \
#           f'manzil :{manzil} \n' \
#           f'tel :{tel} \n' \
#           f'murojat :{textt} \n'
#
#
#     await message.answer(text=f'{matn}',reply_markup=asosiy_tasdiqlash)
#     await Forma.tasdiqlash_qabul_qilish.set()
#
#
# @dp.message_handler(state=Forma.tasdiqlash_qabul_qilish,text='Bekor qilish') # elif
# async def bot_echo(message: types.Message):
#     await message.answer(text='Bekoq qilindi')
#
#
#
# @dp.message_handler(state=Forma.tasdiqlash_qabul_qilish,text='Tasdiqlash') # elif
# async def bot_echo(message: types.Message,state:FSMContext):
#
#     username = message.from_user.first_name
#     id = message.from_user.id
#     matn = f'Ushbu {username} quyidagi malumotni yubordi \n'
#
#
#
#     data = await state.get_data()
#     ism = data.get('ism')
#     fam = data.get('fam')
#     yosh = data.get('yosh')
#     manzil = data.get('manzil')
#     tel = data.get('nomer')
#     textt = data.get('murojat')
#
#     matn += f'Ism :{ism} \n' \
#            f'familya :{fam} \n' \
#            f'yosh :{yosh} \n' \
#            f'manzil :{manzil} \n' \
#            f'tel :{tel} \n' \
#            f'murojat :{textt} \n'
#     await message.answer(text='adminga yuborildi',reply_markup=ReplyKeyboardRemove())
#     await bot.send_message(chat_id=1722082854,text=matn,)
#     await state.finish()
#
