# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

KEY_FIRST_NAME = "first_name"
KEY_MIDDLE_NAME = "middle_name"
KEY_LAST_NAME = "last_name"
KEY_OFFENDER_ID = "offender_id" # Durham and Vine ID
KEY_PRISONER_ID = "prisoner_id" # Mecklenburg County ID
KEY_OFFENDER_NUM = "offender_number" # Department Of Public Safety ID
KEY_AGE = "age"
KEY_RACE = "race"
KEY_GENDER = "gender"
KEY_DATE_OF_BIRTH = "date_of_birth"
KEY_CHARGES = "charges"
KEY_DATE_CONFINED = "date_confined"
KEY_DATE_CHARGED = "date_charged"
KEY_DATE_RELEASED = "date_released"
KEY_STATUTE = "statute"
KEY_BOND_TYPE = "bond_type"
KEY_BOND_AMOUNT = "bond_amount"
KEY_COURT_DOCKET = "court_docket"
KEY_DAYS_CHARGE = "days_charge"
KAY_AGENCY = "agency"

class Charge(scrapy.Item):
    date_confined = scrapy.Field()
    date_charged = scrapy.Field()
    date_released = scrapy.Field()
    statute = scrapy.Field()
    bond_type = scrapy.Field()
    bond_amount = scrapy.Field()
    court_docket = scrapy.Field()
    days_charge = scrapy.Field()
    agency = scrapy.Field()

class Inmate(scrapy.Item):
    first_name = scrapy.Field()
    middle_name = scrapy.Field()
    last_name = scrapy.Field()
    id = scrapy.Field()
    charges = scrapy.Field()
    race = scrapy.Field()
    gender = scrapy.Field()
    date_of_birth = scrapy.Field()
