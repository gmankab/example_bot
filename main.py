from deep_translator import GoogleTranslator
import keyboards as kb
from data import *


async def r(msg, answers=None, reply_markup=None):
    lang = users.loc[users['user'] == msg.from_user.username]['language'].iloc[0]
    text = ''
    if not answers:
        text = msg.text
    else:
        if lang in answers.keys():
            for i in answers[lang]:
                text += i + '\n\n'
        else:
            for i in answers['en']:
                text += GoogleTranslator(source=language, target='ru').translate(i) + '\n\n'

        if lang != 'en' and 'forced' in answers.keys():
            text = text[:-2] + f' ({answers["forced"][0]}):'
    await msg.reply(text, reply=False, reply_markup=reply_markup)


# This handler will be called when user sends `/start` or `/help` command1
@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def process_start_command(message: types.Message):
    lngs = pd.read_csv('data/languages.csv')
    # print(lngs)
    await r(message,
            answers={
                'ru': [
                    'сделаю любого телеграм бота за 1500 рублей - @jolygmanka',
                    'выберите ваш язык чтобы продолжить',
                    ],
                'en': [
                    'i will make any telegram bot for $20 - @jolygmanka',
                    'chose your language to continue'
                    ],
                'forced': [
                    'chose your language to continue',
                    ]},
            reply_markup=kb.lang
            )


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await r(message)


@dp.callback_query_handler(lambda callback: callback.data == 'pressed Первая кнопка!')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(test())
    executor.start_polling(dp)
