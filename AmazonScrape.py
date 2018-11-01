# import libraries
import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
from lxml import html
import requests
from lxml.html.soupparser import fromstring

class AmazonScrape:
    uml = ''
    soup = None
    price = ""
    product_name = None
    response = None
    tree = None

    def __init__(self,url):
        self.uml = url
        self.initHTMLParsed()
        self.initAmazonPrice()
        self.initAmazonName()

    def initAmazonPrice (self):
        self.price = self.tree.xpath('//span[contains(@id,"priceblock_ourprice") or contains(@id,"priceblock_dealprice")]/text()') 
        return self.price

    def initAmazonName (self):
        product_name_box = self.soup.find('h1', attrs={'class':'a-size-large a-spacing-none'})
        if(product_name_box == None):
            return self.product_name
        self.product_name = product_name_box.text.strip()
        return self.product_name

    def initHTMLParsed(self):
        response = urllib.request.urlopen(self.uml)
        htmlparser = etree.HTMLParser()
        self.tree = etree.parse(response, htmlparser)
        request = urllib.request.Request(self.uml)
        self.response = urllib.request.urlopen(request)
        self.soup = BeautifulSoup(self.response, 'html.parser')
       # print(self.soup)

    def getAmazonPrice(self):
        return self.price

    def getAmazonName(self):
        return self.product_name

    def display(self):
        print("Price from amazon.ca!!")
        if(self.product_name == None or self.price == None):
            print("The item your searching is unavilible~~ RIP either your bad or my bad or the webiste's fault!!")
            return
        print ("The name of the product is: ", end = " ")
        print(self.product_name)
        print ("The price of the product is: ", end = " ")
        print(self.price)
        print("\n\n\n")


