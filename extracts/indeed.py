from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) #브라우저 꺼짐 방지 코드
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) #크롬드라이버를 최신으로 유지해줍니다.

    baseURL = "https://kr.indeed.com"
    requestURL = f"{baseURL}/jobs?q="

    browser = webdriver.Chrome()
    browser.get(f"{requestURL}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser") # html 추출
    pagenation = soup.find("nav", class_="css-98e656 eu4oa1w0")
    
    if pagenation==None:
        return 1 # 1페이지밖에 없으므로 1을 return
    else :
        pages = pagenation.select("ul li", recursive=False)
        count = len(pages)
        
        if count >= 5:
            return 5
        else:
            return count

def extract_indeed(keyword):
    
    pages = get_page_count(keyword) # 추출할 페이지 개수
    result =[]
    
    for page in range(pages):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True) #브라우저 꺼짐 방지 코드
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) #크롬드라이버를 최신으로 유지해줍니다.

        baseURL = "https://kr.indeed.com"
        requestURL = f"{baseURL}/jobs?q="

        browser = webdriver.Chrome()
        browser.get(f"{requestURL}{keyword}&start={page * 10}")
        
        soup = BeautifulSoup(browser.page_source, "html.parser") # html 추출
        job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0") # 특정 클래스 ul태그 추출
        jobs = job_list.find_all('li',recursive=False) # ul태그 바로 아래에 있는 모든 li태그 추출

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone") # 각각의 li태그 아래 div태그 추출
            
            if zone == None: # mosaic-zone 클래스가 없는 li태그만 사용 (직업정보가 있는 li태그)
                anchor = job.select_one("h2 a") # h2태그 아래에 a태그 가져오기
                link = anchor['href']
                position = anchor.select_one("span")['title']
                company = job.find("span", class_="css-1x7z1ps eu4oa1w0")
                region = job.find("div", class_="css-t4u72d eu4oa1w0")
                
                data = {
                    'position': position.replace("," ," "),
                    'company': company.string.replace(",", " "),
                    'worktime': "Full-Time",
                    'region': region.string,
                    'link' : f"{baseURL}{link}"
                }
                result.append(data)
    return result

