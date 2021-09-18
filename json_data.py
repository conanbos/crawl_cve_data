import json
import sqlite_db

dic=[]
counter=0

def table_nvd(CVE_data_type='CVE', CVE_data_format='MITRE', CVE_data_version='4.0',
              CVE_data_numberOfCVEs='', CVE_data_timestamp='', data_type='CVE',
              data_format='MITRE',data_version='4.0',CVE_data_meta_ID='',CVE_data_meta_ASSIGNER='',
              problemtypeTid='',referencesTid='', descriptionTid='', configrationTid='',impactTid=''):
    sqlite_db.VData.insert_data('NVD',nvd_data)


def read_data(jsondata_array):
    global counter
    global dic
    if isinstance(jsondata_array, dict):
        for key in jsondata_array.keys():
            key_value = jsondata_array.get(key)
            if isinstance(key_value, dict):
                read_data(key_value)
            elif isinstance(key_value, list):
                if not (key in dic): dic.append(str(key))
                for key_array in key_value:
                    # if not (key in dic): dic.append(str(key))#print('now is key:', str(key))
                    read_data(key_array)
            else:
                # print(str(key), '==',str(key_value))
                if not (key in dic): dic.append(str(key))
                counter += 1




class jsonfile(object):

    def __init__(self, fn, datatype='NVD', database='test', action='read'):
        self.file = fn
        self.read_file(self.file)
        global counter
        counter=0



    def read_file(self,fn):
        with open(fn,'r') as f:
            data = json.load(f)
            read_data(data)
            f.close()

        with open(fn+'_list.txt','w') as fl:
            for i in range(len(dic)):
                fl.write(dic[i]+'\n')
            fl.close()
            print('file:'+fn+'_list.txt')
        print('%(fn)s:total items %(counter)d:' % {'fn':fn,'counter':counter})




