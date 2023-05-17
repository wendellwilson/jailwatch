# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapers.items import Inmate, Charge
from scrapers import items

HEADER_STRING = "Date Charged"


class DurhamSpider(scrapy.Spider):
    name = 'durham'
    allowed_domains = ['durhamcountync.gov']
    start_urls = ['http://p2c.wakeso.net/jailinmates.aspx']

    def parse(self, response):
        inmates = []
        inmate = None
        for inmate_data in response.css('tr'):
            if inmate_data.css('a'):
               if inmate:
                   inmates.append(inmate)
               inmate_loader = ItemLoader(Inmate())
               inmate_loader.add_value(items.KEY_NAME, inmate_data.css('a::text').extract())
               inmate = inmate_loader.load_item()
               inmate[items.KEY_CHARGES] = []
            else:
                charge_loader = ItemLoader(Charge())
                charge_data = inmate_data.css('td::text').extract()
                if charge_data and HEADER_STRING not in charge_data and len(charge_data) == 8:
                    charge_loader.add_value(items.KEY_DATE_CONFINED, charge_data[0])
                    charge_loader.add_value(items.KEY_DATE_CHARGED, charge_data[1])
                    charge_loader.add_value(items.KEY_DATE_RELEASED, charge_data[2])
                    charge_loader.add_value(items.KEY_STATUTE, charge_data[3])
                    charge_loader.add_value(items.KEY_BOND_TYPE, charge_data[4])
                    charge_loader.add_value(items.KEY_BOND_AMOUNT, charge_data[5])
                    charge_loader.add_value(items.KEY_COURT_DOCKET, charge_data[6])
                    charge_loader.add_value(items.KEY_DAYS_CHARGE, charge_data[7])
                    inmate[items.KEY_CHARGES].append(charge_loader.load_item())
        return inmates
