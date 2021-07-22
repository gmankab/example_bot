from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
button_hi = KeyboardButton('Привет! 👋')
hello = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for kb in [
    KeyboardButton('Привет! 👋'),
    KeyboardButton('123'),
]:
    hello.add(kb)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)