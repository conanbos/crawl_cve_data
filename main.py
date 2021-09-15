# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from urllib.request import urlopen
from urllib.parse import urlparse
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
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None
    html_source = BeautifulSoup(html.read(), 'html.parser') #, from_encoding='utf-8')
    return html_source



def get_CNNVD():
    # create beautifulsoupe and open site
    sites = 'http://www.cnnvd.org.cn'
    url = sites + '/web/xxk/xmlDown.tag'
    urls = ''


    while len(urls) <= 0:
        bs = create_bs(url)
        urls = CNNVD_file.get_internallinks(bs, sites)
        print("try connecting to site")
        time.sleep(0.2)

    print('open site: ' + sites + ' successfully')
    print('start downloading vulnerability library....')
    #downloader.download(urls, 54)
    time.sleep(0.2)
    print('all files get done')


def get_NVD_CVE():
    # open NVD CVE
    sites = 'https://nvd.nist.gov'
    url = sites + '/vuln/data-feeds'
    urls = ''
    while len(urls) <= 0:
        bs = create_bs(url)
        urls = NVD_CVE_file.get_internallinks(bs, sites,'all')
        print("try connecting to site")
        time.sleep(1)

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


