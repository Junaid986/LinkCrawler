from HTMLParser import HTMLParser
from urlparse import urljoin

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, val) in attrs:
                if key == 'href':
                    url = urljoin(self.base_url, val)
                    self.links.add(url)

    def page_links(self):
        return self.links
