import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/category/294?keyword=&endYn=Y&order=support')

def scraping_page():
    # 스크롤 15번 내림
    num_scroll = 2
    while num_scroll:
        # 데이터 가져오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(1)
        data_list = soup.select('div.ProjectCardList_list__1YBa2 > div') #리스트
        count = 0
        funding_list = []
        for data in data_list:
            title = data.select('strong')[0].text.strip() #title
            score = data.select('span.RewardProjectCard_isAchieve__1LcUu')[0].text.strip() #성공여부
            count = count+1
            click_page = driver.find_element_by_class_name('ProjectCardList_item__1owJa') #리스트 클릭
            click_page.click()
            # click_community = driver.find_element_by_css_selector('div.reward-nav > ul > li:nth-child(5) > a') #커뮤니티 클릭
            # click_community.click()
            # driver.back()
            driver.back()
            time.sleep(0.5)

            funding_list.append([title, score])
            columns = ['title', 'score']
            result = pd.DataFrame(funding_list, columns=columns)
            print(title,score,count)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
        time.sleep(2)
        num_scroll -= 1

scraping_page()
# # result.to_excel('./files/culture_data.xlsx', index=False)
driver.close()
driver.quit()