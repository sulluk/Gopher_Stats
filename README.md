Gopher_Stats
============

Scrapy spider for gopher data

files saved in the DB_Download and Live_Stats folders are files that can be copied into a Scrapy project.

DB_Download will scrape data for the Gophers or the Big10 for the last 6 seasons, or just the current one.
these selections need to be made before running the spider.  The URL list file needs to be saved within the
project so that it can be called by the spider. This will output a .CSV formatted file in a folder named Outputs

Live_Stats requires an input to run.  The input should be the URL of a specific NCAAM game on ESPN.
The game can be live, or it can be historical.  This will pull the stats for both teams and calculate some
advanced stats.  All will be displayed as outputs in the terminal window, but aren't set to output to a file.
