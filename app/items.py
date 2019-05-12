import scrapy

class ProductItem(scrapy.Item):
	storage 	= scrapy.Field()
	cpu 		= scrapy.Field()
	memory		= scrapy.Field()
	bandwidth 	= scrapy.Field()
	price 		= scrapy.Field()
