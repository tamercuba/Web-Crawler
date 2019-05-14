import scrapy
from ..items import ProductItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

class DigitalOceanSpider(scrapy.Spider):
	name = "digital_ocean"
	start_urls = ['https://www.digitalocean.com/pricing/']
	def parse(self, response):
		product = ProductItem()
		ALL_ROWS = response.xpath('//div[@id="standard-droplets-pricing-table"]').css('table.PricingTable').css('tbody').css('tr')
		for row in ALL_ROWS:
			product['storage']=row.css('td::text')[3].extract().strip()
			product['cpu'] = row.css('td::text')[2].extract().strip()
			product['memory'] = row.css('td')[0].css('strong::text').extract_first()
			product['bandwidth'] = row.css('td::text')[4].extract().strip()
			product['price'] = row.css('td')[4].css('strong::text').extract_first()
			yield product
#
# class DigitalOceanSpider(scrapy.Spider):
# 	name = "digital_ocean"
# 	start_urls = ['https://www.digitalocean.com/pricing/']
#
# 	def parse(self, response):
# 		product = ItemLoader( ProductItem(), response=response)
# 		product.default_input_processor = MapCompose(lambda v: v.split, replace_escape_chars)
# 		product.default_input_processor = Join()
# 		ALL_ROWS = response.xpath('//div[@id="standard-droplets-pricing-table"]').css('table.PricingTable').css('tbody').css('tr')
# 		for row in ALL_ROWS:
# 			items = []
# 			product.add_css('storage',row.css('td::text')[2])
# 			product.add_css('cpu', row.css('td::text')[1])
# 			product.add_css('memory',row.css('td')[0].css('strong::text'))
# 			product.add_css('bandwidth',row.css('td::text')[3])
# 			product.add_css('price',row.css('td')[4].css('strong::text'))
# 			items.append(product.load_item())
# 			yield items

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
