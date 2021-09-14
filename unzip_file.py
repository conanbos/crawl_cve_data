import zipfile
import unzip_file
def test():
    print('hello')

def unzip(unzipfn):
    azip = zipfile.ZipFile(unzipfn)  # ['bb/', 'bb/aa.txt']
    # 返回所有文件夹和文件
    flist=azip.namelist()
    for fn in flist:
        print(fn + ' is unzipped')
    # # 压缩文件里bb文件夹下的aa.txt
    # azip_info = azip.getinfo()
    # # 原来文件大小
    # print(azip_info.file_size)
    # # 压缩后大小
    # print(azip_info.compress_size)
    #
    # # 这样可以求得压缩率，保留小数点后两位
    # print('压缩率为{:.2f}'.format(azip_info.file_size / azip_info.compress_size))
    azip.extractall('data/')
    return unzipfn
