# -*- coding: utf-8 -*-

# Scrapy settings for livestats project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'livestats'

SPIDER_MODULES = ['livestats.spiders']
NEWSPIDER_MODULE = 'livestats.spiders'

ITEM_PIPELINES = [
    'livestats.pipelines.LivestatsPipeline'
    ]
FEED_FORMAT = 'csv'
FEED_URI = 'file:Outputs/LiveSTATS%(time)s.csv'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'TGB (+http://talkgopherbuckets.tumblr.com/)'
