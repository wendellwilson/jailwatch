from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders import p2c
import csv

URL_PREFIX = 'http://'

##Load urls
with open('nc_sites.csv') as f:
    site_list = [tuple(line) for line in csv.reader(f)]

process = CrawlerProcess(get_project_settings())

##For each site
for crawler_name, state, county, url in site_list:
    # Crawl site
    inmate_data = {"state": state, "county": county}
    process.crawl(crawler_name, start_urls=[URL_PREFIX + url], inmate_data=inmate_data)

process.start()
# Pull county data

#For each record
#Check for record
#Sync record data
#Create new record