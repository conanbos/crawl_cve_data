

import os
import threading
import unzip_file
import urllib.request


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

def progressbar(a, b,fn):
    print(fn+'         ', end="")
    per = a / b * 100
    for i in range(1, a):
        for y in range(1,3):
            print('#', end="")

    print('%.2f%%' % per,str(a) + '/' + str(b), end='  ')
    # print( str(a) + '/' + str(b))


def download(links):
    count = 1
    total = len(links)
    if not os.path.exists('data'):
        os.makedirs('data')

    for link in links:
        local = os.path.join('data', link[33:54])
        progressbar(count, total,link[33:54])
        urllib.request.urlretrieve(link, local)
        try:
            thread1 = myThread(1, local)
            thread1.start()
        except:
            print("Error: unzip thread failed",local)
        break
    return 1