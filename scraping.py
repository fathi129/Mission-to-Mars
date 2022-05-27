#!/usr/bin/env python
# coding: utf-8

# In[57]:


from splinter import Browser
from bs4 import BeautifulSoup as soup 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path':ChromeDriverManager().install()}
browser = Browser('chrome',**executable_path,headless=False)


# In[13]:


url = 'https://redplanetscience.com' 
browser.visit(url)
browser.is_element_present_by_css('div.list_text',wait_time=1)


# In[14]:


html = browser.html


# In[15]:


html[0:500]


# In[16]:


news_soup = soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[24]:



# content = slide_elem.find('div',class_ = 'content_title')
# text = content.text
# print(text)

news_title = slide_elem.find('div',class_ = 'content_title').get_text()
news_title


# In[28]:


news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[50]:


url = 'https://spaceimages-mars.com/'
browser.visit(url)

# html[0:500]


# In[51]:



full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[52]:


html = browser.html
img_soup = soup(html,'html.parser')


# In[55]:


img_url_rel = img_soup.find('img',class_='fancybox-image').get('src')
img_url_rel
# url + img_url_rel


# In[56]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[66]:


df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df


# In[67]:


df.columns = ['Description','Mars','Earth']
df


# In[68]:


df.set_index('Description',inplace = True)
df


# In[69]:


df.to_html()


# In[70]:


browser.quit()


# In[ ]:




