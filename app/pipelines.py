import json
import csv
import six
import io
from scrapy.exporters import JsonItemExporter, CsvItemExporter

# variavel global para que o Pipeline só escreva os headers para o primeiro Spider
FIRST_SPIDER = True

class PrintItem:
    def process_item(self, item, spider):
        print(dict(item))
        return item

class JsonPipeline:
    def open_spider(self, spider):
        self.file       = open('static/maquinas.json', 'ab')
        # self.exporter   = CustomJsonExporter(self.file)
        self.exporter = JsonItemExporter(self.file, indent=True)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class CsvPipeline:
    def open_spider(self, spider):
        global FIRST_SPIDER
        self.file       = open('static/maquinas.csv', 'ab')
        self.exporter   = CsvItemExporter(self.file, include_headers_line=FIRST_SPIDER)
        self.exporter.fields_to_export = ['storage', 'cpu', 'memory', 'bandwidth', 'price']
        FIRST_SPIDER=False

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
