

import os
import threading
import time
import prbar



import unzip_file
import urllib.request

progress = prbar.ProgressBar(0, fmt=prbar.ProgressBar.FULL)

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




# def progressbar(a, b,fn):
    # print(fn+'         ', end="")
    # per = a / b * 100
    # for i in range(1, a):
    #     for y in range(1,3):
    #         print('#', end='')
    #
    # print('%.2f%%' % per,str(a) + '/' + str(b), end=' ')
    # # print( str(a) + '/' + str(b))




def download(links,to_n):

    total = len(links)
    progress.total = total
    filen = ''
    if not os.path.exists('data'):#如果没有目录，创建目录
        os.makedirs('data')


    for link in links:
        from_n=link.rfind('/',0,len(link))+1

        if to_n==0:
            local = os.path.join('data', link[from_n:])
            filen = link[from_n:]
        else:
            local = os.path.join('data', link[from_n:to_n])
            filen = link[from_n:to_n]


        if os.path.exists(local):  #过滤掉已经下载的
            continue

        urllib.request.urlretrieve(link, local)
        try:
            thread1 = myThread(1, local)
            thread1.start()
            progress.msg =filen
        except:
            print("Error: unzip thread failed",local)

        progress.current += 1
        progress()
    progress.done()
    return 1