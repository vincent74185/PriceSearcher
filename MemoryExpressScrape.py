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
        Checker = self.initHTMLParsed()
        if(Checker == False):
            self.price = None
            self.product_name = None
            return
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
        try:
            request = urllib.request.Request(self.uml)
            response = urllib.request.urlopen(request)
            self.soup = BeautifulSoup(response, 'html.parser')
        except Exception:
            print("something broke... umm.. in requesting the url.....")
            return False

    def getMemoryExpressPrice(self):
        return self.price

    def getMemoryExpressName(self):
        return self.product_name

    def display(self):
        print("Price from memoryexpress.com!!")
        if(self.product_name == None or self.price == None):
            print("The item your searching is unavilible~~ RIP either your bad or my bad or the webiste's fault!!")
            return
        print ("The name of the product is: ", end = " ")
        print(self.product_name)
        print ("The price of the product is: ", end = " ")
        print(self.price)
        print("\n\n\n")


