#!/usr/bin/env python3

import re
import urllib.parse as parse

reg = re.compile('^GET (?P<url>https?://[^ ]*)')


def get_url_request(get):
    b = reg.search(get)
    if not b:
        return False
    url = b.group('url')
    if url:
        return parse.urlparse(url)


if __name__ == '__main__':
    print(get_url_request('GET http://fxfeeds.mozilla.com/en-US/firefox/headlines.xml HTTP/1.1'))
    print(get_url_request('GET https://www.google.com/ HTTP/1.1'))
    print(get_url_request('http://www.google.com/'))
