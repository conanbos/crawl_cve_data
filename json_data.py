import json
import sqlite_db
import pandas as pd
# from pandas import DataFrame


dic=[]
dic1=[]
counter=0
nvd_key=['CVE_data_type', 'CVE_data_format', 'CVE_data_version','CVE_data_numberOfCVEs', 'CVE_data_timestamp',
         'data_type', 'data_format', 'data_version', 'ID', 'ASSIGNER']
nvd_value=[]
# CVE_data_type='CVE', CVE_data_format='MITRE', CVE_data_version='4.0',
#               CVE_data_numberOfCVEs='', CVE_data_timestamp='', data_type='CVE',
#               data_format='MITRE',data_version='4.0',CVE_data_meta_ID='',CVE_data_meta_ASSIGNER='',
#               problemtypeTid='',referencesTid='', descriptionTid='', configrationTid='',impactTid=''




jsonss="""{
  "CVE_data_type" : "CVE",
  "CVE_data_format" : "MITRE",
  "CVE_data_version" : "4.0",
  "CVE_data_numberOfCVEs" : "18241",
  "CVE_data_timestamp" : "2021-09-18T07:00Z",
  "CVE_Items" : [ {
    "cve" : {
      "data_type" : "CVE",
      "data_format" : "MITRE",
      "data_version" : "4.0",
      "CVE_data_meta" : {
        "ID" : "CVE-2020-0001",
        "ASSIGNER" : "security@android.com"
      },
      "problemtype" : {
        "problemtype_data" : [ {
          "description" : [ {
            "lang" : "en",
            "value" : "NVD-CWE-noinfo"
          } ]
        } ]
      }
    }
 }"""





def table_nvd(nvd_data):
     sqlite_db.VData.insert_data('NVD.db',nvd_data)


def read_data(jsondata_array):
    global counter
    global dic
    if isinstance(jsondata_array, dict):
        for key in jsondata_array.keys():
            key_value = jsondata_array.get(key)
            if isinstance(key_value, dict):
                read_data(key_value)
            elif isinstance(key_value, list):
                # if not (key in dic): dic.append(str(key))
                for key_array in key_value:
                    # if not (key in dic): dic.append(str(key))#print('now is key:', str(key))
                    read_data(key_array)
            else:
                if key in nvd_key:
                    nvd_value.append(str(key_value))
                    print(str(key), '==',str(key_value))
                counter += 1



                #
                # key_value = jsondata_array.get(key)
                # if isinstance(key_value, list):
                #     # if not (key in dic): dic.append(str(key))
                #     for key_array in key_value:
                #         # if not (key in dic): dic.append(str(key))#print('now is key:', str(key))
                #         dic1.append(str(key))
                #         read_data(key_array)
                # else:
                #     print(str(key), '==',str(key_value))
                #     if not (key in dic): dic.append(str(key))
                #     counter += 1




class jsonfile(object):

    def __init__(self, fn, datatype='NVD', database='test', action='read'):
        self.file = fn
        self.read_file(self.file)
        # self.read_json(self.file)
        global counter
        counter=0

    def read_json(self,fn):
        dataset=self.read_file(fn)
        siblings = pd.DataFrame()



    def read_file(self, fn):
        sqls=''
        CVE_num=''
        with open(fn,'r') as f:
            data = json.load(f)
            read_data(data)
            f.close()

        # dataset=pd.read_json(fn)
        # ds=pd.DataFrame(data['CVE_Items'],columns=['lang'])
        # print(ds)
        # return data


            # CVE_num=nvd_value[-3]
            # for i in range(len(nvd_key)):
            #     sql = "'"+nvd_value[i]+"',"
            #     sqls +=sql
            #
            # sqlite_db.VData('NVD.db')
            # sqls = sqls+"'"+CVE_num+"','"+CVE_num+"','"+CVE_num+"','"+CVE_num+"'"
            # print(sqls)
            # sqlite_db.VData.insert_data('NVD', sqls)
            # sqlite_db.VData.disconnect()




        # with open(fn+'_list.txt','w') as fl:
        #     for i in range(len(dic)):
        #         fl.write(dic[i]+'\n')
        #     fl.close()
        #     print('file:'+fn+'_list.txt')
        # print('%(fn)s:total items %(counter)d:' % {'fn':fn,'counter':counter})







    # if isinstance(jsondata_array, dict):
    #     for key in jsondata_array.keys():
    #         key_value = jsondata_array.get(key)
    #         if isinstance(key_value, dict):
    #             read_data(key_value)
    #         elif isinstance(key_value, list):
    #             if not (key in dic): dic.append(str(key))
    #             for key_array in key_value:
    #                 # if not (key in dic): dic.append(str(key))#print('now is key:', str(key))
    #                 dic1.append(str(key))
    #                 read_data(key_array)
    #         else:
    #             # print(str(key), '==',str(key_value))
    #             if not (key in dic): dic.append(str(key))
    #             counter += 1