from deep_translator import GoogleTranslator
from keyboards import *
from data import *


# translate message
async def r(msg, answers=None, reply_markup=None):
    language = users.loc[users['user'] == msg.from_user.username]['language'].iloc[0]
    text = ''
    if not answers:
        text = msg.text
    else:
        if language in answers.keys():
            for answer in answers[language]:
                text += answer + '\n\n'
        else:
            for answer in answers['en']:
                text += GoogleTranslator(source=default_language, target='ru').translate(answer) + '\n\n'

        if language != 'en' and 'forced' in answers.keys():
            text = text[:-2] + f' ({answers["forced"][0]}):'
    await msg.reply(text, reply=False, reply_markup=reply_markup)


# This handler will be called when user sends `/start` or `/help` command1
@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def start_help_command(message: types.Message):
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


@dp.callback_query_handler(lambda callback: callback.data in languages)
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    language = callback_query.data
    text = f'Your language is {language}'
    if language != 'English':
        text = GoogleTranslator(source=default_language, target=language.lower()).translate(text)

    username = callback_query.from_user.username
    if username in list(users['user']):
        index = users.loc[users['user'] == username].index[0]
        users['language'][index] = language
        users.to_csv(r'data\users.csv', index=False)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=Kb.help)


@dp.callback_query_handler(lambda callback: callback.data in languages)
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(test())
    executor.start_polling(dp)
