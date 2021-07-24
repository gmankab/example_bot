from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup()

step = 0
for i in [
    ['en', '🇬🇧', 'English'],
    ['cn', '🇨🇳', 'Chinese'],
    ['hn', '🇮🇳', 'Hindi'],
    ['es', '🇪🇸', 'Spanish'],
    ['eh', '🇪🇭', 'Arabic'],
    ['bd', '🇧🇩', 'Bengali'],
    ['fr', '🇫🇷', 'French'],
    ['ru', '🇷🇺', 'Russian'],
    ['pt', '🇵🇹', 'Portuguese'],
]:
    button = InlineKeyboardButton(f'{i[1]} {i[0]} {i[2]}', callback_data=i[0])
    if step == 2:
        lang.add(button)
    else:
        lang.insert(button)
