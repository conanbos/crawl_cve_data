import json

dic=[]

def read_data(json_data):
    if isinstance(json_data, dict):
        for key in json_data.keys():
            key_value= json_data.get(key)
            if isinstance(key_value, dict):
                read_data(key_value)
            elif isinstance(key_value,list):
                for key_array in key_value:
                    if not (key in dic): dic.append(str(key))#print('now is key:', str(key))
                    read_data(key_array)
            else:
                print(str(key), '==',str(key_value))
                if not (key in dic): dic.append('++++'+str(key))



class jsonfile(object):

    def __init__(self, fn, datatype='NVD', database='test', action='read'):
        self.file = fn
        self.read_file(self.file)



    def read_file(self,fn):
        with open(fn,'r') as f:
            data = json.load(f)
            read_data(data)

        with open(fn+'_list.txt','w') as fl:
            for i in range(len(dic)):
                fl.write(dic[i]+'\n')
            fl.close()
            print('file:'+fn+'_list.txt')


