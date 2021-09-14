# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re
import CNNVD_file

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


# Press the green button in the gutter to run the script.
def getTitle(bs, url):
    try:

        title = ''
        links = bs.find_all('a', {'onclick': re.compile('/attached.*.zip')})
        print(len(links))
        for link in links:
            title = title + '\n' + link['onclick']

    except AttributeError as e:
        return None
    return title






if __name__ == '__main__':
    # title = getTitle('http://www.cnnvd.org.cn/web/xxk/xmlDown.tag')

    bs = create_bs(url)
    includeUrl = ''

    urls = CNNVD_file.get_internallinks(bs, includeUrl)
    print('open site:http://www.cnnvd.org.cn successfully')
    print('Start downloading vulnerability library....')
    CNNVD_file.downloader(urls)

    print('All files get done')





