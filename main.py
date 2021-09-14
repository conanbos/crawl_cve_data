# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import CNNVD_file
import downloader

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

    bs = BeautifulSoup(html.read(), 'html.parser')
    return bs





if __name__ == '__main__':
    #create beautifulsoupe and open site
    bs = create_bs(url)
    includeUrl = ''

    urls = CNNVD_file.get_internallinks(bs, includeUrl)
    print('open site:http://www.cnnvd.org.cn successfully')
    print('Start downloading vulnerability library....')
    downloader.download(urls)

    print('All files get done')





