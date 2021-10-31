"""import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://finance.i.ua/bank/115/")
html = BS(r.content, 'html.parser')

for el in html.select('.data_container > table'):
    title = el.select('span')
    tb = float(title[1].text)*2

    print(tb)"""
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


def main():
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
    print(len_v2)
    print(values2[16])
    


if __name__ == '__main__':
    main()
