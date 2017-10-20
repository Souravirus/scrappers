# -*- coding: utf-8 -*-
import scrapy


class CarlistSpider(scrapy.Spider):
	name = 'carlist'
	allowed_domains = ['www.carlist.my']
	start_urls = ['https://www.carlist.my/cars-for-sale/perodua/myvi/malaysia']

	def parse(self, response):
		cars = response.xpath('//article')

		for car in cars:
			title = car.xpath('.//@data-title').extract_first()
			year = car.xpath('.//@data-year').extract_first() 
			make = car.xpath('.//@data-make').extract_first()
			model = car.xpath('.//@data-model').extract_first()
			url = car.xpath('.//@data-url').extract_first()
			transmission = car.xpath('.//@data-transmission').extract_first()
			mileage = car.xpath('.//@data-mileage').extract_first()
			price = car.xpath('.//*[@class="listing__price  delta  weight--bold"]/text()').extract_first()

			yield {
				'Title': title,
				'Year': year,
				'Make': make,
				'Model': model,
				'URL': url,
				'Transmission': transmission,
				'Mileage': mileage,
				'Price': price
			}

		next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
		absolute_next_page_url = response.urljoin(next_page_url)
		print(absolute_next_page_url)
		yield scrapy.Request(absolute_next_page_url)
