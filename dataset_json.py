
import json
import sqlite_db as db
import prbar

prbar.ProgressBar(0, fmt=prbar.ProgressBar.DB)

keys=[]
head=[]
cve=[]
conf=[]
cve_id=""
cve_sum=0

def get_cpe(cpe_str):
    cpe_chain=cpe_str.split(":")[1:13]#去除第一个"cpe"，保证长度在12
    return cpe_chain

def get_impact(cve_item):
    global cve_id
    impatc=[]
    v3_version=""
    v3_vectorString=""
    v3_attackVector=""
    v3_attackComplexity=""
    v3_privilegesRequired=""
    v3_userInteraction=""
    v3_scope=""
    v3_confidentialityImpact=""
    v3_integrityImpact=""
    v3_availabilityImpact=""
    v3_baseScore=""
    v3_baseSeverity=""
    v3_exploitabilityScore=""
    v3_impactScore=""
    v2_version=""
    v2_vectorString=""
    v2_accessVector=""
    v2_accessComplexity=""
    v2_authentication=""
    v2_confidentialityImpact=""
    v2_integrityImpact=""
    v2_availabilityImpact=""
    v2_baseScore=""
    v2_severity=""
    v2_exploitabilityScore=""
    v2_impactScore=""
    v2_acInsufInfo=""
    v2_obtainAllPrivilege=""
    v2_obtainUserPrivilege=""
    v2_obtainOtherPrivilege=""
    v2_userInteractionRequired=""

    for key in cve_item.keys():
        key_value = cve_item.get(key)
        if key=="baseMetricV3":
            # kv_value = key_value.get(key)
            for key_v3 in key_value.keys():
                k3_value=key_value.get(key_v3)
                if key_v3=="cvssV3":
                    for k3_cvss in k3_value.keys():
                        k3_cvss_value=k3_value.get(k3_cvss)
                        if k3_cvss=="version":
                            v3_version = k3_cvss_value
                        if k3_cvss == "vectorString":
                            v3_vectorString = k3_cvss_value
                        if k3_cvss == "attackVector":
                            v3_attackVector = k3_cvss_value
                        if k3_cvss == "attackComplexity":
                            v3_attackComplexity = k3_cvss_value
                        if k3_cvss == "privilegesRequired":
                            v3_privilegesRequired = k3_cvss_value
                        if k3_cvss == "userInteraction":
                            v3_userInteraction = k3_cvss_value
                        if k3_cvss == "scope":
                            v3_scope = k3_cvss_value
                        if k3_cvss == "confidentialityImpact":
                            v3_confidentialityImpact = k3_cvss_value
                        if k3_cvss == "integrityImpact":
                            v3_integrityImpact = k3_cvss_value
                        if k3_cvss == "availabilityImpact":
                            v3_availabilityImpact = k3_cvss_value
                        if k3_cvss == "baseScore":
                            v3_baseScore = k3_cvss_value
                        if k3_cvss == "baseSeverity":
                            v3_baseSeverity = k3_cvss_value
                if key_v3 == "exploitabilityScore":
                    v3_exploitabilityScore = k3_value
                if key_v3 == "impactScore":
                    v3_impactScore = k3_value
        if key=="baseMetricV2":
            for key_v2 in key_value.keys():
                k2_value = key_value.get(key_v2)
                if key_v2 == "cvssV2":
                    for k2_cvss in k2_value.keys():
                        k2_cvss_value = k2_value.get(k2_cvss)
                        if k2_cvss == "version":
                            v2_version = k2_cvss_value
                        if k2_cvss == "vectorString":
                            v2_vectorString=k2_cvss_value
                        if k2_cvss == "accessVector":
                            v2_accessVector=k2_cvss_value
                        if k2_cvss == "accessComplexity":
                            v2_accessComplexity=k2_cvss_value
                        if k2_cvss == "authentication":
                            v2_authentication=k2_cvss_value
                        if k2_cvss == "confidentialityImpact":
                            v2_confidentialityImpact=k2_cvss_value
                        if k2_cvss == "integrityImpact":
                            v2_integrityImpact=k2_cvss_value
                        if k2_cvss == "availabilityImpact":
                            v2_availabilityImpact=k2_cvss_value
                        if k2_cvss == "baseScore":
                            v2_baseScore=k2_cvss_value
                if key_v2 == "severity":
                    v2_severity=k2_value
                if key_v2 == "exploitabilityScore":
                    v2_exploitabilityScore=k2_value
                if key_v2 == "impactScore":
                    v2_impactScore=k2_value
                if key_v2 == "acInsufInfo":
                    v2_acInsufInfo=k2_value
                if key_v2 == "obtainAllPrivilege":
                    v2_obtainAllPrivilege=k2_value
                if key_v2 == "obtainUserPrivilege":
                    v2_obtainUserPrivilege=k2_value
                if key_v2 == "obtainOtherPrivilege":
                    v2_obtainOtherPrivilege=k2_value
                if key_v2 == "userInteractionRequired":
                    v2_userInteractionRequired=k2_value

    impatc.append(cve_id)
    impatc.append(v3_version)
    impatc.append(v3_vectorString)
    impatc.append(v3_attackVector)
    impatc.append(v3_attackComplexity)
    impatc.append(v3_privilegesRequired)
    impatc.append(v3_userInteraction)
    impatc.append(v3_scope)
    impatc.append(v3_confidentialityImpact)
    impatc.append(v3_integrityImpact)
    impatc.append(v3_availabilityImpact)
    impatc.append(v3_baseScore)
    impatc.append(v3_baseSeverity)
    impatc.append(v3_exploitabilityScore)
    impatc.append(v3_impactScore)
    impatc.append(v2_version)
    impatc.append(v2_vectorString)
    impatc.append(v2_accessVector)
    impatc.append(v2_accessComplexity)
    impatc.append(v2_authentication)
    impatc.append(v2_confidentialityImpact)
    impatc.append(v2_integrityImpact)
    impatc.append(v2_availabilityImpact)
    impatc.append(v2_baseScore)
    impatc.append(v2_severity)
    impatc.append(v2_exploitabilityScore)
    impatc.append(v2_impactScore)
    impatc.append(v2_acInsufInfo)
    impatc.append(v2_obtainAllPrivilege)
    impatc.append(v2_obtainUserPrivilege)
    impatc.append(v2_obtainOtherPrivilege)
    impatc.append(v2_userInteractionRequired)
    sql = "INSERT INTO impact VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    db.VData.insert_data(sql, impatc)
    impatc.clear()


def get_conf(cve_item):
    global conf
    global cve_id
    conf.clear()
    confs=[]
    confs_t = []
    conf.append(cve_id)
    op=""
    for key in cve_item.keys():
        key_value=cve_item.get(key)
        if key=="CVE_data_version":
            conf.append(key_value)
        elif key=="nodes":
            confs_t.clear()
            confs_t.append(0)
            for i in range(len(key_value)):
                key_conf_value=key_value[i]
                for key_conf in key_conf_value.keys():
                    if key_conf=="operator":
                        op=key_conf_value.get(key_conf)
                        if len(confs_t)<2:
                            confs_t.append(op)
                        else:confs_t[1]=op
                    elif key_conf=="children":#完成二级节点
                        conf_child_value=key_conf_value.get(key_conf)
                        confs_t[0]=1
                        for x in range(len(conf_child_value)):
                            c_match_value=conf_child_value[x]
                            for c_match_key in c_match_value:
                                if c_match_key == "operator": confs_t[1]=c_match_value.get(c_match_key)
                                if c_match_key=="cpe_match":
                                    cc_match_value=c_match_value.get(c_match_key)
                                    for w in range(len(cc_match_value)):
                                        arr_match_value=cc_match_value[w]
                                        name = ""
                                        vstart = ""
                                        vend = ""
                                        vse=""
                                        vee=""
                                        for arr_match_key in arr_match_value:
                                            if arr_match_key=="cpe_name":
                                                arr_match_name=arr_match_value.get(arr_match_key)
                                                for y in range(len(arr_match_name)):
                                                    if y==0:
                                                        name=c_match_name[y]
                                                    else:
                                                        name=name+","+arr_match_name[y]
                                            elif arr_match_key=="cpe23Uri":#处理cpe uri 信息
                                                cpeUri=arr_match_value.get(arr_match_key)
                                                confs.append(cpeUri)
                                                cpeInfo=get_cpe(cpeUri)
                                            elif arr_match_key=="versionStartIncluding":
                                                vstart=arr_match_value.get(arr_match_key)
                                            elif arr_match_key=="versionEndIncluding":
                                                vend=arr_match_value.get(arr_match_key)
                                            elif arr_match_key=="versionEndExcluding":
                                                vee=arr_match_value.get(arr_match_key)
                                            elif arr_match_key == "versionStartExcluding":
                                                vse = arr_match_value.get(arr_match_key)
                                            else:
                                                confs.append(arr_match_value.get(arr_match_key))
                                        confs.append(name)
                                        confs.append(vstart)
                                        confs.append(vend)
                                        confs.append(vse)
                                        confs.append(vee)
                                        sql="INSERT INTO configuration VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                                        db.VData.insert_data(sql, conf+confs_t+confs+cpeInfo)
                                        confs.clear()
                    elif key_conf=="cpe_match":#完成一级节点
                        confs_t[1] = op #  恢复一级节点operator
                        confs_t[0] = 0
                        cpe_value=key_conf_value.get(key_conf)
                        for x in range(len(cpe_value)):
                            match_value=cpe_value[x]
                            name = ""
                            vstart = ""
                            vend = ""
                            vse = ""
                            vee = ""
                            for key_match in match_value.keys():
                                if key_match=="cpe_name":
                                    match_name=match_value.get(key_match)
                                    for y in range(len(match_name)):
                                        if y==0:
                                            name=match_name[y]
                                        else:
                                            name=name+","+match_name[y]
                                elif key_match == "cpe23Uri":  # 处理cpe uri 信息
                                    cpeUri = match_value.get(key_match)
                                    confs.append(cpeUri)
                                    cpeInfo = get_cpe(cpeUri)
                                elif key_match == "versionStartIncluding":
                                    vstart = match_value.get(key_match)
                                elif key_match == "versionEndIncluding":
                                    vend = match_value.get(key_match)
                                elif key_match == "versionStartExcluding":
                                    vse = match_value.get(key_match)
                                elif key_match == "versionEndExcluding":
                                    vee = match_value.get(key_match)
                                else:
                                    confs.append(match_value.get(key_match))
                            confs.append(name)
                            confs.append(vstart)
                            confs.append(vend)
                            confs.append(vse)
                            confs.append(vee)
                            sql="INSERT INTO configuration VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                            db.VData.insert_data(sql, conf+confs_t+confs+cpeInfo)
                            confs.clear()


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
    global progress
    # count = 1
    for i in range(len(items)):
        item_value = items[i]
        if isinstance(item_value,dict):
            for key in item_value.keys():
                key_value=item_value.get(key)
                if key=="cve":
                    get_cve(key_value)
                elif key=="configurations":
                    get_conf(key_value)
                elif key=="impact":
                    get_impact(key_value)
                elif key=="publishedDate":
                    cve.append(key_value)
                elif key == "lastModifiedDate":
                    cve.append(key_value)
                else:
                    pass
            sql = "INSERT INTO cve VALUES (?,?,?,?,?,?,?)"  # 合成CVE表所有字段
            db.VData.insert_data(sql, cve)
        # print('\r'+str(count)+'/'+cve_sum,end="")
        # count +=1
        progress.current +=1
        progress()  # 更新进度条



def get_head(jsondata):
    global head
    global cve_sum
    head=[]
    cve_sum=0
    for key in jsondata.keys():
        key_value = jsondata.get(key)
        # keys.append(key)
        if key=="CVE_data_numberOfCVEs":cve_sum = key_value
        if not isinstance(key_value,list):
            head.append(key_value)
    progress.total = int(cve_sum)
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
    global progress
    progress = prbar.ProgressBar(0, fmt=prbar.ProgressBar.DB)
    progress.msg = fn
    with open(fn,'r') as f:
        data = json.load(f)
        get_head(data)
    progress.done()  # 结束进度条
