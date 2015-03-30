"""Reporting subsystem for web crawler."""

import time
import sqlite3

class Stats:
    """Record stats of various sorts."""

    def __init__(self):
        self.stats = {}

    def add(self, key, count=1):
        self.stats[key] = self.stats.get(key, 0) + count

    def report(self, file=None):
        for key, count in sorted(self.stats.items()):
            print('%10d' % count, key, file=file)


def report(crawler, file=None):
    """connect to db"""
    try:
        conn = sqlite3.connect('db.sqlite3')
    except:
        print ("I am unable to connect to the database")
    
    cur = conn.cursor()
    prefix = crawler.roots.pop()
    SQL = "INSERT INTO home_domain (name) VALUES (?);"
    data = (prefix,)
    cur.execute(SQL, data)
    conn.commit()
    
    SQL = "SELECT id FROM home_domain WHERE name=(?);"
    data = (prefix,)
    cur.execute(SQL, data)
    current_id = cur.fetchone()[0]
    
    """Print a report on all completed URLs."""
    finalList = []
    urlCount = 0
    t1 = crawler.t1 or time.time()
    dt = t1 - crawler.t0
    if dt and crawler.max_tasks:
        speed = len(crawler.done) / dt / crawler.max_tasks
    else:
        speed = 0
    stats = Stats()
    print('*** Report ***', file=file)
    try:
        show = list(crawler.done)
        show.sort(key=lambda _stat: _stat.url)
        for stat in show:
            url_report(stat, stats, file=file)
            
            SQL = "INSERT INTO home_address (title,domain_id) VALUES (?,?);"

            data = (stat.url,current_id,)
            cur.execute(SQL, data)
            if urlCount < 10:
                finalList.append(stat.url)
                urlCount += 1
        conn.commit()
        cur.close()
        conn.close()
    except KeyboardInterrupt:
        print('\nInterrupted', file=file)
    print('Finished', len(crawler.done),
          'urls in %.3f secs' % dt,
          '(max_tasks=%d)' % crawler.max_tasks,
          '(%.3f urls/sec/task)' % speed,
          file=file)
    stats.report(file=file)
    print('Todo:', crawler.q.qsize(), file=file)
    print('Done:', len(crawler.done), file=file)
    print('Date:', time.ctime(), 'local time', file=file)
    
    return finalList

def url_report(stat, stats, file=None):
    """Print a report on the state for this URL.

    Also update the Stats instance.
    """
    if stat.exception:
        stats.add('fail')
        stats.add('fail_' + str(stat.exception.__class__.__name__))
        print(stat.url, 'error', stat.exception, file=file)
    elif stat.next_url:
        stats.add('redirect')
        print(stat.url, stat.status, 'redirect', stat.next_url,
              file=file)
    elif stat.content_type == 'text/html':
        stats.add('html')
        stats.add('html_bytes', stat.size)
        print(stat.url, stat.status,
              stat.content_type, stat.encoding,
              stat.size,
              '%d/%d' % (stat.num_new_urls, stat.num_urls),
              file=file)
    else:
        if stat.status == 200:
            stats.add('other')
            stats.add('other_bytes', stat.size)
        else:
            stats.add('error')
            stats.add('error_bytes', stat.size)
            stats.add('status_%s' % stat.status)
        print(stat.url, stat.status,
              stat.content_type, stat.encoding,
              stat.size,
              file=file)
