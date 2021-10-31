import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://finance.i.ua/bank/115/")
html = BS(r.content, 'html.parser')

for el in html.select('.data_container > table'):
    title = el.select('span')

    print(title[4].text + " " + title[1].text)
