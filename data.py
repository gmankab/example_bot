from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher
from dataclasses import dataclass
from config import TOKEN
import pandas as pd
import logging


def make_users():
    pd.DataFrame({
        'users': ['jolygmanka', 'jolygmank'],
        'languages': ['ru', 'en']
    }).to_csv(r'data\users', index=False)


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dataclass()
class Languages:
    default = 'english'

    short_emoji = [
        ['🇬🇧', 'english'],
        ['🇨🇳', 'chinese'],
        ['🇮🇳', 'hindi'],
        ['🇪🇸', 'spanish'],
        ['🇪🇭', 'arabic'],
        ['🇧🇩', 'bengali'],
        ['🇫🇷', 'french'],
        ['🇷🇺', 'russian'],
        ['🇵🇹', 'portuguese'],
    ]

    short = [
        'english',
        'chinese',
        'hindi',
        'spanish',
        'arabic',
        'bengali',
        'french',
        'russian',
        'portuguese',
    ]

    @dataclass()
    class Supported:
        dict = {v: k for k, v in GoogleTranslator.get_supported_languages(as_dict=True).items()}
        abbreviations = list(GoogleTranslator.get_supported_languages(as_dict=True).values())
        list = GoogleTranslator.get_supported_languages()

    users = pd.read_csv(r'data\users.csv')

    users_list = list(users['user'])

    @staticmethod
    def get(username):
        return Languages.users.loc[Languages.users['user'] == username]['language'].iloc[0]
