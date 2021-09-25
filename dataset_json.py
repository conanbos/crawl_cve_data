
import json
import sqlite_db as db


keys=[]
head=[]
cve=[]
conf=[]
cve_id=""
cve_sum="0"


def get_conf(cve_item):
    pass

def get_cve(cve_item):
    global cve
    global cve_id
    global head
    cve=[]
    cve_id=""
    cveids=[]

    for key in cve_item.keys():
        key_value=cve_item.get(key)

        if key=="CVE_data_meta":
            for keymeta in key_value.keys():
                keymeta_value=key_value.get(keymeta)
                cve.append(keymeta_value)
                if keymeta=="ID":
                    cve_id=keymeta_value
                    for i in range(5):
                        cveids.append(cve_id)
                    var_meta=head+cveids
                    sql = "INSERT INTO nvd VALUES (?,?,?,?,?,?,?,?,?,?)"  # 合成NVD表所有字段
                    db.VData.insert_data(sql, var_meta)
            if len(key_value)==1:cve.append("") #防止有缺少字段的情况
        elif key=="problemtype":
            pt=[]
            pt.clear()
            key_temp_value = key_value.get("problemtype_data")
            if isinstance(key_temp_value,list):
                for i in range(len(key_temp_value)):
                    key_temps_value=key_temp_value[i]
                    if isinstance(key_temps_value,dict):
                        for keytemp in key_temps_value.keys():
                            if keytemp=="description":
                                keytemp_value=key_temps_value.get(keytemp)

                                for i in range(len(keytemp_value)):
                                    for keylang in keytemp_value[i].keys():
                                        pt.append(keytemp_value[i].get(keylang))
                                    sql = "INSERT INTO problemtype VALUES (?,?,?)"
                                    pt.insert(0,cve_id)
                                    db.VData.insert_data(sql, pt)
                                    pt.clear()

        elif key=="references":
            refs=[]
            key_ref_value = key_value.get("reference_data")
            for i in range(len(key_ref_value)):
                ref_value=key_ref_value[i]
                for ref_key in ref_value.keys():
                    if ref_key=="tags":
                        tags=''
                        if not (len(ref_value.get(ref_key)) == 0):
                            ref_tags=ref_value.get(ref_key)
                            for x in range(len(ref_tags)):
                                if x==0:
                                    tags += ref_tags[x]
                                else:
                                    tags  = tags+','+ref_tags[x]
                        refs.append(tags)
                    else:
                        refs.append(ref_value.get(ref_key))
                refs.insert(0,cve_id)
                sql = "INSERT INTO refs VALUES (?,?,?,?,?)"
                db.VData.insert_data(sql, refs)
                refs.clear()

        elif key=="description":
            des = []
            des.clear()
            key_temp_value = key_value.get("description_data")
            if isinstance(key_temp_value, list):
                for i in range(len(key_temp_value)):
                    key_des_value = key_temp_value[i]
                    if isinstance(key_des_value, dict):
                        for keydes in key_des_value.keys():
                            des.append(key_des_value.get(keydes))
                        sql = "INSERT INTO description VALUES (?,?,?)"
                        des.insert(0, cve_id)
                        db.VData.insert_data(sql, des)
                        des.clear()
        else:
            cve.append(key_value)





def get_items(items):
    global cve
    count=1
    for i in range(len(items)):
        item_value = items[i]
        if isinstance(item_value,dict):
            for key in item_value.keys():
                key_value=item_value.get(key)
                if key=="cve":
                    get_cve(key_value)
                elif key=="configurations":
                    pass
                elif key=="impact":
                    pass
                elif key=="publishedDate":
                    cve.append(key_value)
                elif key == "lastModifiedDate":
                    cve.append(key_value)
                else:
                    pass
            sql = "INSERT INTO cve VALUES (?,?,?,?,?,?,?)"  # 合成CVE表所有字段
            db.VData.insert_data(sql, cve)
        print('\r'+str(count)+'/'+cve_sum,end="")
        count +=1
        # if count==6104:
        #     print("6104")






def get_head(jsondata):
    global head
    global cve_sum
    head=[]
    cve_sum="0"
    for key in jsondata.keys():
        key_value = jsondata.get(key)
        # keys.append(key)
        if key=="CVE_data_numberOfCVEs":cve_sum=key_value
        if not isinstance(key_value,list):
            head.append(key_value)
    db.VData("NVD.db")

    # db.VData.disconnect(db)

    get_items(key_value)

    db.VData.disconnect()




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
                # if key in nvd_key:
                #     nvd_value.append(str(key_value))
                print(str(key), '==',str(key_value))
                counter += 1


def read_file(fn):
    global head
    sqls=''
    CVE_num=''
    with open(fn,'r') as f:
        data = json.load(f)
        data=get_head(data)
