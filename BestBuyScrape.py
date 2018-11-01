# import libraries
import urllib.request
from bs4 import BeautifulSoup


class BestBuyScrape:
    uml = ''
    soup = None
    price = None
    product_name = None

    def __init__(self,url):
        self.uml = url
        self.initHTMLParsed()
        self.initBestBuyPrice()
        self.initBestBuyName()

    def initBestBuyPrice (self):
        # get the index price
        price_box = self.soup.find('div', attrs={'class':'price-wrapper price-extra-large'})
        if(price_box == None):
            return self.price
        self.price = price_box.text
        self.price = " ".join(self.price .split())
        return self.price

    def initBestBuyName (self):
        product_name_box = self.soup.find('h1', attrs= {'class': 'product-title'})
        if(product_name_box == None):
            return self.product_name
        self.product_name = product_name_box.text.strip()
        return self.product_name

    def initHTMLParsed(self):
        try:
            request = urllib.request.Request(self.uml)
            response = urllib.request.urlopen(request)
        except Exception:
            print("something broke... umm.. in requesting the url.....")
        self.soup = BeautifulSoup(response, 'html.parser')

    def getBestBuyPrice(self):
        return self.price

    def getBestBuyName(self):
        return self.product_name

    def display(self):
        print("Price from bestbuy.ca!!")
        if(self.product_name == None or self.price == None):
            print("The item your searching is unavilible~~ RIP either your bad or my bad or the webiste's fault!!")
            return
        print ("The name of the product is: ", end = " ")
        print(self.product_name)
        print ("The price of the product is: ", end = " ")
        print(self.price)
        print("\n\n\n")

