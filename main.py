# from pprint import pp
# test 2
import keyboards as kb
import logging
from config import *
from aiogram import Bot, Dispatcher, executor, types
from translate import Translator
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
translator = Translator(to_lang='ru', from_lang='en')


async def t(to_translate):
    return translator.translate(to_translate)


# This handler will be called when user sends `/start` or `/help` command1
@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def process_start_command(message: types.Message):
    lngs = pd.read_csv('languages.csv')
    # print(lngs)
    await message.reply(await t(
        '''Сделаю любого телеграмм-бота за 20$
        
        chose your language:'''
    ))


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(await t(message.text))


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(test())
    executor.start_polling(dp)
