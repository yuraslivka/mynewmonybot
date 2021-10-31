import config
import logging
import asyncio
import requests
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keybords import kb_client
from bs4 import BeautifulSoup as BS


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
   This handler will be called when user sends `/start` or `/help` command
   """
    await bot.send_message(message.from_user.id, 'Hello Yurii', reply_markup=kb_client)


@dp.message_handler(commands=['f'])
async def send_welcome(message: types.Message):

    await bot.send_message(message.from_user.id, 'fuck off:)')


@dp.message_handler(commands=['USD'])
async def send_welcome(message: types.Message):

    r = requests.get("https://finance.i.ua/bank/115/")
    html = BS(r.content, 'html.parser')

    for el in html.select('.data_container > table'):
        title = el.select('span')
        await bot.send_message(message.from_user.id, title[4].text + " " + title[1].text)


@dp.message_handler()
async def echo(message: types.Message):
    b = int(message.text)

    if message.text.lower() == "0":
        await message.answer('Fuck you.')
    else:
        if message.text.lower() == '1':
            await message.answer('Hello!.')
        else:
            await message.answer(6*b)


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
