#!/usr/bin/env python
import scrapy
from app.spiders.vultr import VultrSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

process.crawl(VultrSpider())

process.start()
