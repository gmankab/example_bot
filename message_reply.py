from aiogram import types
from keyboards import *
from data import *


@dp.message_handler()
async def aboba(message: types.Message):
    for world in message.text.split():
        if world in ['aboba', 'абоба', '🅰️🅱️🅾️🅱️🅰️']:
            await message.reply('🅰️🅱️🅾️🅱️🅰️', reply=True, reply_markup=Keyboards.help)
        if world == 'когда':
            await message.reply('завтра', reply=True, reply_markup=Keyboards.help)
