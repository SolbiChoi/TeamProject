import pandas as pd
from selenium import webdriver
import time
import numpy as np
import requests
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/category/289?keyword=&endYn=Y&order=support')

table = driver.find_element_by_class_name('ProjectCardList_container__3Y14k')
rows = table.find_element_by_class_name('ProjectCardList_item__1owJa')
time.sleep(1)

wadiz_star_grade = []
wadiz_review = []
for i in range(0,96): #데이터 범위 한페이지 48개
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight-500)") #스크롤
    table = driver.find_element_by_class_name('ProjectCardList_container__3Y14k')  # 표 전체
    rows = table.find_elements_by_class_name("ProjectCardList_item__1owJa")[i]
    rows.click()
    time.sleep(1)
    community = driver.find_element_by_css_selector('#container > div.reward-nav > ul > li:nth-child(5) > a') #커뮤니티 클릭
    community.click()
    try:
        while True:
            try:
                review_more = driver.find_element_by_css_selector('#rating-app > div.CommentListMoreButton_container__23PfA > button') #더보기 클릭
                review_more.click()
                time.sleep(0.7)
            except:
                break
        star = driver.find_elements_by_css_selector('div.RatingCommentContent_ratingWrapper__2KDnK > div > span:nth-child(3)') #별점
        review = driver.find_elements_by_css_selector('#rating-app > div > div > div:nth-child(3) > div >div') #리뷰
        for s in star:
            wadiz_star_grade.append(s.text.strip())
        for r in review:
            wadiz_review.append(r.text.strip())
        driver.back()
        driver.back()
    except NoSuchElementException: #리뷰 없을 경우 예외처리
        driver.back()
        driver.back()
    time.sleep(1)

df = pd.DataFrame({'star grade':wadiz_star_grade, 'review':wadiz_review})
df.to_excel('./files/food_scraping.xlsx', index=False)
# print(df)
driver.close()
driver.quit()