# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TengxunPrintPipeline(object):
    def process_item(self, item, spider):
        print("=================")
        print(item["zhName"])
        print(item["zhLink"])
        print(item["zhType"])
        print(item["zhNum"])
        print(item["zhAddress"])
        print(item["zhTime"])
        print("=================")
        

class TengxunMongoPipeline(object):
    def process_item(self,item,spider):
        return item

class TengxunMysqlPipeline(object):
    def process_item(self,item,spider):
        return item
