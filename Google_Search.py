#import BestBuyScrape
from BestBuyScrape import BestBuyScrape
from googlesearch import search 
#import AmazonScrape
from AmazonScrape import AmazonScrape
#import NewEggScrape
from NewEggScrape import NewEggScrape
#import MemoryExpressScrape
from MemoryExpressScrape import MemoryExpressScrape

class Google_Search(object):

    searchResult = None

    def __init__(self):
        self.initGoogle_Search()

    def initGoogle_Search(self):
        return 

    def search(self, searchItem):
        # to search 
        self.searchResult = []
        i = 0
        for j in search(searchItem, tld="co.in", num=10, stop=1, pause=2): 
            self.searchResult.append(j)
            i = i + 1
        return self.searchResult
    
    def getSearchResult(self):
        return self.searchResult

    def playWithBestBuy(self):
        for i in range(len(self.searchResult)):
            if("bestbuy.ca" in self.searchResult[i]):
                print(self.searchResult[i])
                object = BestBuyScrape(self.searchResult[i])
                object.display()
                break

    def playWithAmazon(self):
        for i in range(len(self.searchResult)):
            if("amazon.ca" in self.searchResult[i]):
                print(self.searchResult[i])
                object = AmazonScrape(self.searchResult[i])
                object.display()
                break

    def playWithMemoryExpress(self):
        for i in range(len(self.searchResult)):
            if("memoryexpress.com" in self.searchResult[i]):
                print(self.searchResult[i])
                object = MemoryExpressScrape(self.searchResult[i])
                object.display()
                break

    def playWithNewEgg(self):
        for i in range(len(self.searchResult)):
            if("newegg.ca" in self.searchResult[i]):
                print(self.searchResult[i])
                object = NewEggScrape(self.searchResult[i])
                object.display()
                break
