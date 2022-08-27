import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. 크롤링
# 검색어
keyword = input("크롤링할 키워드 입력 : ")
size_input = input("크롤링할 갯수 : ")

# 크롬 드라이버
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.google.co.kr")

# 크롬창 띄우기
time.sleep(3)
print('크롬 open 완료')
