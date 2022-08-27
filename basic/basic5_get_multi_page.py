import requests
from bs4 import BeautifulSoup
import pyautogui

#검색어 변경하여 크롤링
#keyword = pyautogui.prompt('크롤링할 검색어 : ')
keyword = input('크롤링할 검색어 : ')
lastpage = int(input('마지막 페이지 번호 입력 : '))
page_num = 1
for i in range(1, lastpage * 10, 10):
    print(f"{page_num}페이지")
    page_num += 1
    response = requests.get(
        f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.news_tit')
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
