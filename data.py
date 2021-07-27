from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor
from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher
from dataclasses import dataclass
from config import TOKEN
import pandas as pd
import logging

imported = []


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
    langs = pd.read_csv(r'data\users.csv')
    list = list(langs.columns)


@dataclass()
class Get:
    @staticmethod
    def language_indexes():
        lang_index = 0
        for i in GoogleTranslator.get_supported_languages():
            Langs.index[i] = lang_index
            lang_index += 1


Get.language_indexes()
