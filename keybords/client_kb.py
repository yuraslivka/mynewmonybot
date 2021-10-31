from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('f')
b2 = KeyboardButton('USD')
b3 = KeyboardButton('im here', request_location=True)
b4 = KeyboardButton('1')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).insert(b3).insert(b4)
