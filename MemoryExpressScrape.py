# import libraries
import urllib.request
from bs4 import BeautifulSoup


class MemoryExpressScrape:
    uml = ''
    soup = None
    price = None
    product_name = None

    def __init__(self,url):
        self.uml = url
        self.initHTMLParsed()
        self.initMemoryExpressPrice()
        self.initMemoryExpressName()

    def initMemoryExpressPrice (self):
        # get the index price
        price_box = self.soup.find('div', attrs={'class':'GrandTotal'})
        if(price_box == None):
            return self.price
        self.price = price_box.text
        self.price = " ".join(self.price .split())
        return self.price

    def initMemoryExpressName (self):
        product_name_box = self.soup.find('h1')
        if(product_name_box == None):
            return self.product_name
        self.product_name = product_name_box.text.strip()
        return self.product_name

    def initHTMLParsed(self):
        request = urllib.request.Request(self.uml)
        response = urllib.request.urlopen(request)
        self.soup = BeautifulSoup(response, 'html.parser')

    def getMemoryExpressPrice(self):
        return self.price

    def getMemoryExpressName(self):
        return self.product_name

    def display(self):
        print ("The name of the product is: ", end = " ")
        print(self.product_name)
        print ("The price of the product is: ", end = " ")
        print(self.price)


