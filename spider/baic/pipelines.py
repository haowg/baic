# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from baic.utils import SaveToDB

class BaicPipeline(object):
    def process_item(self, item, spider):
        baicorm = SaveToDB.BaicORM()
        print "insert into mysql....."
        baicorm.save(item)
        return item
