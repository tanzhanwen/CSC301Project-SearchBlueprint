#!/usr/bin/env python

from crawler import Crawler
from threading import Lock

class TestCrawler(Crawler):
    def __init__(self):
        super(TestCrawler, self).__init__()
        self.process_lock = Lock()

    def process_document(self, doc):
        self.process_lock.acquire()
        print('GET', doc.status, doc.url)
        self.process_lock.release()

c = TestCrawler()
c.set_max_depth(5)
c.crawl('http://www.abhijeeth.com/')
print(c.visited)
print(len(c.visited))
