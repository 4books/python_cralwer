import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = "/Users/naegwonhwang/Documents/data.xlsx"
wb = openpyxl.load_workbook(fpath)
ws = wb.active

# 종목 코드
codes = [
    '005930',
    '000660',
    '035720'
]

row = 3
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal').text
    price = price.replace(',', '')
    print(price)
    ws[f'B{row}'] = price
    row += 1

wb.save(fpath)
