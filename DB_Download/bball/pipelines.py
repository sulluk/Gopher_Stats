# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

totals = ['Minnesota','Wisconsin','Purdue','Iowa','Penn St.','Ohio St.','Indiana','Michigan','Michigan St.','Northwestern','Illinois','Rutgers','Maryland','Nebraska']

class bballpipeline(object):

    def process_item(self, item, spider):
#drop header rows where WL field is null
        if not(item["WL"]):
            raise DropItem()
#drop team rows with minutes of >=200
        if item['NAME'][0] in totals:
            raise DropItem()
#Strip / and * denoting season highs/conference highs
        if item['FGA']:
            for a in item.keys():
                if item[a]:
                        if type(item[a][0]) == unicode:
                                if item[a][0][-1:] == '/':
                                        item[a] = [item[a][0].replace('/','')]
                                elif item[a][0][-1:] == '*':
                                        item[a] = [item[a][0].replace('*','')]
#slice season header to show season in YYYY-YY format
        item['SEASON'] = [item['SEASON'][0][5:10]]
#slice player name to specifically show position indicator
        item['POS'] = [item['POS'][0][-1:]]
#slice game outcome to just show 'W' or 'L'
        item['WL'] = [item['WL'][0][:1]]
#Determine if game is away
        if item['OPP']:
            if item['OPP'][0][:1] == '@':
                item['VENUE'] = ['AWAY']
            else:
                item['VENUE'] = ['HOME']
        if item['NS']:
            item['VENUE'] = ['NeutralSite']
#Calculate 3-point FG percentage
        if item['iiiFG']:
            item['iiiFGP'] = round(float(item['iiiFG'][0])/float(item['iiiFGA'][0]),3)
        if not(item['iiiFG']):
            item['iiiFG'] = 0
            item['iiiFGP'] = 0
        if not(item['iiiFGA']):
            item['iiiFGA'] = 0
#Calculate FG percentage
        if item['FG']:
            item['FGP'] = round(float(item['FG'][0])/float(item['FGA'][0]),3)
        if not(item['FG']):
            item['FG'] = 0
            item['FGP'] = 0
        if not(item['FGA']):
            item['FGA'] = 0
#Calculate Free throw percentage
        if item['FT']:
            item['FTP'] = round(float(item['FT'][0])/float(item['FTA'][0]),3)
        if not(item['FT']):
            item['FT'] = 0
            item['FTP'] = 0
        if not(item['FTA']):
            item['FTA'] = 0
#convert date to YYYY-MM-DD format
        if item['DTE']:
            d = str(item['DTE'][0])
            item['DTE'] = d[6:]+"-"+d[:2]+"-"+d[3:5]            
#convert nulls to zeroes
        if not(item['OREB']):
            item['OREB'] = 0
        if not(item['DREB']):
            item['DREB'] = 0
        if not(item['REB']):
            item['REB'] = 0
        if not(item['AST']):
            item['AST'] = 0
        if not(item['TRO']):
            item['TRO'] = 0
        if not(item['STL']):
            item['STL'] = 0
        if not(item['BLK']):
            item['BLK'] = 0
        if not(item['FOULS']):
            item['FOULS'] = 0
        return item
