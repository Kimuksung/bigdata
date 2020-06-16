from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

#네이버 자동 로그인 방지 함수
#너무 빠르게 접속 및 값이 이미 있는것들을 방지한다.

def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

id = 'kimuksung5'
pw = 'hannah0603!'

driver = webdriver.Chrome("/Users/kimuk/download/chromedriver/chromedriver")
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

copy_input('//*[@id="id"]', id)
time.sleep(1)
copy_input('//*[@id="pw"]', pw)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

print("before pay")
# Naver 페이 들어가기
time.sleep(4)
driver.get('https://order.pay.naver.com/home')
print("after pay")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('a.goods_thumb')

#내가 샀던 물품들 출력
print(notices)
print("--------")
for n in notices:
    print(n.text.strip())