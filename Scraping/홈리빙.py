#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests


# In[2]:


get_ipython().system('dir .\\chromedriver.exe')


# In[3]:


driver = webdriver.Chrome()
driver.get('https://www.wadiz.kr/web/wreward/category/310?keyword=&endYn=Y&order=support')


# In[4]:


num_scroll = 15
while num_scroll:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
    time.sleep(2)
    num_scroll -= 1
time.sleep(1)


# In[5]:


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

browser = webdriver.Chrome('./chromedriver.exe')
data_list = soup.select('div.ProjectCardList_list__1YBa2 > div > div > div > div')
for data in data_list:
    title = data.select('strong')[0].text.strip()
    print(title)


# In[ ]:




