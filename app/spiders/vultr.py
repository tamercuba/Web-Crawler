import scrapy
from ..items import ProductItem


class VultrSpider(scrapy.Spider):
	name 		= "vultr_spider"
	start_urls 	= ['https://www.vultr.com/pricing/']

	def parse(self, response):
		product = ProductItem()
		ALL_ROWS = response.css('div.pt__row').css('div.pt__row-content')
		for row in ALL_ROWS:
			if row.css('div.pt__col--storage').css('b::text').extract_first() is None:
				product['storage'] 	= row.css('div.pt__col--storage').css('b').css('span::text').extract_first()
			else:
				product['storage'] 	= row.css('div.pt__col--storage').css('b::text').extract_first()
			product['cpu'] 			= row.css('div.pt__col--cpu').css('b::text').extract_first()
			product['memory']  		= row.css('div.pt__col--memory').css('b::text').extract_first()
			product['bandwidth']  	= row.css('div.pt__col--bandwidth').css('b::text').extract_first()
			product['price']		= row.css('div.pt__col--price').css('b::text').extract_first()

			yield product
