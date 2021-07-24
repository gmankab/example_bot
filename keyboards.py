from data import languages_emoji
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup()


step = 0
for i in languages_emoji:
    button = InlineKeyboardButton(f'{i[0]} {i[1]}', callback_data=i[1])
    if step == 2:
        lang.add(button)
    else:
        lang.insert(button)

info = InlineKeyboardMarkup().add(
    InlineKeyboardButton('@jolygmanka', url='t.me/jolygmanka'),
    InlineKeyboardButton(f'🌐 change language', callback_data='change lang')
)

help_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/help'))
