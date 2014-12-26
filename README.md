Gopher_Stats
============

Scrapy spider for gopher data

Scrapy projects are saved as DB_Download and Live_Stats.

Clone DB_Download and run spider DM4 to scrape basketball stats that will output in CSV.  
Default setting is to scrape just the gophers for the current season.  Option to scrape for all BIG 10 teams for the last 6 seasons. This will output a .CSV formatted file in a folder named Outputs

Live_Stats will prompt for an input to run.  The input should be the URL of a specific NCAAM game on ESPN.
The game can be live, or it can be historical.  This will pull the stats for both teams and calculate some
advanced stats.  All will be displayed as outputs in the terminal window, but aren't set to output to a file.
