# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ImageItem

class BookSpider(scrapy.Spider):
	name="nude"
	item=ImageItem()

	start_urls=['http://nudejapangirls.com/']

	def parse(self,response):
		linkclasses=response.css('div.grid-item div.dev-thumb a::attr(href)').extract()
		for linkclass in linkclasses:
			linkclass=response.urljoin(linkclass)
			yield scrapy.Request(linkclass,callback=self.getname)
	
	def getname(self,response):
		namelinks=response.css('div.grid-item div.dev-thumb a::attr(href)').extract()
		for namelink in namelinks:
			
			namelink=re.search('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]',namelink).group(0)
			self.item['image_urls']=[]
			yield scrapy.Request(namelink,callback=self.getpic)

		next_url=response.css('ul.dev-next-prev a::attr(href)').extract_first()
		if next_url:
			next_url=response.urljoin(next_url)
			yield scrapy.Request(next_url,callback=self.getname)
	
	def getpic(self,response):
		links=response.css('div.grid-item div.dev-thumb a::attr(href)').extract()
		for link in links:
			link=response.urljoin(link)
			self.item['image_urls'].append(link)		
		yield self.item

