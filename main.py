from data import *


async def r(msg, answers=None):
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
                text += i + '\n\n'
            text.join(answers['force'] + '\n\n')
            Translate.translator = Translator(to_lang=lang, from_lang='en')
            text = Translate.translator.translate(text)
        if lang != 'en':
            text = text[:-3] + ', '
        for i in answers.get('forced', ''):
            text += i
    await msg.reply(text, reply=False)


# This handler will be called when user sends `/start` or `/help` command1
@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def process_start_command(message: types.Message):
    lngs = pd.read_csv('data/languages.csv')
    # print(lngs)
    await r(message,
            answers={
                'ru': [
                    'сделаю любого телеграм бота за 1500 рублей - @jolygmanka',
                    'выберите ваш язык чтобы продолжить,',
                    ],
                'en': [
                    'i will make any telegram bot for $20 - @jolygmanka',
                    ],
                'forced': [
                    'chose your language to continue:',
                    ]
            })


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await r(message)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(test())
    executor.start_polling(dp)
