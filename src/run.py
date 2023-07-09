from scrapy.crawler import CrawlerProcess
from vividseats.spiders.vvs import VvsSpider
from scrapy.utils.project import get_project_settings
import csv
from os import remove
import datetime
from  drpbx import AbsMethds
from statfuncs import StatFuncs
settings=get_project_settings()
dropbox_ = AbsMethds()
stats = StatFuncs()
process = CrawlerProcess(settings)
now = datetime.datetime.now().__str__().split(" ")[0]
f1 = open("eventOUTPUT.csv","w")
f2 = open("ticketOUTPUT.csv","w")
events_writer = csv.DictWriter(
    f1, fieldnames = ['venue_url', 'venue_id', 'venue_name', 'event_name', 'production_id', 'venue_name', 'event_url', 'event_date', 'event_time', 'timestamp']

)
tickets_writer = csv.DictWriter(
    f2, fieldnames= [ 'production_id', 'venue_name', 'event_name', 'event_date', 'event_time', 'row', 'section', 'split', 'amount', 'price', 'instant_del', 'zone_seating', 'timestamp', 'venue_id']

)
events_writer.writeheader()
tickets_writer.writeheader()
f1.close()
f2.close()

process.crawl('vvs')
process.start() 

stats.update_gstats()      

dropbox_.upload__OUTPUTCSV()
remove('ticketOUTPUT.csv')
remove('eventOUTPUT.csv')


