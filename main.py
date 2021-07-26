from aiogram import executor, types
from keyboards import *
from functions import *


# This handler will be called when user sends /start or /help command
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
    text = t('i will make any telegram bot for $20 - @jolygmanka', language)
    await message.reply(text, reply=False, reply_markup=GetKeyboards.info(language))


@dp.callback_query_handler(lambda callback: callback.data == 'change lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           '(powered by google translate)\nchose your language:', reply_markup=Keyboards.change_lang)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data in Langs.short)
async def callback_change_lang(callback_query: types.CallbackQuery):
    language = callback_query.data
    await bot.send_message(callback_query.from_user.id, t('Your language is', language),
                           reply_markup=Keyboards.help)
    await bot.answer_callback_query(callback_query.id)
    set_language(callback_query.from_user.username, language)


@dp.callback_query_handler(lambda callback: callback.data == 'other lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'write /l {name of your language} to set language,\n'
                                                        'or /c to cancel.\n'
                                                        'examples:', reply_markup=Keyboards.set_lang)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '/l english')
    await bot.send_message(callback_query.from_user.id, '/l en')
    await bot.send_message(callback_query.from_user.id, '/l russian')


# This handler will be called when user sends /lang command
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


# aboba
@dp.message_handler(lambda message: message.text in ['aboba', 'абоба', '🅰️🅱️🅾️🅱️🅰️'])
async def echo(message: types.Message):
    await message.reply('🅰️🅱️🅾️🅱️🅰️', reply=False, reply_markup=Keyboards.help)


@dp.message_handler(commands=['c', 'can', 'canc', 'cancel'])
async def echo(message: types.Message):
    await message.reply(t('action canceled',
                          Users.langs[message.from_user.username]), reply=False, reply_markup=Keyboards.help)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(test())
    executor.start_polling(dp)
