# -*- coding: utf-8 -*-
import json
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class VirmpSpider2017Pipeline(object):
    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # Process number of positions
        if item['number_of_positions']:
            positions = re.search('(\d+)\s+Position', item['number_of_positions'])
            item['number_of_positions'] = positions.group(1)
            print('Number of positions: ' + item['number_of_positions'])
        
        if item['program_categories']:
            categories = re.search('', item['program_categories'])

        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item