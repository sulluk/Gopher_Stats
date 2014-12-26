# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LivestatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TEAM = scrapy.Field()
    DTE = scrapy.Field()
    FG = scrapy.Field()
    FGA = scrapy.Field()
    FGP = scrapy.Field()
    iiiFG = scrapy.Field()
    iiiFGA = scrapy.Field()
    iiiFGP = scrapy.Field()
    FT = scrapy.Field()
    FTA = scrapy.Field()
    FTP = scrapy.Field()
    PTS = scrapy.Field()
    OREB = scrapy.Field()
    DREB = scrapy.Field()
    OPP_DREB = scrapy.Field()
    REB = scrapy.Field()
    AST = scrapy.Field()
    TRO = scrapy.Field()
    STL = scrapy.Field()
    BLK = scrapy.Field()
    FOULS = scrapy.Field()
    VENUE = scrapy.Field()
    TEAM_POSS = scrapy.Field()
    PtsPerPoss = scrapy.Field()
    eFG_PCT = scrapy.Field()
    OREB_PCT = scrapy.Field()
    TRO_PCT = scrapy.Field()
    FTRATE = scrapy.Field()
    pass
