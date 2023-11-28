from requests import get
from bs4 import BeautifulSoup
from extracts.wwr import extract_wwr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #브라우저 꺼짐 방지 코드
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) #크롬드라이버를 최신으로 유지해줍니다.

requestURL = "https://kr.indeed.com/jobs?q="
keyword = "react"

driver = webdriver.Chrome()
driver.get(f"{requestURL}{keyword}")

print(browser.page_source)

while (True):
    pass