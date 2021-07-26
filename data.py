from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher
from dataclasses import dataclass
from config import TOKEN
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dataclass()
class Langs:
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

    dict = {val: key for key, val in GoogleTranslator.get_supported_languages(as_dict=True).items()}
    index = {}

    abbreviations = list(GoogleTranslator.get_supported_languages(as_dict=True).values())
    list = GoogleTranslator.get_supported_languages()
    translations = pd.read_csv(r'data\translations.csv')


@dataclass()
class Users:
    df = pd.read_csv(r'data\users.csv')
    list = list(df['user'])
    langs = {}

    for i in df.index:
        langs[df['user'][i]] = df['language'][i]
