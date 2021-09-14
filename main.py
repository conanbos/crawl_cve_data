# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re
import os
import unzip_file
import threading

def start_unzip(filepath):
    try:
        aa = unzip_file.unzip(filepath)
    except:
        return 0
    return 1

class myThread (threading.Thread):
    def __init__(self, threadID, zipname ):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.zipname = zipname

    def run(self):
        start_unzip(self.zipname)




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


def combine_link(origin_link):
    pop_link = ''
    pop_link = sites + origin_link[16:25] + origin_link[26:48]
    return pop_link


def get_internallinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internallinks = []
    for link in bs.find_all('a', onclick=re.compile('/attached.*.zip')):
        # print(link.attrs['onclick'])
        if link.attrs['onclick'] is not None:
            if link.attrs['onclick'] not in internallinks:
                if (link.attrs['onclick'].startswith('/')):
                    internallinks.append(includeUrl + combine_link(link.attrs['onclick']))
                else:
                    internallinks.append(combine_link(link.attrs['onclick']))
    return internallinks



def progressbar(a, b,fn):
    print(fn+'         ', end="")
    per = a / b * 100
    for i in range(1, a):
        for y in range(1,3):
            print('#', end="")

    print('%.2f%%' % per,str(a) + '/' + str(b), end='  ')
    # print( str(a) + '/' + str(b))




def downloader(links):
    count = 1
    total = len(links)
    for link in links:
        local = os.path.join('src', link[33:54])
        progressbar(count, total,link[33:54])
        # print(count)
        count = count + 1
        urllib.request.urlretrieve(link, local)
        try:
            thread1 = myThread(1, local)
            thread1.start()
        except:
            print("Error: unzip thread failed",local)
    return 1






if __name__ == '__main__':
    # title = getTitle('http://www.cnnvd.org.cn/web/xxk/xmlDown.tag')
    sites = 'http://www.cnnvd.org.cn'
    url = sites + '/web/xxk/xmlDown.tag'
    bs = create_bs(url)
    includeUrl = ''
    urls = get_internallinks(bs, includeUrl)
    print('open site:http://www.cnnvd.org.cn successfully')
    print('Start downloading vulnerability library....')
    downloader(urls)

    print('All files get done')





