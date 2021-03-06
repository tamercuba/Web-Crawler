#!/usr/bin/env python
import scrapy
import os
from app.spiders.spider_maquinas import VultrSpider, DigitalOceanSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Main():
    def __init__(self):
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(VultrSpider())
        process.crawl(DigitalOceanSpider())
        process.start()
        #converte o arquivo jsonl em arquivo json
        os.system("jq -s '.' static/maquinas.jsonl > static/maquinas.json")
if __name__ == '__main__':
    main = Main()
