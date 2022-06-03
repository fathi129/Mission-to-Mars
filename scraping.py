
from splinter import Browser
from bs4 import BeautifulSoup as soup 
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import time
import pandas as pd
def scrape_all():
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path,headless=False)
    news_title, news_paragraph = mars_news(browser)
    # hemisphere_image_urls = mars_hemisphere(browser),
    data = {
        "news_title":news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemisphere(browser),
        "last_modified": dt.datetime.now()
    }
    browser.quit()
    return data

def mars_news(browser):
    url = 'https://redplanetscience.com' 
    browser.visit(url)
    browser.is_element_present_by_css('div.list_text',wait_time=1)
    html = browser.html
    news_soup = soup(html,'html.parser')
    try:
        slide_elem = news_soup.select_one('div.list_text')
        news_title = slide_elem.find('div',class_ = 'content_title').get_text()
        news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
    except AttributeError:
        return None,None   
    return news_title,news_p
# ### Featured Images
def featured_image(browser):
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
    html = browser.html
    img_soup = soup(html,'html.parser')
    try:
        img_url_rel = img_soup.find('img',class_='fancybox-image').get('src')
        img_url_rel
        # url + img_url_rel
    except AttributeError:
        return None  
    img_url = f'https://spaceimages-mars.com/{img_url_rel}' 
    return img_url
    
def mars_facts():
    try:    
        df = pd.read_html('https://galaxyfacts-mars.com/')[0]
    except BaseException:
        return None    
    df.columns = ['Description','Mars','Earth']
    df.set_index('Description',inplace = True)
    return df.to_html()

def mars_hemisphere(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(1)
    #Soupify the main page
    html = browser.html
    soupify = soup(html,'html.parser')
    items = soupify.find("div",{"class":"results"}).find_all("div",{"class":"item"})
    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []
    for item in items:
        link = item.find("a",{"class":"itemLink"})["href"]
        full_url = url+link
        browser.visit(full_url)
        time.sleep(1)
        html = browser.html
        soupify = soup(html,'html.parser')
        # 3. Write code to retrieve the image urls and titles for each hemisphere.
        img = soupify.find("img",{"class":"wide-image"})["src"]
        img_url_mars = url+img
        title = soupify.find("h2",{"class":"title"}).text.split("Enhanced")[0].strip()
        datanew = {"img_url":img_url_mars,"title":title}
        hemisphere_image_urls.append(datanew)
        return hemisphere_image_urls


       


if __name__ == "__main__":
    print(scrape_all())    



   
