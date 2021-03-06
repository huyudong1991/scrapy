# -*- coding: utf-8 -*-
import scrapy
from ..items import ImageItem
class BookSpider(scrapy.Spider):
	name="mm"

	start_urls=['http://www.mm131.com/xinggan/']
	item=ImageItem()
	def parse(self,response):
		links=response.css('div.main dl.list-left dd a::attr(href)').extract()

		for link in links:
			if len(link)>=25:
				self.item['image_urls']=[]
				yield scrapy.Request(link,callback=self.getpic)
			
		pagenow=response.css('div.main dl.list-left dd.page span').extract()
		if len(pagenow)==1:
			next_url=response.css('div.main dl.list-left dd.page a.page-en::attr(href)').extract()[-2]
			if next_url:
				next_url=response.urljoin(next_url)
				yield scrapy.Request(next_url,callback=self.parse)
		
	def getpic(self,response):
		link=response.css('div.content-pic a img::attr(src)').extract_first()


		self.item['image_urls'].append(link)
		
		next_url=response.css('div.content-page a.page-ch::attr(href)').extract()[-1]
		if next_url:
			next_url=response.urljoin(next_url)
			yield scrapy.Request(next_url,callback=self.getpic)
		yield self.item

		
		