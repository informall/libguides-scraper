from bs4 import BeautifulSoup
import requests
import re

__all__ = \
    [ 'HREF'
    , 'A'
    , 'get'
    , 'get_text'
    , 'html_parser'
    , 'url_filter'
    , 'to_site_id'
    , 'tag_to_str'
    ]

HREF = 'href'
A = 'a'

def get(url):
    return requests.get(url)

def get_text(url):
    return get(url).text

def html_parser(text):
    return BeautifulSoup(text, 'html.parser')

def url_filter(aref):
    href = aref.get(HREF)
    return href and href.startswith("http")

def to_site_id(scripts):
    found = None
    for script in scripts:
        src = script.get('src')
        if not src: break
        fa = re.search('site_id=(\d+)', src)
        found_id = fa and fa.group(1)

        if not found and found_id:
            found = found_id

        elif found and found_id:
            raise Exception("found two site ids!")

    return found

def tag_to_str(mtag):
    try:
        return mtag.text
    except:
        return mtag
