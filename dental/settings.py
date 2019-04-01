# -*- coding: utf-8 -*-
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from config import Config

BOT_NAME = 'dental'

SPIDER_MODULES = ['dental.spiders']
NEWSPIDER_MODULE = 'dental.spiders'


CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
    drivername="mysql",
    user=Config.user,
    passwd=Config.passwd,
    host=Config.host,
    port=Config.port,
    db_name=Config.database,
)


ITEM_PIPELINES = {
    'dental.pipelines.DentalSpiderPipeline': 300,
}


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

LOG_LEVEL = 'ERROR'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16
