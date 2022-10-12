# 크롤링 작업 위한 라이브러리 임포트

import time
import requests
from bs4 import BeautifulSoup

#=====================================================================
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")

# =================================================================
# from selenium import webdriver    
# import chromedriver_autoinstaller
# from selenium.webdriver.chrome.service import Service
# chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(service=Service())


# =====================================================================
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")


# =========================================================================
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")
print(driver.title)




# driver라는 변수를 이용해 물리 브라우저를 제어합니다.
# driver = webdriver.Chrome('./chromedriver')

# 2022년도 이후 selenium 업데이트로 인한 xpath 추적시 임포트
from selenium.webdriver.common.by import By


# 딜레이 1초
# time.sleep(지연시간(초)) 입력시 해당시간만큼 코드 시연이 지연됨
time.sleep(1)

# .get(접속주소)를 입력하면 브라우저가 해당 주소로 접속
driver.get('https://naver.com')
print(driver.title)

time.sleep(2)

# 네이버 로그인버튼의 xpath를 따온 다음 클릭하게 하기
driver.find_element(By.XPATH, '//*[@id="account"]/a').click()

# 로그인창 xpath 지정
# 키 입력은 send_keys('전송문자열')을 입력
driver.find_element(By.XPATH, '//*[@id="id"]').send_keys('aaaa')

time.sleep(2)

# 비밀번호 입력
driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys('비밀번호\n') # \n = 엔터
time.sleep(2)

# 로그인 버튼 누르기
# driver.find_element(By.XPATH, '//*[@id="log.login"]/span').click()

# 로그인 되었을 때 카페로 접속
driver.get('https://cafe.naver.com/gugucoding')
print(driver.title)
time.sleep(3)

# 글쓰기 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="cafe-info-data"]/div[3]/a').click()


# 브라우저를 다 쓰면 닫아야 메모리가 절약된다.
driver.close()