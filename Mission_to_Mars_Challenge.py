#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import re


# In[3]:


# Path to chromedriver
#!which chromedriver


# In[4]:


# Set the executable path and initialize the chrome browser in splinter
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path)
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[33]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# full_image_elem = browser.find_by_css('div[class="item"]')
hemisphere_items = browser.find_by_tag('div[class="item"]')

hemisphere_items_tagged = []

for i in hemisphere_items:
    hi = {}
    html = i.html
    item_soup = soup(html, 'html.parser')
    title = item_soup.find("h3").get_text()
    thumb = item_soup.find("img", class_='thumb')['src']
    link = item_soup.find("a", class_='itemLink')['href']
    hi["title"]=title
    hi["thumb"]=thumb
    hi["link"]=link
    hemisphere_items_tagged.append(hi)

hemisphere_image_urls = []
for hi in hemisphere_items_tagged:
    browser.visit('https://astrogeology.usgs.gov'+hi['link'])
    download_panel = browser.find_by_tag('div[class="downloads"]')
    html = download_panel.html
    item_soup = soup(html, 'html.parser')
    full_img_url = item_soup.find(href=re.compile("full.jpg"))['href']
    hemisphere_image_urls.append(full_img_url)
    hi["full_img_url"]=full_img_url

#     full_img_url = item_soup.find("h3").get_text()
#     hemisphere_image_urls.append(full_img_url)


# In[34]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[24]:


# 5. Quit the browser
browser.quit()


# In[ ]:




