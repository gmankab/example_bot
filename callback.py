from keyboards import *
from aiogram import types
from random import randint


@dp.callback_query_handler(lambda callback: callback.data == 'change lang')
async def query_change_lang(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, '(powered by google translate)\n'
                                                        'chose your language:', reply_markup=Keyboards.change_lang)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data in Langs.short)
async def query_set_language(callback_query: types.CallbackQuery):
    language = callback_query.data
    set_language(callback_query.from_user.username, language)
    await bot.send_message(callback_query.from_user.id, t('Your language is', language),
                           reply_markup=Keyboards.help)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data == 'advanced')
async def advanced(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=GetKeyboards.advanced_info(
                                                   language=Users.langs[callback_query.from_user.username][0]))
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data == 'hide advanced')
async def info(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=GetKeyboards.info(
                                                   language=Users.langs[callback_query.from_user.username][0]))
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data == 'flip a coin')
async def info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, [
        t('tails', language=Users.langs[callback_query.from_user.username][0]),
        t('heads', language=Users.langs[callback_query.from_user.username][0]),
    ][randint(0, 1)])
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data == 'translate')
async def info(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           t('write /t {source language} {what language to translate into} {text to translate}',
                             language=Users.langs[callback_query.from_user.username][0])
                           + '\n' +
                           t('example:',
                             language=Users.langs[callback_query.from_user.username][0]))
    await bot.send_message(callback_query.from_user.id, '/t en ru hello world')
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data == 'other lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'write /l {name of your language} to set language,\n'
                                                        'or /c to cancel.\n'
                                                        'examples:', reply_markup=Keyboards.set_lang)
    await bot.send_message(callback_query.from_user.id, '/l english')
    await bot.send_message(callback_query.from_user.id, '/l en')
    await bot.send_message(callback_query.from_user.id, '/l russian')
    await bot.answer_callback_query(callback_query.id)


def fuck_pycharm_import_warnings_callback():
    pass
