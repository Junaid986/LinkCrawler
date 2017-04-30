import threading
from Queue import Queue
from spider import Spider
from domain import *
from file_helper import *

PROJECT_NAME = 'Micron'
HOME_PAGE = 'https://www.micron.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWL_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

spider = Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME, QUEUE_FILE, CRAWL_FILE)
