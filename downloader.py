

import os
import threading
import time

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
            print('#', end='')

    print('%.2f%%' % per,str(a) + '/' + str(b), end='    ')
    # print( str(a) + '/' + str(b))


def download(links,to_n):
    count = 1
    total = len(links)
    if not os.path.exists('data'):
        os.makedirs('data')


    for link in links:
        from_n=link.rfind('/',0,len(link))+1

        if to_n==0:
            local = os.path.join('data', link[from_n:])
            progressbar(count, total,link[from_n:])
        else:
            local = os.path.join('data', link[from_n:to_n])
            progressbar(count, total, link[from_n:to_n])
        count = count + 1
        if os.path.exists(local):
            print('\n')
            continue

        urllib.request.urlretrieve(link, local)
        try:
            thread1 = myThread(1, local)
            thread1.start()
        except:
            print("Error: unzip thread failed",local)
        time.sleep(0.1)
    return 1