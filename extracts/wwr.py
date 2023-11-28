from requests import get
from bs4 import BeautifulSoup


def extract_wwr(keyword):
    baseURL = "https://weworkremotely.com"
    requestURL = f"{baseURL}/remote-jobs/search?term="
    response = get(f"{requestURL}{keyword}")
    
    if response.status_code == 200:
        result =[]
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        
        for job_section in jobs:
            job_list = job_section.find_all('li')
            job_list.pop() # 필요없는 맨 아래 태그 삭제
            
            for job_item in job_list:
                anchors = job_item.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                
                company, worktime, region = anchor.find_all('span', class_='company')
                position = anchor.find('span', class_='title')
                
                data = {
                    'position': position.string,
                    'company': company.string,
                    'worktime': worktime.string,
                    'region': region.string,
                    'link' : f"{baseURL}{link}"
                }
                result.append(data) 
        return result   
    else:
        return "error"  

