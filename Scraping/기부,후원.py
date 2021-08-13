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
driver.get('https://www.wadiz.kr/web/wreward/category/312?keyword=&endYn=Y&order=support')


# In[4]:


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

browser = webdriver.Chrome('./chromedriver.exe')
data_list = soup.select('div.ProjectCardList_list__1YBa2 > div > div > div > div')
for data in data_list:
    title = data.select('strong')[0].text.strip()
    print(title)
len(title)


# In[ ]:




