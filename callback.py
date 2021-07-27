from keyboards import *
from functions import *
from data import *


@dp.callback_query_handler(lambda callback: callback.data == 'change lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           '(powered by google translate)\nchose your language:', reply_markup=Keyboards.change_lang)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data in Langs.short)
async def callback_change_lang(callback_query: types.CallbackQuery):
    language = callback_query.data
    set_language(callback_query.from_user.username, language)
    await bot.send_message(callback_query.from_user.id, t('Your language is', language),
                           reply_markup=Keyboards.help)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data == 'advanced')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=GetKeyboards.info(
            language=Users.langs[callback_query.from_user.username]))
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda callback: callback.data == 'other lang')
async def callback_change_lang(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'write /l {name of your language} to set language,\n'
                                                        'or /c to cancel.\n'
                                                        'examples:', reply_markup=Keyboards.set_lang)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '/l english')
    await bot.send_message(callback_query.from_user.id, '/l en')
    await bot.send_message(callback_query.from_user.id, '/l russian')
