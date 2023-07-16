# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import requests

class WorkerAPIPipeline:

    def __init__(self, api_url):
        self.api_url = api_url
    
    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            api_url=crawler.settings.get('API_URL'),
        )

    def open_spider(self, spider):
        ## initializing spider
        ## build 
        pass

    def close_spider(self, spider):
        ## clean up when spider is closed
        pass

    def process_item(self, item, spider):
        ## how to handle each item
        
        #TODO: map gender and race fields to enum values
        #TODO: standardize date format
        #TODO: clean up text fields to help with dedup

        self.write_inmate(dict(item))
        #TODO: centralized logging to keep track of all scraped data in case we
        # have data pipeline issues
        return item
    
    def write_inmate(self, inmate):
        requests.put(f'{self.api_url}/inmate', inmate)