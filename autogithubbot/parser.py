from bs4 import BeautifulSoup, SoupStrainer
from html import unescape
from urllib import parse

def parser(message):
    soup = BeautifulSoup(unescape(message.body_html), parse_only=SoupStrainer('a'))
    for link in soup:
        if link.has_attr('href'):
            url = parse.urlparse(link['href'])
            results = check_url(url)
            if results:
                return results[0], results[1]
    return False

def check_url(url):
    if url.netloc == 'github.com':
        if url.path:
            path = url.path[1:] if url.path[0] == '/' else url.path
            path = path.split('/')
            if len(path) >= 2:
                return path[0], path[1]
    return False
