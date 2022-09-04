#-*-codeing=utf-8 -*-
#@Time :2021/12/30 20:22
#@Author :Csn
#@File:__init__.py
#@Software:PyCharm
from pprint import pprint
import json
import pandas as pd
import requests
url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers={
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"
}
dict_id=[]
for i in range(1,300):
    data_first={
        "on": "true",
        "page": i,
        "pageSize": 15,
        "productName": "",
        "conditionType": 1,
        "applyname": "",
        "applysn": "",
    }

    try:
        # respose=requests.post(url=url,data=data_first,headers=headers,timeout=3)
        respose = requests.post(url=url, data=data_first, headers=headers)
        if respose.content:
            data=respose.json()
            all_id = data['list']
    except:
        print(1)
    #pageCount=respose['pageCount']


    #print(pageCount)

    for id in all_id:
        i=id['ID']
        dict_id.append(i)
    #print(i)
#pprint(respose)
#print(dict_id)

url_list='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

Cosmetics=[]

for id in dict_id:
    #print(id)
    data_drug = {}
    data_list = {
        "id": id,
    }
    respose_list=requests.post(url=url_list,headers=headers,data=data_list).json()
    data_drug["company_name"]=respose_list['epsName']
    data_drug["license"]=respose_list['productSn']
    data_drug["items"]=respose_list['certStr']
    data_drug["home"]=respose_list['epsAddress']
    data_drug["businessPerson"]= respose_list['businessPerson']
    data_drug["epsProductAddress"]= respose_list['epsProductAddress']
    data_drug["businessLicenseNumber"]= respose_list['businessLicenseNumber']
    data_drug["businessPerson"]=respose_list['businessPerson']
    data_drug["legalPerson"]= respose_list['legalPerson']
    data_drug["qfManagerName"]= respose_list['qfManagerName']
    data_drug["qualityPerson"]= respose_list['qualityPerson']
    data_drug["rcManagerDepartName"]= respose_list['rcManagerDepartName']
    data_drug["rcManagerUser"]= respose_list['rcManagerUser']
    data_drug["xkDate"]= respose_list['xkDate']
    data_drug["xkDateStr"]= respose_list['xkDateStr']
    data_drug["xkName"]= respose_list['xkName']
    #print(data_drug)
    Cosmetics.append(data_drug)

#print(Cosmetics)
hzp=pd.DataFrame(Cosmetics)
# hzp.to_csv('化妆品.csv',encoding='utf_8_sig')
hzp.to_excel('化妆品.xlsx')