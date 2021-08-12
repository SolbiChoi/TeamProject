from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/main?keyword=&endYn=Y&order=support')

num_scroll = 15
while num_scroll:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
    time.sleep(2)
    num_scroll -= 1
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data_list = soup.select('div.ProjectCardList_list__1YBa2 > div > div > div > div')
time.sleep(1)
for data in data_list:
    title = data.select('strong')[0].text.strip()
    category = data.select('span.RewardProjectCard_category__2muXk')[0].text.strip()
    score = data.select('span.RewardProjectCard_percent__3TW4_')[0].text.strip()
    print(title, category, score)
driver.close()
driver.quit()