# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from inmatescraper.items import Inmate, Charge
import json

HEADER_STRING = 'Date Charged'


class P2CSpider(scrapy.Spider):
    name = 'durham'
    allowed_domains = []
    start_urls = ['http://p2c.wakeso.net',
                  'https://p2c.guilfordcountysheriff.com',
                  'http://p2c.nhcgov.com',
                  'http://sheriff.co.union.nc.us',
                  'https://p2c.fcso.us',
                  'http://p2c.stanlycountync.gov',
                  'https://apps.alamance-nc.com/p2c',
                  'http://onlineservices.cabarruscounty.us/p2c',
                  'http://74.218.167.200/p2c',
                  'http://www.morgantonps.org/p2c',
                  'http://www.lincolnsheriff.org/p2c',
                  'https://bcsdp2c.buncombecounty.org',
                  'https://ossip2c.rowancountync.gov/p2c',
                  '']
    QUERY_URL_SUFFIX = '/jqHandler.ashx?op=s'
    REFFERER_URL_SUFFIX = '/jailinmates.aspx'
    P2C_DEFAULT_FORMDATA = {'t':'ii', '_search':'fasle', 'rows':'100000', 'page':'1', 'sidx':'disp_name', 'sord':'asc'}

    def get_formdata(self):
        return self.P2C_DEFAULT_FORMDATA

    def get_headers(self):
        return self.P2C_DEFAULT_HEADER

    def make_requests_from_url(self, url):
        post_url = url + self.QUERY_URL_SUFFIX
        post_headers = {'POST': self.QUERY_URL_SUFFIX + ' HTTP/1.1',
                        'Connection': 'keep-alive',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Origin': url,
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Referer': url + self.REFFERER_URL_SUFFIX,
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Cache-Control': 'no-cache'}
        return scrapy.FormRequest(dont_filter=True,
                                  formdata=self.P2C_DEFAULT_FORMADATA,
                                  headers = post_headers)

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        inmate = None
        inmates = []
        for inmate_data in jsonresponse['rows']:
            inmate_loader = ItemLoader(Inmate())
            inmate_loader.add_value(items.KEY_FIRST_NAME, inmate_data['firstname'])
            inmate_loader.add_value(items.KEY_MIDDLE_NAME, inmate_data['middlename'])
            inmate_loader.add_value(items.KEY_LAST_NAME, inmate_data['lastname'])
            inmate_loader.add_value(items.KEY_SEX, inmate_data['sex'])
            inmate_loader.add_value(items.KEY_DATE_OF_BIRTH, inmate_data['dob'])
            inmate_loader.add_value(items.KEY_RACE, inmate_data['race'])
            inmate = inmate_loader.load_item()
            inmate[items.KEY_CHARGES] = []
            charge_loader = ItemLoader(Charge())
            charge_loader.add_value(items.KEY_DATE_CONFINED, inmate_data['date_arr'])
            charge_loader.add_value(items.KEY_DESC, inmate_data['chrgdesc'])
            charge_loader.add_value(items.KEY_AGENCY, inmate_data['agency'])
            inmate[items.KEY_CHARGES].append(charge_loader.load_item())
            inmates.append(inmate)
        return inmates
