#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


def scrape_info():
    mars_data = {}


    # In[3]:


    url = 'https://redplanetscience.com/'
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[4]:


     browser.visit(url)


    # In[5]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)


    # In[6]:


    article_title = soup.find('div', class_='content_title')
    article_title = article_title.text
    print(article_title)


    # In[7]:


    article_tease = soup.find('div', class_='article_teaser_body')
    article_tease = article_tease.text
    print(article_tease)


    # In[8]:


    url = "https://spaceimages-mars.com"
    browser.visit(url)


    # In[16]:


    browser.find_by_value(' FULL IMAGE').click()


    # In[17]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup


    # In[19]:


    feat_img_src = soup.find('img', class_='fancybox-image')
    feat_img_src = feat_img_src.get('src')
    feat_img_src = url + '/' + feat_img_src
    feat_img_src


    # In[ ]:


    featured_image_url = url + "/" + feat_img_src
    featured_image_url


    # In[ ]:


    url = "https://galaxyfacts-mars.com"
    browser.visit(url)


    # In[ ]:


    tables = pd.read_html(url)
    mars_table_df = tables[1]
    mars_table_df


    # In[ ]:


    mars_table_df.to_html("mars_table.html")


    # ### I tried to run through the list but I was having difficulty iterating correctly

    # In[ ]:


    # url = "https://marshemispheres.com/"
    # browser.visit(url)


    # In[ ]:


    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')


    # In[ ]:


    # thumblinks = soup.find_all('img', class_='thumb')

    # hirez_title=[]
    # hirez_url=[]

    # for link in thumblinks:
    #     url = link['src']
    #     browser.find_by_value(url).click
    # #     browser.visit(url)
    #     html = browser.html
    #     soup = BeautifulSoup(html, 'html.parser')
    #     working_url = soup.find('a', target='_blank').get('href')
    #     hirez_url.append(working_url)
        


    # In[27]:


    mars_data["article_title"] = article_title
    mars_data["article_tease"] = article_tease
    mars_data["featured_image_url"] = feat_img_src
    mars_data["mars_facts"] = mars_table_df


    # In[28]:


    return mars_data


# In[ ]:




