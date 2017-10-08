# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

"""
Get the most recent CNN News Headlines in your terminal
"""
def main():
    cnn_url = "http://www.cnn.com/specials/last-50-stories"
    page = urllib2.urlopen(cnn_url)
    headlines = []
    soup = BeautifulSoup(page, "html.parser")
    for news_item in soup.find_all('span', attrs={'class': 'cd__headline-text'}):
        headlines.append(news_item.text)
    for i, headline in enumerate(headlines):
        print "{}. {}".format(i+1, headline.encode('utf-8'))

if __name__ == '__main__':
    main()
