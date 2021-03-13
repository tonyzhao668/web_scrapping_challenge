from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import datetime
from dateutil.parser import parse
import pandas as pd
# import requests
# import pymongo


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=True)

def scrape_info():
    browser = init_browser()

    mar_list = []

    # Visit the required 4 urls in turn, the first one

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the news' title and paragraph
    news = []
    n = {}
    threads = soup.find_all('li', class_='slide')

    for thread in threads:
        div = thread.find('div', class_= 'list_text')
        temp = {}
        try: 
            dt = div.find('div', class_= 'list_date').text
            d = parse(dt).strftime("%y-%m-%d")   #change US date into normal date
    
            if d >= '21-03-05':
                p = div.find('div', class_= 'article_teaser_body').text
                if div.a.text:
                    t = div.a.text
                    if t.split("-"):
                        i = t.split("-")
                        t = i[0]
                if (d and t and p):
                    temp.update({'date': d, 'title': t, 'paragraph': p})
                    news.append(temp)
                
        except AttributeError as e:
            print(e)

    n.update({'news' : news})       
    mar_list.append(n)
    #print("news ok /n")
    
    
    #read in the 2nd url and parsing into soup
    url2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url2)
    time.sleep(1)
    html2 = browser.html
    soup = bs(html2, "html.parser")

    # Get the featured image and its url
    images = []
    ii = {}
    di = soup.find('div', class_ = 'col-md-12 mt-5')
    locates = di.find_all('div', class_='col-md-4')

    for loc in locates:
        temp = {}
        try: 
            img = loc.img
            img_url = img['src'] 
            im = img_url.split(".")
            if (im[-1]) == "jpg":
                temp.update({"url": img_url})
                images.append(temp)
                #print(img_url)
            
        except AttributeError as e:
            print(e)

    ii.update({'imgs': images})
    mar_list.append(ii)
    
    #print('img ok /n')
    
    
    #read in the 3rd url and build table.html
    url3 = 'https://space-facts.com/mars/'

    # Get the Mars fact table 
    tt = {}
    tables = pd.read_html(url3)
    time.sleep(1)
    df = tables[0]
    df.columns = ['items', 'data']
    table = df.to_html(index = False)

    tt.update({'table' : table})
    mar_list.append(tt)
    
    #print('table ok /n')
    
    

    #read in the 4th url and parsing into soup
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    ul = {}
    urs = []

    browser.visit(url4)
    time.sleep(1)
    html4 = browser.html
    soup = bs(html4, "html.parser")

    # build mars hemisphere images' title list
    titles = []

    dv = soup.find('div', class_ = 'collapsible results')
    los = dv.find_all('div', class_='item')

    for lo in los:
        try: 
            h = lo.find('div', class_ = 'description')
            title = h.a.h3.text
            if (title.split(' ')[-1]) == 'Enhanced':
                titles.append(title)
        
        except AttributeError as e:
            print(e)

    #make a short title list (tiles without 'hemisphere and in low case')
    short_t = []
    for i in range(4):
        t = titles[i].split(' ')
        short_t.append((t[0] + '_' + t[-1]).lower())
        if i > 1:
            short_t[i] = ((t[0] + '_' + t[1] +'_'+ t[-1]).lower())
    
    #build dict for the images' titles and urls (urls) for sample images with smaller size, for easy loading
    
    u = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/'
    for j in range(4):
        temp = {}
        urlo = u + short_t[j]+'.'+'tif'
        urls = urlo + '/full.jpg'
        temp.update({'title':titles[j], 'href': urls})
        urs.append(temp)
    
    ul.update({'urls' : urs})
    mar_list.append(ul) 
          
    #print('url ok /n')
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mar_list



