# About
A scraping tools build with scrapy that scrape [carlist.com.my](http://carlist.com.my/)

# Dependencies
- Scrapy
- Python3
- Tested on Mac

# To start
- find the start url (format: `https://www.carlist.my/cars-for-sale/perodua/myvi/malaysia`)
- replace the url in `scrapper/spiders/carlist.py` in the `start_urls`
- start scrapping! `scrapy run carlist`

# Result
[myvi.csv](./myvi.csv)



