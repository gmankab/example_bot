from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import dataclass
from data import languages_emoji


@dataclass()
class Kb:
    info = InlineKeyboardMarkup().add(
        InlineKeyboardButton('@jolygmanka', url='t.me/jolygmanka'),
        InlineKeyboardButton(f'🌐 change language', callback_data='change lang')
    )

    help = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/help'))

    lang = InlineKeyboardMarkup()


def get_kb_lang():
    step = 0
    for i in languages_emoji:
        button = InlineKeyboardButton(f'{i[0]} {i[1]}', callback_data=i[1])
        if step == 2:
            Kb.lang.add(button)
        else:
            Kb.lang.insert(button)
    Kb.lang.add(InlineKeyboardButton('🌐 other language', callback_data='other language'))


get_kb_lang()
