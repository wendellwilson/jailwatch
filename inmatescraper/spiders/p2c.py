import scrapy
from scrapy.loader import ItemLoader
from inmatescraper import items
import json


class P2CSpider(scrapy.Spider):
    name = 'P2C'
    QUERY_URL_SUFFIX = '/jqHandler.ashx?op=s'
    P2C_DEFAULT_FORMDATA = {'t': 'ii', '_search': 'false', 'rows': '100000', 'page': '1', 'sidx': 'disp_name',
                            'sord': 'asc'}
    HEADER_STRING = 'Date Charged'
    P2C_DEFAULT_HEADER = ''

    def __init__(self, **kwargs):
        ##TODO take input state and county
        super().__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            post_url = url + self.QUERY_URL_SUFFIX
            ##TODO figure out required headers
            post_headers = {'POST': url + self.QUERY_URL_SUFFIX + ' HTTP/1.1',
                            'Connection': 'keep-alive',
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Origin': url,
                            'X-Requested-With': 'XMLHttpRequest',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Cache-Control': 'no-cache'}
            yield scrapy.FormRequest(dont_filter=True,
                                      formdata=self.P2C_DEFAULT_FORMDATA,
                                      headers=post_headers,
                                      url=post_url,)

    ##TODO map data names as a spider argument
    def parse(self, response):
        jsonresponse = json.loads(response.text)
        inmates = []
        for inmate_data in jsonresponse['rows']:
            inmate_loader = ItemLoader(items.Inmate())
            inmate_loader.add_value(items.KEY_FIRST_NAME, inmate_data['firstname'])
            inmate_loader.add_value(items.KEY_MIDDLE_NAME, inmate_data['middlename'])
            inmate_loader.add_value(items.KEY_LAST_NAME, inmate_data['lastname'])
            inmate_loader.add_value(items.KEY_GENDER, inmate_data['sex'])
            inmate_loader.add_value(items.KEY_DATE_OF_BIRTH, inmate_data['dob'])
            inmate_loader.add_value(items.KEY_RACE, inmate_data['race'])
            inmate_loader.add_value(items.KEY_BOOK_ID, inmate_data['book_id'])
            inmate = inmate_loader.load_item()
            inmate[items.KEY_CHARGES] = []
            charge_loader = ItemLoader(items.Charge())
            charge_loader.add_value(items.KEY_DATE_CONFINED, inmate_data['date_arr'])
            charge_loader.add_value(items.KEY_DESC, inmate_data['disp_charge'])
            charge_loader.add_value(items.KEY_AGENCY, inmate_data['disp_agency'])
            inmate[items.KEY_CHARGES].append(charge_loader.load_item())
            inmates.append(inmate)
        return inmates
