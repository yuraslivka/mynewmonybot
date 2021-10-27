import config
import logging
import asyncio
import aioschedule
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types


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
    await message.reply("Hi!\nI'm EchoBot!\nPowered by Yurii!")


@dp.message_handler()
async def echo(message: types.Message):
    b = int(message.text)

    if message.text.lower() == '5':
        await message.answer('Fuck you.')
    else:
        await message.answer(b*5)


async def noon_print():
    print("It's noon!")


async def scheduler():
    aioschedule.every().day.at("15:54").do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
