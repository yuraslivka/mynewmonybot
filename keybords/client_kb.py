from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/f')
b2 = KeyboardButton('/h')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2)
