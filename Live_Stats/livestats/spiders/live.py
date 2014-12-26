# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from livestats.items import LivestatsItem


class LiveSpider(scrapy.Spider):
    name = "live"
    allowed_domains = ["http://scores.espn.go.com"]
    start_urls = (
        'http://scores.espn.go.com/ncb/boxscore?gameId=400585728',
    )
    
#Need to add a pipeline and calculate stats.  Might be worth pulling in overall team stats in here
#or else in a separate spider that hits tbody 3 and 6.  can calculate stats in pipeline for players and for teams
#dont need overall identifying info in here as the game details will be known when pulling live stats from it.

    def parse(self, response):
        sel = Selector(response)
        a_starters = sel.xpath("//table[@class='mod-data']/tbody[1]/tr")
        stats = []
        for game in a_starters:
            item = LivestatsItem()
            item['TEAM'] = sel.xpath("//table[@class='mod-data']/thead[1]/tr[1]/th/text()").extract()
            item['DTE'] = sel.xpath("//div[@class='game-time-location']/p[1]/text()").extract()
            item['VENUE'] = ['Away']
            item['NAME'] = game.xpath('./td/a/text()').extract()
            item['POS'] = game.xpath('./td[1]/text()').extract()
            item['MP'] = game.xpath('./td[2]/text()').extract()
            item['FG'] = game.xpath('./td[3]/text()').extract()
            item['FGA'] = game.xpath('./td[3]/text()').extract()
            item['iiiFG'] = game.xpath('./td[4]/text()').extract()
            item['iiiFGA'] = game.xpath('./td[4]/text()').extract()
            item['FT'] = game.xpath('./td[5]/text()').extract()
            item['FTA'] = game.xpath('./td[5]/text()').extract()
            item['OREB'] = game.xpath('./td[6]/text()').extract()
            item['DREB'] = game.xpath('./td[7]/text()').extract()
            item['REB'] = game.xpath('./td[8]/text()').extract()
            item['AST'] = game.xpath('./td[9]/text()').extract()
            item['STL'] = game.xpath('./td[10]/text()').extract()
            item['BLK'] = game.xpath('./td[11]/text()').extract()
            item['TRO'] = game.xpath('./td[12]/text()').extract()
            item['FOULS'] = game.xpath('./td[13]/text()').extract()
            item['PTS'] = game.xpath('./td[14]/text()').extract()
            item['LINK'] = response.url
            stats.append(item)

        a_bench = sel.xpath("//table[@class='mod-data']/tbody[2]/tr")
        
        for game in a_bench:
            item = LivestatsItem()
            item['TEAM'] = sel.xpath("//table[@class='mod-data']/thead[1]/tr[1]/th/text()").extract()
            item['DTE'] = sel.xpath("//div[@class='game-time-location']/p[1]/text()").extract()
            item['VENUE'] = ['Away']
            item['NAME'] = game.xpath('./td/a/text()').extract()
            item['POS'] = game.xpath('./td[1]/text()').extract()
            item['MP'] = game.xpath('./td[2]/text()').extract()
            item['FG'] = game.xpath('./td[3]/text()').extract()
            item['FGA'] = game.xpath('./td[3]/text()').extract()
            item['iiiFG'] = game.xpath('./td[4]/text()').extract()
            item['iiiFGA'] = game.xpath('./td[4]/text()').extract()
            item['FT'] = game.xpath('./td[5]/text()').extract()
            item['FTA'] = game.xpath('./td[5]/text()').extract()
            item['OREB'] = game.xpath('./td[6]/text()').extract()
            item['DREB'] = game.xpath('./td[7]/text()').extract()
            item['REB'] = game.xpath('./td[8]/text()').extract()
            item['AST'] = game.xpath('./td[9]/text()').extract()
            item['STL'] = game.xpath('./td[10]/text()').extract()
            item['BLK'] = game.xpath('./td[11]/text()').extract()
            item['TRO'] = game.xpath('./td[12]/text()').extract()
            item['FOULS'] = game.xpath('./td[13]/text()').extract()
            item['PTS'] = game.xpath('./td[14]/text()').extract()
            item['LINK'] = response.url
            stats.append(item)

        b_starters = sel.xpath("//table[@class='mod-data']/tbody[4]/tr")
        for game in b_starters:
            item = LivestatsItem()
            item['TEAM'] = sel.xpath("//table[@class='mod-data']/thead[3]/tr[1]/th/text()").extract()
            item['DTE'] = sel.xpath("//div[@class='game-time-location']/p[1]/text()").extract()
            item['VENUE'] = ['Home']
            item['NAME'] = game.xpath('./td/a/text()').extract()
            item['POS'] = game.xpath('./td[1]/text()').extract()
            item['MP'] = game.xpath('./td[2]/text()').extract()
            item['FG'] = game.xpath('./td[3]/text()').extract()
            item['FGA'] = game.xpath('./td[3]/text()').extract()
            item['iiiFG'] = game.xpath('./td[4]/text()').extract()
            item['iiiFGA'] = game.xpath('./td[4]/text()').extract()
            item['FT'] = game.xpath('./td[5]/text()').extract()
            item['FTA'] = game.xpath('./td[5]/text()').extract()
            item['OREB'] = game.xpath('./td[6]/text()').extract()
            item['DREB'] = game.xpath('./td[7]/text()').extract()
            item['REB'] = game.xpath('./td[8]/text()').extract()
            item['AST'] = game.xpath('./td[9]/text()').extract()
            item['STL'] = game.xpath('./td[10]/text()').extract()
            item['BLK'] = game.xpath('./td[11]/text()').extract()
            item['TRO'] = game.xpath('./td[12]/text()').extract()
            item['FOULS'] = game.xpath('./td[13]/text()').extract()
            item['PTS'] = game.xpath('./td[14]/text()').extract()
            item['LINK'] = response.url
            stats.append(item)

        b_bench = sel.xpath("//table[@class='mod-data']/tbody[5]/tr")
        
        for game in b_bench:
            item = LivestatsItem()
            item['TEAM'] = sel.xpath("//table[@class='mod-data']/thead[3]/tr[1]/th/text()").extract()
            item['DTE'] = sel.xpath("//div[@class='game-time-location']/p[1]/text()").extract()
            item['VENUE'] = ['Home']
            item['NAME'] = game.xpath('./td/a/text()').extract()
            item['POS'] = game.xpath('./td[1]/text()').extract()
            item['MP'] = game.xpath('./td[2]/text()').extract()
            item['FG'] = game.xpath('./td[3]/text()').extract()
            item['FGA'] = game.xpath('./td[3]/text()').extract()
            item['iiiFG'] = game.xpath('./td[4]/text()').extract()
            item['iiiFGA'] = game.xpath('./td[4]/text()').extract()
            item['FT'] = game.xpath('./td[5]/text()').extract()
            item['FTA'] = game.xpath('./td[5]/text()').extract()
            item['OREB'] = game.xpath('./td[6]/text()').extract()
            item['DREB'] = game.xpath('./td[7]/text()').extract()
            item['REB'] = game.xpath('./td[8]/text()').extract()
            item['AST'] = game.xpath('./td[9]/text()').extract()
            item['STL'] = game.xpath('./td[10]/text()').extract()
            item['BLK'] = game.xpath('./td[11]/text()').extract()
            item['TRO'] = game.xpath('./td[12]/text()').extract()
            item['FOULS'] = game.xpath('./td[13]/text()').extract()
            item['PTS'] = game.xpath('./td[14]/text()').extract()
            item['LINK'] = response.url
            stats.append(item)
        return stats
