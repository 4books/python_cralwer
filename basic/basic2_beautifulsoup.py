# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com')
html = response.text

#Beautiful soup html parser를 통해 파싱 진행
soup = BeautifulSoup(html, 'html.parser')
#id로 해당 html 태그를 가져옴
word = soup.select_one('#NM_set_home_btn')
print(word.text)




