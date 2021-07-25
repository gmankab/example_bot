from aiogram import executor, types
from keyboards import *
from functions import *


# This handler will be called when user sends /start or /help command
@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def start_help_command(message: types.Message):
    username = message.from_user.username
    if username not in Languages.users_list:
        language_user_set(message.from_user.language_code, username)
    language = Languages.users.loc[Languages.users['user'] == username]['language'].iloc[0]

    text = 'get this message'
    if language != 'english':
        text = GoogleTranslator(source=Languages.default, target=language).translate(text)
    await message.reply('/help - ' + text, reply=False, reply_markup=Keyboards.help)

    if language == 'russian':
        text = 'сделаю любого телеграм бота за 1500 рублей - @jolygmanka'
    else:
        text = 'i will make any telegram bot for $20 - @jolygmanka'
        if language != 'english':
            text = GoogleTranslator(source=Languages.default, target=language).translate(text)
    await message.reply(text, reply=False, reply_markup=GetKeyboards.info(language))


@dp.callback_query_handler(lambda callback: callback.data == 'change lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           '(powered by google translate)\nchose your language:', reply_markup=Keyboards.change_lang)


@dp.callback_query_handler(lambda callback: callback.data in Languages.short)
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    language = callback_query.data
    text = f'Your language is {language}'
    language = language.lower()
    if language != 'english':
        text = GoogleTranslator(source=Languages.default, target=language).translate(text)

    username = callback_query.from_user.username
    change_language(language, username)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=Keyboards.help)


@dp.callback_query_handler(lambda callback: callback.data == 'other lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'write /l {name of your language} to set language,\n'
                                                        'or /c to cancel.\n'
                                                        'examples:', reply_markup=Keyboards.set_lang)
    await bot.send_message(callback_query.from_user.id, '/l english')
    await bot.send_message(callback_query.from_user.id, '/l en')
    await bot.send_message(callback_query.from_user.id, '/l russian')


# This handler will be called when user sends /lang command
@dp.message_handler(commands=['lang', 'l', 'language'])
async def start_help_command(message: types.Message):
    language = message.text.split()[-1]
    if language in Languages.Supported.abbreviations:
        language = Languages.Supported.dict[language]
    if language in Languages.Supported.list:
        change_language(language, message.from_user.username)
        text = f'Your language is {language}'
        if language != 'english':
            text = GoogleTranslator(source=Languages.default, target=language).translate(text)
        await message.reply(text, reply=False, reply_markup=Keyboards.help)
    else:
        await message.reply("google translate isn't support this language", reply=False, reply_markup=Keyboards.help)


# echo function
@dp.message_handler(lambda message: message.text in ['aboba', 'абоба', '🅰️🅱️🅾️🅱️🅰️'])
async def echo(message: types.Message):
    await message.reply('🅰️🅱️🅾️🅱️🅰️', reply=False, reply_markup=Keyboards.help)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(test())
    executor.start_polling(dp)
