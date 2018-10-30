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

    def test (self):
        print('The main is now running!')

        print("Testing BestBuyScrape!")
        quote_page1 = 'https://www.bestbuy.ca/en-ca/product/marantz-sr7012-9-2-channel-4k-ultra-hd-pass-through-network-av-receiver/10885190.aspx?'
        object = BestBuyScrape(quote_page1)
        object.display()
        # specify the url
        quote_page2 = 'https://www.bestbuy.ca/en-ca/product/denon-avr-x6400h-11-1-channel-4k-ultra-hd-network-av-receiver/10885709.aspx?'
        object2 = BestBuyScrape(quote_page2)
        object2.display()

        print("Testing Google_Search!")
        searchItem = object2.getBestBuyName()
        object3 = Google_Search()
        object3.search(searchItem)
        object3.playWithBestBuy()

        searchItem = input('Enter the stuff you want you search that probably exist at BestBuy: ')
        object4 = Google_Search()
        object4.search(searchItem)
        object4.playWithBestBuy()

    def run (self):
        clipboard = ClipboardListener()
        object3 = Google_Search()
        data1 = None
        data2 = None
        while(1):
            clipboard.getClipboard()
            if(clipboard.data != None and clipboard.data != data1 and clipboard.data != "GG"):
                print("Start searching for the product!! \n\n")
                print("the product name searching now is: " + clipboard.data)
                object3.search(clipboard.data)
                object3.playWithBestBuy()
                object3.playWithAmazon()
                x = clipboard.data + " memoryexpress"
                object3.search(x)
                object3.playWithMemoryExpress()
                print("Now waiting for new input~~ \n\n")
                data1 = clipboard.data
            time.sleep(5)
WebScrape_main().run()

