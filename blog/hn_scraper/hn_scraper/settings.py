# -*- coding: utf-8 -*-

# Scrapy settings for hn_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hn_scraper'

SPIDER_MODULES = ['hn_scraper.spiders']
NEWSPIDER_MODULE = 'hn_scraper.spiders'

#--------------------------------------------------------------------------
# Frontier Settings
#--------------------------------------------------------------------------

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'hn_scraper (+http://www.yourdomain.com)'


DOWNLOAD_HANDLERS = {
#    'http': 'kafka_downloader.KafkaDownloadHandler',
    'https': 'kafka_downloader.KafkaDownloadHandler',
}

KAFKA_LOCATION = 'localhost:9092'
KAFKA_RESPONSES_TOPIC = 'responses'
KAFKA_REQUESTS_TOPIC = 'requests'
KAFKA_CONSUMER_GROUP = 'scrapy-cloud-downloader'

LOG_LEVEL='INFO'