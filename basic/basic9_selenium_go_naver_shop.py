import warnings

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 직접 chrome driver 호출
# browser = webdriver.Chrome('/Users/naegwonhwang/Documents/chromedriver')

# 설치된 Chrome으로 실행
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())

# DeprecatedWarning 로그 무시
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 셀레니움 로그 무시
warnings.filterwarnings("ignore", category=DeprecationWarning)  # Deprecated options 무시

browser = webdriver.Chrome('/Users/naegwonhwang/Documents/chromedriver', options=chrome_options)
browser.get("https://www.naver.com")
browser.implicitly_wait(10)

# 네이버 쇼핑 이동
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
browser.implicitly_wait(10)

search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_input_QXUFf')
search.click()
search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)

while True:
    pass
