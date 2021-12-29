


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
# import json_data
import dataset_json
import mysql_db


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
    i = 0
    while len(urls) <= 0 and i <= 3:
        i += 1
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
    i = 0
    while len(urls) <= 0 and i <= 3:
        i += 1
        bs = create_bs(url)
        urls = NVD_CVE_file.get_internallinks(bs, sites, 'nvdjson')
        print("\r try connecting to site "+str(i))
        if i > 1 : print(bs)
        time.sleep(0.5)

    print('open site: ' + sites + ' successfully')
    print('Start downloading vulnerability library....')
    downloader.download(urls, 0)
    time.sleep(0.2)
    print('Download has completed')

def NVD_DB():
    jd = dataset_json.read_file('data/nvdcve-1.1-modified.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-recent.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2021.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2020.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2019.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2018.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2017.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2016.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2015.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2014.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2013.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2012.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2011.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2010.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2009.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2008.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2007.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2006.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2005.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2004.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2003.json')
    jd = dataset_json.read_file('data/nvdcve-1.1-2002.json')
    print("Vulnerability database (NVD) has been created")


if __name__ == '__main__':
    # jd=dataset_json.read_file('data/nvd_dataset.json')
    #  jd=dataset_json.read_file('data/nvdcve-1.1-2021.json')
    # get_CNNVD()
    # get_NVD_CVE()
    NVD_DB()
    # mysql_db.VData()
    # sql = "INSERT INTO nvd_cve VALUES (%s,%s,%s,%s,%s,%s,%s)"  # 合成CVE表所有字段
    # cve=("a","dfd","4.0","cve-d343rt","dfsdf@dfd.com","2021","2021-12-01")
    # mysql_db.VData.insert_data(sql, cve)
    # mysql_db.VData.commit_data()
    # mysql_db.VData.disconnect()







