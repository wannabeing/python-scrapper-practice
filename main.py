from extracts.indeed import extract_indeed
from extracts.wwr import extract_wwr
import datetime







keyword = input("언어를 말씀해주세요: ")

indeedJobs = extract_indeed(keyword)
wwrJobs = extract_wwr(keyword)

jobs = indeedJobs + wwrJobs

# 날짜계산
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")

file = open(f"{today}_{keyword}_recruitment.csv", "w")
file.write("Position,Company,Worktime,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['worktime']},{job['region']},{job['link']}\n")
file.close()
