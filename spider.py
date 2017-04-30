import urllib2
from link_parser import LinkFinder
from file_helper import *

class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, proj_name, base_url, domain_name, queue_file, crawl_file):
        Spider.project_name = proj_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = queue_file
        Spider.crawled_file = crawl_file
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url, Spider.queue_file, Spider.crawled_file)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print '{} now crawling {}'.format(thread_name, page_url)
            print 'Queue {}'.format(str(len(Spider.queue)))
            print 'Crawled {}'.format(str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            try:
                Spider.queue.remove(page_url)
            except:
                pass
            Spider.crawled.add(page_url)
            Spider.update_file()


    @staticmethod
    def gather_links(page_url):
        html_data = ""
        try:
            request = urllib2.Request(page_url)
            response = urllib2.urlopen(request)
            print str(response.headers['Content-Type'])
            print str(response.headers.getencoding())
            if response.headers['Content-Type'].split(';')[0] == 'text/html':
                html_data = response.read()
                link_parser = LinkFinder(Spider.base_url, page_url)
                link_parser.feed(html_data)
        except Exception,e:
            print str(e)
            return set()
        return link_parser.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_file():
        print 'Queue {}'.format(str(Spider.queue))
        print 'Crawled {}'.format(str(Spider.crawled))
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)



#spider = Spider("jun2", "http://www.google.co.in/", "www.google.com")
#Spider.gather_links('http://python.org/')



