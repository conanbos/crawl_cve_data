
import urllib.request
import re
import os
import threading
import unzip_file
import main

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

def combine_link(origin_link):
    pop_link = ''
    pop_link = main.sites + origin_link[16:25] + origin_link[26:48]
    return pop_link


def get_internallinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(main.urlparse(includeUrl).scheme, main.urlparse(includeUrl).netloc)
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
    if not os.path.exists('data'):
        os.makedirs('data')

    for link in links:
        local = os.path.join('data', link[33:54])
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

