from requests import get
from bs4 import BeautifulSoup


def extract_wwr(keyword):
    baseURL = "https://weworkremotely.com"
    requestURL = f"{baseURL}/remote-jobs/search?term="
    response = get(f"{requestURL}{keyword}")
    
    if response.status_code == 200:
        result =[]
        soup = BeautifulSoup(response.text, "html.parser") # html parse
        jobs = soup.find_all('section', class_="jobs") # className="jobs"이면서 section 태그 추출
        
        for job_section in jobs:
            job_list = job_section.find_all('li') # section 태그 안에 li태그 추출
            job_list.pop() # 필요없는 맨 아래 li태그 삭제
            
            for job_item in job_list:
                anchors = job_item.find_all('a') # li 태그 안에 모든 a태그 추출
                anchor = anchors[1] # 두번째 a태그 들만 사용함
                link = anchor['href'] # link변수에 href값 저장
                
                company, worktime, region = anchor.find_all('span', class_='company') # 두번째 a태그 아래에 있는 span태그 추출
                position = anchor.find('span', class_='title') # 두번째 a태그 아래에 있는 span태그 추출
                
                data = {
                    'position': position.string.replace(","," "),
                    'company': company.string,
                    'worktime': worktime.string,
                    'region': region.string,
                    'link' : f"{baseURL}{link}"
                }
                result.append(data) # 추출한 데이터를 result변수에 저장
        return result   
    else:
        return "error"  

