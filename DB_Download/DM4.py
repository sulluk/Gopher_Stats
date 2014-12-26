from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from bball.items import BballItem
from bball.URL_List import BIG_Hist, MINN_Hist, BIG_CY, MINN_CY

class StatSpider(CrawlSpider):
    name = "dm4"
    allowed_domains = ["stats.ncaa.org"]
    COOKIES_Enabled = False
#    start_urls = ["http://stats.ncaa.org/player?game_sport_year_ctl_id=11220&stats_player_seq=1290368.0"]
#    start_urls = BIG_Hist
#    start_urls = BIG_CY
#    start_urls = MINN_Hist
    start_urls = MINN_CY
    rules = [
        Rule(SgmlLinkExtractor(restrict_xpaths=('/html/body/div[2]/div[2]/table/tbody')),follow=True),
        Rule(SgmlLinkExtractor(unique=True),callback='parse_item'),
    ]

    def parse_item(self, response):
#    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        games = hxs.select('//div[@id="game_breakdown_div"]//table[@class="mytable"]//tr')
        stats = []
        for game in games:
            item = BballItem()
            item['LINK'] = response.url
            item['SEASON'] = hxs.select('/html/body/div[@class="header"]/div[@class="appTitle"]/text()').extract()
            item['TEAM'] = hxs.select('//div[@id="contentArea"]/h1/text()').extract()
            item['NAME'] = hxs.select('//*[@id="stats_player_person_id"]/option[@selected]/text()').extract()
            item['POS'] = hxs.select('//*[@id="stats_player_person_id"]/option[@selected]/text()').extract()
            item['DTE'] = game.select('./td[1]/text()').extract()
            item['OPP'] = game.select('./td[2]/a/text()[1]').extract()
            item['NS'] = game.select('./td[2]/a/text()[2]').extract()
            item['WL'] = game.select('./td[3]/a/text()').extract()
            item['SCORE'] = game.select('./td[3]/a//text()').extract()
            item['MP'] = game.select('./td[4]/div/text()').extract()
            item['FG'] = game.select('./td[5]//div/text()').extract()
            item['FGA'] = game.select('./td[6]/div/text()').extract()
            item['iiiFG'] = game.select('./td[7]/div/text()').extract()
            item['iiiFGA'] = game.select('.//td[8]/div/text()').extract()
            item['FT'] = game.select('./td[9]/div/text()').extract()
            item['FTA'] = game.select('./td[10]/div/text()').extract()
            item['PTS'] = game.select('./td[11]/div/text()').extract()
            item['OREB'] = game.select('./td[12]/div/text()').extract()
            item['DREB'] = game.select('./td[13]/div/text()').extract()
            item['REB'] = game.select('./td[14]/div/text()').extract()
            item['AST'] = game.select('./td[15]/div/text()').extract()
            item['TRO'] = game.select('./td[16]/div/text()').extract()
            item['STL'] = game.select('./td[17]/div/text()').extract()
            item['BLK'] = game.select('./td[18]/div/text()').extract()
            item['FOULS'] = game.select('./td[19]/div/text()').extract()
            stats.append(item)
        return stats
