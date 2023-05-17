import scrapy
from scrapy.loader import ItemLoader
from scrapers import items
import json


class P2CSpider(scrapy.Spider):
    name = 'P2C'
    QUERY_URL_SUFFIX = '/jqHandler.ashx?op=s'
    DEFAULT_FORMDATA = {'t': 'ii', '_search': 'false', 'rows': '100000', 'page': '1', 'sidx': 'disp_name',
                        'sord': 'asc'}

    DEFAULT_INMATE_MAP = {items.KEY_FIRST_NAME: 'firstname',
                          items.KEY_MIDDLE_NAME: 'middlename',
                          items.KEY_LAST_NAME: 'lastname',
                          items.KEY_GENDER: 'sex',
                          items.KEY_DATE_OF_BIRTH: 'dob',
                          items.KEY_RACE: 'race',
                          items.KEY_BOOK_ID: 'book_id',}

    DEFAULT_CHARGE_MAP = {items.KEY_DATE_CONFINED: 'date_arr',
                          items.KEY_DESC: 'disp_charge',
                          items.KEY_AGENCY: 'disp_agency',}
    inmate_map = {}
    charge_map = {}
    inmate_data = {}

    def __init__(self, start_urls, inmate_map={}, charge_map={}, inmate_data={}, **kwargs):
        self.start_urls = start_urls
        self.inmate_data = inmate_data
        self.inmate_map = {**self.DEFAULT_INMATE_MAP, **inmate_map}
        self.charge_map = {**self.DEFAULT_CHARGE_MAP, **charge_map}
        super().__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            post_url = url + self.QUERY_URL_SUFFIX
            ##TODO figure out required headers
            yield scrapy.FormRequest(dont_filter=True,
                                     formdata=self.DEFAULT_FORMDATA,
                                     url=post_url,)

    def parse(self, response):
        json_response = json.loads(response.text)
        inmates = []
        for inmate_data in json_response['rows']:
            inmate_loader = ItemLoader(items.Inmate())

            for key, value in self.inmate_map.items():
                inmate_loader.add_value(key, inmate_data[value])

            for key, value in self.inmate_data.items():
                inmate_loader.add_value(key, value)

            inmate = inmate_loader.load_item()
            inmate[items.KEY_CHARGES] = []
            charge_loader = ItemLoader(items.Charge())

            for key, value in self.charge_map.items():
                charge_loader.add_value(key, inmate_data[value])

            inmate[items.KEY_CHARGES].append(charge_loader.load_item())
            inmates.append(inmate)
        return inmates
