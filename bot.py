import config
import logging
import asyncio
import aioschedule
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keybords import kb_client
import os


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
    await message.reply("Hi!\nI'm EchoBot!\nPowered by Yurii!")


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


async def noon_print():
    print("It's noon!")


async def scheduler():
    aioschedule.every().day.at("13:50").do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
