import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import subprocess
import shutil
import pyautogui

try:
    shutil.rmtree(r"C:\chrometemp")  # remove Cookie, Cache files
except FileNotFoundError:
    pass

try:
    subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')  # Open the debugger chrome

except FileNotFoundError:
    subprocess.Popen(r'C:\Users\binsu\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

driver.get(
    url='https://lostark.game.onstove.com/Shop#mari')

time.sleep(1)
element = driver.find_element(By.ID, "login-btn")
element.click()

time.sleep(1)
element = driver.find_element(By.ID, "google_login")
element.click()

driver.implicitly_wait(10)

time.sleep(3)
pyautogui.write('###ID###')  # Fill in your ID or E-mail
pyautogui.press('tab', presses=2)  # Press the Tab key 2 times
pyautogui.press('enter')
time.sleep(3)  # wait a process
pyautogui.write('###PW###')  # Fill in your PW
pyautogui.press('tab', presses=2)  # Press the Tab key 2 times
pyautogui.press('enter')

time.sleep(10)
element = driver.find_element(By.ID, "otp")
element.click()
time.sleep(10)

# 전투 생활 탭으로
element = driver.find_element(By.LINK_TEXT, "전투ㆍ생활 추천")
element.click()
time.sleep(3)

# 전희팩 구매
try:
    element = driver.find_element(By.XPATH, "//button[@type='button'][@class='bt-buy'][@data-itemcode='1100508']")
    element.click()
except:
    sys.exit()

# 동의
element = driver.find_element(By.XPATH, "//label[@for='check-agreement1'][@class='label']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//label[@for='check-agreement2'][@class='label']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='button'][@class='lui-modal__payment']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='button'][@name='btnRandompad'][text()='4']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='button'][@name='btnRandompad'][text()='1']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='button'][@name='btnRandompad'][text()='4']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='button'][@name='btnRandompad'][text()='1']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='button'][@name='btnRandompad'][text()='4']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='button'][@name='btnRandompad'][text()='1']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//button[@type='submit'][@class='button button--password-confirm']")
element.click()

print("done")
