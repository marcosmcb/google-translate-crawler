
import urllib2,cookielib
import re
import urllib
from bs4 import BeautifulSoup

SITE       = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
HEADER     = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

source_lan = 'en'
target_lan = ''

languages = { 0: 'pt', 1: 'fr', 2: 'es' }

def translate( wordQuery ):
    link = SITE % (target_lan, source_lan, urllib.pathname2url(wordQuery))

    req = urllib2.Request( link, headers=HEADER )

    try:
        page = urllib2.urlopen(req) 
        soup = BeautifulSoup( page, 'lxml')    
    except urllib2.HTTPError, e:
        print e.fp.read()


    print soup.find('div', {'dir':'ltr'}).get_text()


def showMenu():
    print "Please, select a target language"
    print "[0] Portuguese"
    print "[1] French"
    print "[2] Spanish"
    return int(raw_input())

if __name__ == '__main__':
    lan = showMenu( )
    print 'Language Selected - ' + languages[ lan ]
    target_lan = languages[ lan ]
    
    print "Please, type in your word/sentence to be translated"
    translate( raw_input() )