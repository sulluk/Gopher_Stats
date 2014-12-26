# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LivestatsPipeline(object):
    def process_item(self, item, spider):
        item['FGP'] = item['FG'][1]
        item['FG'] = item['FG'][0][:item['FG'][0].index('-')]
        item['FGA'] = item['FGA'][0][item['FGA'][0].index('-')+1:]

        item['FTP'] = item['FT'][1]
        item['FT'] = item['FT'][0][:item['FT'][0].index('-')]
        item['FTA'] = item['FTA'][0][item['FTA'][0].index('-')+1:]

        item['iiiFGP'] = item['iiiFG'][1]
        item['iiiFG'] = item['iiiFG'][0][:item['iiiFG'][0].index('-')]
        item['iiiFGA'] = item['iiiFGA'][0][item['iiiFGA'][0].index('-')+1:]

        item['TEAM_POSS'] = round(float(item['FGA'])-float(item['OREB'][0])+float(item['TRO'][0])+float(item['FTA'])*.475,2)
        item['PtsPerPoss'] = round(float(item['PTS'][0])/item['TEAM_POSS'],2)
        item['eFG_PCT'] = round((float(item['FG'])+(float(item['iiiFG'])*.5))/float(item['FGA']),3)
        item['OREB_PCT'] = round(float(item['OREB'][0])/(float(item['OREB'][0])+float(item['OPP_DREB'][0])),3)
        item['TRO_PCT'] = round(float(item['TRO'][0])/item['TEAM_POSS'],3)
        item['FTRATE'] = round(float(item['FTA'])/float(item['FGA']),3)
        return item
                
