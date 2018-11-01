#import BestBuyScrape
from BestBuyScrape import BestBuyScrape

#import AmazonScrape
from AmazonScrape import AmazonScrape

#import MemoryExpressScrape
from MemoryExpressScrape import MemoryExpressScrape

#import Google_Search
from Google_Search import Google_Search

#import ClipboardListener
from ClipboardListener import ClipboardListener
import time 

class WebScrape_main(object):

    clipboard = ClipboardListener()
    Searcher = Google_Search()
    searchItem = None
    NewEggEnabler = None

    def __init__(self):
        self.clipboard.getClipboard()
        if(self.clipboard.data != None):
            searchItem = self.clipboard.data
        self.NewEggEnabler = None

    def enableNewEgg(self):
        print("In order to search on newegg, many extra steps needs to be done.")
        print("Such as installing Google Chrome and ChromeDriver for selenium.")
        print("In addition, running newegg will greatly affect the proformance of this software, since a real brower will be opened.")
        enable = input("Would you like to enable search on newegg? Type Yes or No ")
        if(enable == "Yes"):
            self.NewEggEnabler = True

    def updateSearchItem(self):
         self.clipboard.getClipboard()
         if(self.clipboard.data != None and self.clipboard.data != self.searchItem):
             self.searchItem = self.clipboard.data
             print("********************************************************************************************************")
             print("The current search item is: ",self.searchItem)
             print("********************************************************************************************************")
             return True
         return False

    def searchingForAmazon(self):
         customSearchItem = self.searchItem + " amazon.ca"
         self.Searcher.search(customSearchItem)
         self.Searcher.playWithAmazon()

    def searchingForNewEgg(self):
        if(self.NewEggEnabler == True):
            customSearchItem = self.searchItem + " newegg.ca"
            self.Searcher.search(customSearchItem)
            self.Searcher.playWithNewEgg()

    def searchingForBestBuy(self):
         customSearchItem = self.searchItem + " bestbuy.ca"
         self.Searcher.search(customSearchItem)
         self.Searcher.playWithBestBuy()

    def searchingForMemoryExpress(self):
         customSearchItem = self.searchItem + "memoryexpress"
         self.Searcher.search(customSearchItem)
         self.Searcher.playWithMemoryExpress()

    def run (self):
        while(1):
            if(self.updateSearchItem()):
                self.searchingForAmazon()
                self.searchingForNewEgg()
                self.searchingForBestBuy()
                self.searchingForMemoryExpress()
            time.sleep(2)

main = WebScrape_main()
main.enableNewEgg()
main.run()

