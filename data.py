from aiogram import Bot, Dispatcher, executor, types
from dataclasses import dataclass
from config import *
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

default_language = 'en'


languages_emoji = [
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

languages = [
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