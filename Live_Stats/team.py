# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from livestats.items import LivestatsItem


class LiveSpider(scrapy.Spider):
    name = "team"
    cookies_enabled = False
    allowed_domains = ["http://scores.espn.go.com"]
#    start_urls = (
#        'http://scores.espn.go.com/ncb/boxscore?gameId=400585728',
#    )
    start_urls = (
        raw_input(['Paste ESPN Mens BBall game url like: http://scores.espn.go.com/ncb/boxscore?gameId=400585728']),
    )

    def parse(self, response):
        sel = Selector(response)
        away_team = sel.xpath("//table[@class='mod-data']/tbody[3]/tr")
        home_team = sel.xpath("//table[@class='mod-data']/tbody[6]/tr")
        stats = []
        item = LivestatsItem()
        item['TEAM'] = sel.xpath("//table[@class='mod-data']/thead[1]/tr[1]/th/text()").extract()
        item['DTE'] = sel.xpath("//div[@class='game-time-location']/p[1]/text()").extract()
        item['VENUE'] = ['Away']
        item['FG'] = away_team.xpath('./td[2]/text()').extract()
        item['FGA'] = away_team.xpath('./td[2]/text()').extract()
        item['iiiFG'] = away_team.xpath('./td[3]/text()').extract()
        item['iiiFGA'] = away_team.xpath('./td[3]/text()').extract()
        item['FT'] = away_team.xpath('./td[4]/text()').extract()
        item['FTA'] = away_team.xpath('./td[4]/text()').extract()
        item['OREB'] = away_team.xpath('./td[5]/text()').extract()
        item['DREB'] = away_team.xpath('./td[6]/text()').extract()
        item['OPP_DREB'] = home_team.xpath('./td[6]/text()').extract()
        item['REB'] = away_team.xpath('./td[7]/text()').extract()
        item['AST'] = away_team.xpath('./td[8]/text()').extract()
        item['STL'] = away_team.xpath('./td[9]/text()').extract()
        item['BLK'] = away_team.xpath('./td[10]/text()').extract()
        item['TRO'] = away_team.xpath('./td[11]/text()').extract()
        item['FOULS'] = away_team.xpath('./td[12]/text()').extract()
        item['PTS'] = away_team.xpath('./td[13]/text()').extract()
        stats.append(item)
        
        item = LivestatsItem()
        item['TEAM'] = sel.xpath("//table[@class='mod-data']/thead[3]/tr[1]/th/text()").extract()
        item['DTE'] = sel.xpath("//div[@class='game-time-location']/p[1]/text()").extract()
        item['VENUE'] = ['Home']
        item['FG'] = home_team.xpath('./td[2]/text()').extract()
        item['FGA'] = home_team.xpath('./td[2]/text()').extract()
        item['iiiFG'] = home_team.xpath('./td[3]/text()').extract()
        item['iiiFGA'] = home_team.xpath('./td[3]/text()').extract()
        item['FT'] = home_team.xpath('./td[4]/text()').extract()
        item['FTA'] = home_team.xpath('./td[4]/text()').extract()
        item['OREB'] = home_team.xpath('./td[5]/text()').extract()
        item['DREB'] = home_team.xpath('./td[6]/text()').extract()
        item['OPP_DREB'] = away_team.xpath('./td[6]/text()').extract()
        item['REB'] = home_team.xpath('./td[7]/text()').extract()
        item['AST'] = home_team.xpath('./td[8]/text()').extract()
        item['STL'] = home_team.xpath('./td[9]/text()').extract()
        item['BLK'] = home_team.xpath('./td[10]/text()').extract()
        item['TRO'] = home_team.xpath('./td[11]/text()').extract()
        item['FOULS'] = home_team.xpath('./td[12]/text()').extract()
        item['PTS'] = home_team.xpath('./td[13]/text()').extract()
        stats.append(item)
        return stats
