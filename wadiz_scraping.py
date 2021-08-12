from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/main?keyword=&endYn=Y&order=support')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data_list = soup.select('div.ProjectCardList_list__1YBa2 > div > div > div > div')
for data in data_list:
    title = data.select('strong')[0].text.strip()
    category = data.select('span.RewardProjectCard_category__2muXk')[0].text.strip()
    score = data.select('span.RewardProjectCard_percent__3TW4_')[0].text.strip()
    print(title)
    for i in range(len(data_list)):
        time.sleep(0.5)
        page = driver.find_element_by_css_selector('div.RewardProjectCard_infoTop__3QR5w > a')
        page.click()
        time.sleep(0.5)
driver.close()
driver.quit()