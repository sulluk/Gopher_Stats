# -*- coding: utf-8 -*-

# Scrapy settings for bball project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bball'

SPIDER_MODULES = ['bball.spiders']
NEWSPIDER_MODULE = 'bball.spiders'
ITEM_PIPELINES = [
    'bball.pipelines.bballpipeline'
    ]
FEED_FORMAT = 'csv'
FEED_URI = 'file:Outputs/SEASONSTATS%(time)s.csv'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'TGB (+http://talkgopherbuckets.tumblr.com/)'
