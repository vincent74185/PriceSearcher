# import libraries
import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
from lxml import html
import html5lib
import requests
from lxml.html.soupparser import fromstring
#import selenium for requesting the html, why? beacuse newegg.ca is javascript heavy, some essential information is hidden by javascript
#therefore, use of browser is required
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class NewEggScrape:
    uml = ''
    soup = None
    price = ""
    product_name = None
    response = None

    def __init__(self,url):
        self.uml = url
        self.initHTMLParsed()
        self.initNewEggPrice()
        self.initNewEggName()

    def initNewEggPrice (self):
        # get the index price
        price_box = self.soup.find('ul', attrs={'class':'price has-label-membership price-product-cells price-main-product'})
        #price_box = self.soup.find('product_sale_price')
        if(price_box == None):
            return self.price
        self.price = price_box.text
        self.price = " ".join(self.price .split())
        return self.price

    def initNewEggName (self):
        product_name_box = self.soup.find('h1', attrs= {'id': 'grpDescrip_h'})
        if(product_name_box == None):
            return self.product_name
        self.product_name = product_name_box.text.strip()
        return self.product_name

    def initHTMLParsed(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe',chrome_options=options)
        #driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        driver.get(self.uml)
        html = driver.page_source
        self.soup = BeautifulSoup(html)


    def getNewEggPrice(self):
        return self.price

    def getNewEggName(self):
        return self.product_name

    def display(self):
        print("Price from newegg.ca!!")
        if(self.product_name == None or self.price == None):
            print("The item your searching is unavilible~~ RIP either your bad or my bad or the webiste's fault!!")
            return
        print ("The name of the product is: ", end = " ")
        print(self.product_name)
        print ("The price of the product is: ", end = " ")
        print(self.price)
        print("\n\n\n")



