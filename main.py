# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import CNNVD_file
import NVD_CVE_file
import downloader
import time

sites = 'http://www.cnnvd.org.cn'
url = sites + '/web/xxk/xmlDown.tag'



def create_bs(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None

    source = BeautifulSoup(html.read(), 'html.parser')#, from_encoding='utf-8')
    print(source.original_encoding)
    print(source)
    return source





if __name__ == '__main__':
    #create beautifulsoupe and open site
    # bs = create_bs(url)
    # includeUrl = ''
    #
    # urls = CNNVD_file.get_internallinks(bs, includeUrl)
    # print('open site: '+sites+ ' successfully')
    # print('Start downloading vulnerability library....')
    # downloader.download(urls,33,54)
    # time.sleep(0.2)
    # print('All files get done')

# open NVD CVE
    sites = 'https://nvd.nist.gov'
    url = sites + '/vuln/data-feeds'
    bss = create_bs(url)
    includeUrl = ''
    # urls.clear()
    urls = NVD_CVE_file.get_internallinks(bss, includeUrl)
    print('open site: ' + sites + ' successfully')
    print('Start downloading vulnerability library....')
    downloader.download(urls,31,0)
    time.sleep(0.2)
    print('All files get done')





