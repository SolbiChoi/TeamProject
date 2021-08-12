import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/category/287?keyword=&endYn=Y&order=support')

# 스크롤 15번 내림
num_scroll = 15
while num_scroll:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
    time.sleep(2)
    num_scroll -= 1
time.sleep(1)

# 데이터 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data_list = soup.select('div.ProjectCardList_list__1YBa2 > div > div > div > div')
time.sleep(1)
funding_list = []
for data in data_list:
    title = data.select('strong')[0].text.strip()
    category = data.select('span.RewardProjectCard_category__2muXk')[0].text.strip()
    score = data.select('span.RewardProjectCard_percent__3TW4_')[0].text.strip()
    funding_list.append([title, category, score])
    columns = ['title', 'category', 'score']
    result = pd.DataFrame(funding_list, columns=columns)
result.to_excel('./files/data.xlsx', index=False)
driver.close()
driver.quit()