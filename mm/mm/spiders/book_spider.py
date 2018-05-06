# -*- coding: utf-8 -*-
import scrapy
from ..items import ImageItem
class BookSpider(scrapy.Spider):
	# 每一个爬虫的唯一标识
	name="mm"

	# 定义爬虫的起始点，起始点可以是多个，这里只有一个
	start_urls=['http://www.mm131.com/qingchun/']
	item=ImageItem()
	item['image_urls']=[]
	def parse(self,response):
		link=response.css('div.main dl.list-left dd a::attr(href)').extract_first()
		
		yield{
			"link":link,
		}
		
