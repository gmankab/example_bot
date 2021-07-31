from install_dependencies import *
from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from dataclasses import dataclass
from config import TOKEN
import pandas as pd
import logging
from deep_translator import exceptions

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
    translations = pd.read_csv(r'translations.csv')


@dataclass()
class Users:
    langs = pd.read_csv(r'users.csv')
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
fuck_pycharm_import_warning_install_dependencies()

exceptions_translate = (exceptions.AuthorizationException,
                        exceptions.BaseError,
                        exceptions.ElementNotFoundInGetRequest,
                        exceptions.InvalidSourceOrTargetLanguage,
                        exceptions.LanguageNotSupportedException,
                        exceptions.MicrosoftAPIerror,
                        exceptions.NotValidLength,
                        exceptions.NotValidPayload,
                        exceptions.RequestError,
                        exceptions.ServerException,
                        exceptions.TooManyRequests,
                        exceptions.TranslationNotFound,
                        IndexError)
