
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uzbek🇺🇿',callback_data='uzb🇺🇿'),
            InlineKeyboardButton(text='English🇺🇸',callback_data='eng🇺🇸')
        ],

    ]
)