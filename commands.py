from aiogram import types
from keyboards import *
from functions import *
from data import *


@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def start_help_command(message: types.Message):
    username = message.from_user.username
    if username not in Users.list:
        language = message.from_user.language_code
        if language in Langs.abbreviations:
            language = Langs.dict[language]
        else:
            language = 'english'
        set_language(username, language)
    else:
        language = Users.langs[username][0]

    text = t('get this message', language)
    await message.reply('/help - ' + text, reply=False, reply_markup=Keyboards.help)
    text = t('i will make any telegram bot - @jolygmanka', language)
    await message.reply(text, reply=False, reply_markup=GetKeyboards.info(language))


@dp.message_handler(commands=['lang', 'l', 'language'])
async def start_help_command(message: types.Message):
    language = message.text.split()[-1]
    if language in Langs.abbreviations:
        language = Langs.dict[language]
    if language in Langs.list:
        set_language(message.from_user.username, language)
        await message.reply(t('Your language is', language), reply=False, reply_markup=Keyboards.help)
    else:
        await message.reply("google translate isn't support this language", reply=False, reply_markup=Keyboards.help)


@dp.message_handler(commands=['c', 'can', 'canc', 'cancel'])
async def cancel(message: types.Message):
    await message.reply(t('action canceled',
                          Users.langs[message.from_user.username]), reply=False, reply_markup=Keyboards.help)


@dp.message_handler(commands=['t', 'trans', 'translate'])
async def cancel(message: types.Message):
    try:
        splitted = message.text.split()
        text = message.text.split(splitted[2], 1)[1]
        text = GoogleTranslator(source=splitted[1], target=splitted[2]).translate(text)
        await message.reply(text, reply=False, reply_markup=Keyboards.help)
    except exceptions_translate:
        await message.reply(t('error translating', Users.langs[message.from_user.username][0]), reply=False)


def fuck_pycharm_import_warning_commands():
    pass
