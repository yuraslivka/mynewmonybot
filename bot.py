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
from __future__ import print_function
import os.path
from re import A
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '182ULBylx-QdGFbsmIrP1yr83iq4RmiVOYZs9CZ8wrMU'
SAMPLE_RANGE_NAME = '2021!A1:Z56'

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

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    values2 = values[6]
    len_v2 = len(values2)
    """print(len_v2)
    print(values2[16])"""

    await bot.send_message(message.from_user.id, values2[16])


@dp.message_handler(commands=['USD'])
async def send_welcome(message: types.Message):

    r = requests.get("https://finance.i.ua/bank/115/")
    html = BS(r.content, 'html.parser')

    for el in html.select('.data_container > table'):
        title = el.select('span')
        print(title[4].text)

    await bot.send_message(message.from_user.id, "USD " + title[4].text + " " + title[1].text)


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
