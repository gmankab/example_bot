from functions import *
from data import *


@dataclass()
class Keyboards:
    help = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/help'))
    set_lang = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('/help'), KeyboardButton('/lang english'), KeyboardButton('/cancel'))
    change_lang = None


@dataclass()
class GetKeyboards:
    @staticmethod
    def change_lang():
        step = 0
        Keyboards.change_lang = InlineKeyboardMarkup()
        for i in Langs.short_emoji:
            button = InlineKeyboardButton(f'{i[0]} {i[1]}', callback_data=i[1])
            if step == 2:
                Keyboards.change_lang.add(button)
            else:
                Keyboards.change_lang.insert(button)
        Keyboards.change_lang.add(InlineKeyboardButton('🌐 other language', callback_data='other lang'))

    @staticmethod
    def info(language):
        return InlineKeyboardMarkup().add(
            InlineKeyboardButton('@jolygmanka', url='t.me/jolygmanka'),
            InlineKeyboardButton(f'🌐 change language', callback_data='change lang'),
        ).add(
            InlineKeyboardButton(t('source code on github', language), url='https://github.com/gmankab/test_bot'),
            InlineKeyboardButton(t('what this bot can?', language), callback_data=f'advanced'),
        )

    @staticmethod
    def advanced_info(language):
        return InlineKeyboardMarkup().add(
            InlineKeyboardButton('@jolygmanka', url='t.me/jolygmanka'),
            InlineKeyboardButton(f'🌐 change language', callback_data='change lang'),
        ).add(
            InlineKeyboardButton(t('source code on github', language), url='https://github.com/gmankab/test_bot'),
            InlineKeyboardButton(t('hide advanced menu', language), callback_data='hide advanced'),
        ).add(
            InlineKeyboardButton(t('flip a coin', language), callback_data='flip a coin'),
            InlineKeyboardButton(t('translate something', language), callback_data='translate'),
        )


GetKeyboards.change_lang()
