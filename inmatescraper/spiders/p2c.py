import scrapy
from scrapy.loader import ItemLoader
from inmatescraper import items
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

    def __init__(self, start_urls, inmate_map=DEFAULT_INMATE_MAP, charge_map=DEFAULT_CHARGE_MAP, **kwargs):
        self.start_urls = start_urls
        self.inmate_map = inmate_map
        self.charge_map = charge_map
        ##TODO take input state and county
        super().__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            post_url = url + self.QUERY_URL_SUFFIX
            ##TODO figure out required headers
            yield scrapy.FormRequest(dont_filter=True,
                                     formdata=self.P2C_DEFAULT_FORMDATA,
                                     url=post_url,)

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        inmates = []
        for inmate_data in jsonresponse['rows']:
            inmate_loader = ItemLoader(items.Inmate())

            for key, value in self.inmate_map:
                inmate_loader.add_value(key, inmate_data[value])

            inmate = inmate_loader.load_item()
            inmate[items.KEY_CHARGES] = []
            charge_loader = ItemLoader(items.Charge())

            for key, value in self.charge_map:
                charge_loader.add_value(key, inmate_data[value])

            inmate[items.KEY_CHARGES].append(charge_loader.load_item())
            inmates.append(inmate)
        return inmates
