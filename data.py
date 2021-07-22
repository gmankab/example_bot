from aiogram import Bot, Dispatcher, executor, types
from dataclasses import dataclass
from translate import Translator
from config import *
import keyboards as kb
import pandas as pd
import logging


def make_users():
    pd.DataFrame({
        'users': ['jolygmanka', 'jolygmank'],
        'languages': ['ru', 'en']
    }).to_csv(r'data\users', index=False)


users = pd.read_csv(r'data\users')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dataclass
class Translate:
    language = 'en'
    translator = Translator(to_lang='ru', from_lang='en')
