from aiogram import executor, types
from keyboards import *
from functions import *


# This handler will be called when user sends `/start` or `/help` command1
@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def start_help_command(message: types.Message):
    if message.from_user.username not in users_list:
        set_language(message.from_user.language_code, message.from_user.username)
    await r(message,
            answers={
                'ru': [
                    'сделаю любого телеграм бота за 1500 рублей - @jolygmanka',
                    ],
                'en': [
                    'i will make any telegram bot for $20 - @jolygmanka',
                    ]},
            reply_markup=Kb.info
            )


# echo function
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await r(message)


@dp.callback_query_handler(lambda callback: callback.data == 'change lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'chose your language:', reply_markup=Kb.lang)


@dp.callback_query_handler(lambda callback: callback.data in Languages.short)
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    language = callback_query.data
    text = f'Your language is {language}'
    language = language.lower()
    if language != 'english':
        text = GoogleTranslator(source=Languages.default, target=language).translate(text)

    username = callback_query.from_user.username
    if username in users_list:
        index = Languages.users.loc[Languages.users['user'] == username].index[0]
        Languages.users['language'][index] = language
        Languages.users.to_csv(r'data\users.csv', index=False)
    else:
        set_language(language, username)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=Kb.help)


@dp.callback_query_handler(lambda callback: callback.data == 'other lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(test())
    executor.start_polling(dp)
