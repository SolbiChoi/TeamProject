#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


browser = webdriver.Chrome('./chromedriver.exe')
driver = webdriver.Chrome()


# In[3]:


browser.get('https://www.wadiz.kr/web/wreward/category/311?keyword=&endYn=Y&order=support')


# In[5]:


import time
time.sleep(5)
browser.find_element_by_css_selector('ul > div > a.href').click()

time.sleep(5)
browser.find_element_by_css_selector('ul > li > span.count-total.comment-total').click()


#list = driver.find_elements_by_css_selector(' div[class^=RewardProjectListApp]> li')
#for data in list:
    #data.find_element_by_css_selector('commonCard_container >a').click()


# In[ ]:


from bs4 import BeautifulSoup


# In[ ]:


soup = BeautifulSoup(browser.page_source, 'html.parser')


# In[ ]:




