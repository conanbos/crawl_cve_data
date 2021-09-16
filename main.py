# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# from urllib.request import urlopen
# from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import NVD_CVE_file
import CNNVD_file
import downloader
import time
import sqlite_db

sites = ''
url = ''



def create_bs(url):
    session = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Machintosh; Intel Mac OS X 10_9_5)'
               'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
               'Accept':'text/html,application/xhtml+xml,application/xml;'
               'q=0.9,image/webp,*/*;q=0.8'}

    try:
        req = session.get(url, headers=headers)#html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None
    html_source = BeautifulSoup(req.text,'html.parser')  #(html.read(), 'html.parser') #, from_encoding='utf-8')
    return html_source



def get_CNNVD():
    # create beautifulsoupe and open site
    sites = 'http://www.cnnvd.org.cn'
    url = sites + '/web/xxk/xmlDown.tag'
    urls = ''
    i=0
    while len(urls) <= 0:
        bs = create_bs(url)
        urls = CNNVD_file.get_internallinks(bs, sites)
        print("\r try connecting to site " + str(i))
        if i > 1: print(bs)
        time.sleep(0.5)

    print('open site: ' + sites + ' successfully')
    print('start downloading vulnerability library....')
    downloader.download(urls, 54)
    time.sleep(0.2)
    print('all files get done')


def get_NVD_CVE():
    # open NVD CVE
    sites = 'https://nvd.nist.gov'
    url = sites + '/vuln/data-feeds'
    urls = ''
    i=0
    while len(urls) <= 0 and i<=3:
        i+=1
        bs = create_bs(url)
        urls = NVD_CVE_file.get_internallinks(bs, sites,'nvdjson')
        print("\r try connecting to site "+str(i))
        if i>1:print(bs)
        time.sleep(0.5)

    print('open site: ' + sites + ' successfully')
    print('Start downloading vulnerability library....')
    downloader.download(urls,0)
    time.sleep(0.2)
    print('All files get done')


if __name__ == '__main__':
    #get_CNNVD()
    get_NVD_CVE()

    # i=sqlite_db.create_db('test.db')
    # if i==1:
    #     print('created database ok!')


