# -*- coding: utf-8 -*-

# Scrapy settings for sfda project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sfda'

SPIDER_MODULES = ['sfda.spiders']
NEWSPIDER_MODULE = 'sfda.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sfda (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIE={'UserName': 'qq_34162294', '__message_gu_msg_id': '0', 'UN': 'qq_34162294', 'dc_session_id': '1488202837136', 'UserNick': 'BLMOTOF', 'uuid_tt_dd': '-1719952174247490520_20161121', '_ga': 'GA1.2.1879034154.1480664253', 'dc_tos': 'om1cnp', '_gat': '1', 'BT': '1488202848784', 'access-token': '1d44ad73-b1be-4efc-b315-cf2d967bcd79', 'UserInfo': 't4QXCOeGqh7oB5rxGYe80Hmi8eb5Iegwljq5Xk1nS2SVdu0JHV27mSuoUgI6M2z4LzmlVuNip2clHjuo4Og8moSStg2VOM%2BKnrNkwwRfNmfi8DGN7jJ4Czq%2BIjvHX1VFdJGr7UQpqUwOC%2B%2BYcH%2Bg2w%3D%3D', 'AU': 'E75', '__message_sys_msg_id': '0', '__message_in_school': '0', 'UE': "'18796327106@163.com'", 'Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac': '1488197611', 'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac': '1488083111,1488115004,1488116855,1488182666', '__message_cnel_msg_id': '0', '_message_m': 'mdqt40yxadmh13ler4h1xxx0', '__message_district_code': '000000'}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sfda.middlewares.SfdaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'sfda.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'sfda.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
