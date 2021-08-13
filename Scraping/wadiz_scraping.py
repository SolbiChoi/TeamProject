import pandas as pd
from selenium import webdriver
import time
import numpy as np
import requests
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/category/294?keyword=&endYn=Y&order=support')

table = driver.find_element_by_class_name('ProjectCardList_container__3Y14k')
rows = table.find_element_by_class_name('ProjectCardList_item__1owJa')
time.sleep(1)

wadiz_review = []
for i in range(47,50): #데이터 범위 한페이지 48개
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight-500)") #스크롤
    table = driver.find_element_by_class_name('ProjectCardList_container__3Y14k')  # 표 전체
    rows = table.find_elements_by_class_name("ProjectCardList_item__1owJa")[i]
    rows.click()
    time.sleep(1)
    community = driver.find_element_by_css_selector('#container > div.reward-nav > ul > li:nth-child(5) > a') #커뮤니티 클릭
    community.click()
    try:
        reward = driver.find_element_by_xpath('//*[@id="rating-app"]/div[3]/div[1]/div[1]/div/span[1]') #리뷰
        while True:
            try:
                review_more = driver.find_element_by_css_selector('#rating-app > div.CommentListMoreButton_container__23PfA > button') #더보기
                review_more.click()
                time.sleep(0.7)
            except:
                break
        review = driver.find_elements_by_css_selector('#rating-app > div > div > div:nth-child(3) > div >div')
        for s in review:
            wadiz_review.append(s.text.strip())
        driver.back()
        driver.back()
    except NoSuchElementException: #별점 없을 경우 예외처리
        driver.back()
        driver.back()
    time.sleep(1)
df = pd.DataFrame({'review':wadiz_review})
print(df)

driver.close()
driver.quit()