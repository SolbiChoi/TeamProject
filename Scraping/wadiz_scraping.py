import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

driver = webdriver.Chrome('/chromedriver.exe')
driver.get('https://www.wadiz.kr/web/wreward/category/294?keyword=&endYn=Y&order=support')

# 스크롤 15번 내림
# num_scroll = 15
# while num_scroll:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
#     time.sleep(2)
#     num_scroll -= 1
# time.sleep(1)
# 데이터 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
time.sleep(1)
data_list = soup.select('div.ProjectCardList_list__1YBa2 > div')
funding_list = []
for data in data_list:
    # 클릭
    link = driver.find_element_by_css_selector('div.ProjectCardList_item__1owJa > div > div > a')
    link.click()
    community = driver.find_element_by_css_selector('#container > div.reward-nav > ul > li:nth-child(5) > a')
    community.click()
    driver.back()
    driver.back()



#     title = data.select('strong')[0].text.strip() #title
#     category = data.select('span.RewardProjectCard_category__2muXk')[0].text.strip() #category
#     score = data.select('span.RewardProjectCard_isAchieve__1LcUu')[0].text.strip() #성공여부
#     funding_list.append([title, category, score])
#     columns = ['title', 'category', 'score']
#     result = pd.DataFrame(funding_list, columns=columns)
#     # more = driver.find_element_by_css_selector('#rating-app > div.CommentListMoreButton_container__23PfA')
#     # more.click()
#     time.sleep(1)
#     try:
#         reward = data.select('span.RatingCommentAverageItem_score__dcVnr')[0].text.strip()
#         average = data.select('span.RatingCommentAverageItem_score__dcVnr')[1].text.strip()
#     except IndexError:
#         pass
#
#     # review = data.select('')
# print(title,category,score,reward,average)
#
# # result.to_excel('./files/culture_data.xlsx', index=False)
# driver.close()
# driver.quit()