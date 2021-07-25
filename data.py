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
        ['🇬🇧', 'English'],
        ['🇨🇳', 'Chinese'],
        ['🇮🇳', 'Hindi'],
        ['🇪🇸', 'Spanish'],
        ['🇪🇭', 'Arabic'],
        ['🇧🇩', 'Bengali'],
        ['🇫🇷', 'French'],
        ['🇷🇺', 'Russian'],
        ['🇵🇹', 'Portuguese'],
    ]

    short = [
        'English',
        'Chinese',
        'Hindi',
        'Spanish',
        'Arabic',
        'Bengali',
        'French',
        'Russian',
        'Portuguese',
    ]

    @dataclass()
    class Supported:
        dict = {v: k for k, v in GoogleTranslator.get_supported_languages(as_dict=True).items()}
        abbreviations = GoogleTranslator.get_supported_languages(as_dict=True).values()
        list = GoogleTranslator.get_supported_languages

    users = pd.read_csv(r'data\users.csv')


users_list = list(Languages.users['user'])
