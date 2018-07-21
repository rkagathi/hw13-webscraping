
# coding: utf-8

# <h1> Mission to Mars </h1>
# 
# ### NASA Mars News

# In[1]:


# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time


def initialize():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


# In[3]:

def scrape():
    # URL of page to be scraped
    # visiting the page
    mars_data = {}
    browser = initialize()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(2)

    # In[4]:


    #using bs to write it into html
    html = browser.html
    soup = bs(html,"html.parser")


    # In[5]:


    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text


    # In[6]:


    # latest_news_title = news_titles[0]
    # latest_news_title
    mars_data['news_title'] =   str(news_title).replace('\'', '')


    # In[7]:


    # Latest_news_paragraph = news_paragraphs[0]
    # Latest_news_paragraph
    mars_data['news_paragraph'] = str(news_paragraph).replace('\'','')


    # ### JPL Mars Space Images - Featured Image

    # In[8]:


    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
    browser.visit(url_image)
    time.sleep(2)


    # In[9]:

    #Getting the base url
    from urllib.parse import urlsplit
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
    print(base_url)


    # In[10]:


    #Design an xpath selector to grab the image
    xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"


    # In[11]:


    #Use splinter to click on the mars featured image
    #to bring the full resolution image
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()
    time.sleep(2)

    # In[12]:


    #get image url using BeautifulSoup
    html_image = browser.html
    soup = bs(html_image, "html.parser")
    time.sleep(2)
    img_url = soup.find("img", class_="fancybox-image")["src"]
    full_img_url = base_url + img_url
    mars_data['featured_image'] = full_img_url
    # print(full_img_url)


    # ### Mars Weather

    # In[13]:


    #get mars weather's latest tweet from the website
    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)
    time.sleep(2)

    # In[14]:


    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    # print(mars_weather)
    mars_data["mars_weather"] = mars_weather


    # ### Mars Facts

    # In[15]:


    # get mars facts website
    url_facts = "https://space-facts.com/mars/"


    # In[16]:


    table = pd.read_html(url_facts)
    table[0]


    # In[17]:


    df_mars_facts = table[0]
    df_mars_facts.columns = ["Parameter", "Values"]
    df_mars_facts.set_index(["Parameter"])


    # In[18]:


    mars_html_table = df_mars_facts.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    mars_html_table

    mars_data["mars_facts_table"] = mars_html_table


    # ### Mars Hemispheres

    # In[19]:


    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemisphere)
    time.sleep(2)

    # In[20]:


    #Getting the base url
    hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_hemisphere))
    print(hemisphere_base_url)


    # In[21]:


    hemisphere_img_urls = []
    results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)
    cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemisphere_base_url + cerberus_url
    print(cerberus_img_url)
    cerberus_title = soup.find("h2",class_="title").text
    print(cerberus_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    time.sleep(2)
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)


    # In[22]:


    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)
    schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, "html.parser")
    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
    print(schiaparelli_img_url)
    schiaparelli_title = soup.find("h2",class_="title").text
    print(schiaparelli_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    time.sleep(2)
    schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    hemisphere_img_urls.append(schiaparelli)


    # In[23]:


    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)
    syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    syrtis_major_image = browser.html
    soup = bs(syrtis_major_image, "html.parser")
    syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
    print(syrtis_major_img_url)
    syrtis_major_title = soup.find("h2",class_="title").text
    print(syrtis_major_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    time.sleep(2)
    syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
    hemisphere_img_urls.append(syrtis_major)


    # In[24]:


    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    print(valles_marineris_img_url)
    valles_marineris_title = soup.find("h2",class_="title").text
    print(valles_marineris_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    time.sleep(2)
    valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    hemisphere_img_urls.append(valles_marineris)


    # In[25]:


    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    print(valles_marineris_img_url)
    valles_marineris_title = soup.find("h2",class_="title").text
    print(valles_marineris_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    time.sleep(2)
    valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    hemisphere_img_urls.append(valles_marineris)

    mars_data["hemisphere_img_url"] = hemisphere_img_urls
    # In[ ]:
    browser.quit()

    return mars_data








