import json
import csv
import six
import io
from scrapy.exporters import JsonItemExporter, CsvItemExporter

class CustomJsonExporter(JsonItemExporter):
    def _beautify_newline(self):
        self.file.write(b'\n')

class PrintItem:
    def process_item(self, item, spider):
        print(dict(item))
        return item

class JsonPipeline:
    def open_spider(self, spider):
        self.file       = open('static/maquinas.json', 'ab')
        self.exporter   = CustomJsonExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class CsvPipeline:
    def open_spider(self, spider):
        self.file       = open('static/maquinas.csv', 'ab')
        if spider.name == 'digital_ocean':
            header = False
        else:
            header = True
        self.exporter   = CsvItemExporter(self.file, include_headers_line=header)
        self.exporter.fields_to_export = ['storage', 'cpu', 'memory', 'bandwidth', 'price']

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
