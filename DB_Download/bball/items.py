# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BballItem(Item):
    NAME = Field()
    POS = Field()
    TEAM = Field()
    DTE = Field()
    OPP = Field()
    WL = Field()
    SCORE = Field()
    MP = Field()
    FG = Field()
    FGA = Field()
    FGP = Field()
    iiiFG = Field()
    iiiFGA = Field()
    iiiFGP = Field()
    FT = Field()
    FTA = Field()
    FTP = Field()
    PTS = Field()
    OREB = Field()
    DREB = Field()
    REB = Field()
    AST = Field()
    TRO = Field()
    STL = Field()
    BLK = Field()
    FOULS = Field()
    LINK = Field()
    SEASON = Field()
    NS = Field()
    VENUE = Field()
    pass
