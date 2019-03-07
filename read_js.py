import json
import re
from collections import defaultdict
with open('main.6f5b9d827e678e58fdba.js') as dataFile:
    data1 = dataFile.readline()
    data2 = dataFile.readline()
    data1=data1.rstrip('\n')
    data2=data2.rstrip('\n')
#    obj = data[data.find('makes:[') : data.rfind(']')+1]

#obj=re.match(r'make:\[(.*?)\]','make:[ok]').group(1)
data1=re.sub(r',name:".*?"','',data1)
data1=re.sub(r',visibleIn:\[.*?\]','',data1)
data1=re.sub(r'label:\"','',data1)
data1=re.sub(r'\"','',data1)
data1=re.sub(r'id:','',data1)
data1=re.sub(r'makeId:','',data1)
data1=re.sub(r',aliasId:\d*','',data1)
data1=re.sub(r',mdId:\[.*?\]','',data1)
data2=re.sub(r',name:".*?"','',data2)
data2=re.sub(r',visibleIn:\[.*?\]','',data2)
data2=re.sub(r'label:\"','',data2)
data2=re.sub(r'\"','',data2)
data2=re.sub(r'id:','',data2)
data2=re.sub(r'makeId:','',data2)
data2=re.sub(r',aliasId:\d*','',data2)
data2=re.sub(r',mdId:\[.*?\]','',data2)
data1_list=data1.strip('{}').split('},{')
data1_list=[i.split(',') for i in data1_list]
data2_list=data2.strip('{}').split('},{')
data2_list=[i.split(',')[1:3] for i in data2_list]
data_dic=defaultdict(lambda: [])
for i in data2_list:
    data_dic[i[1]].append(i[0])
for i in data1_list:
    data_dic[i[1]] = data_dic.pop(i[0])

data_dic['BMW']= ['128', '135', '228', '230', 'M2', 'M 235', ' M240', '318', '320',
'323', '325', '328', '328 d', '330', '330 e', '335', '340', 'ActiveHybrid 3', 'M3', '428', '430',
'435', '440', 'M4', '525', '528', '530', '530 e',
'535', '535 d', '540', '540 d', '545', '550', 'ActiveHybrid 5', 'M5', 'M 550',
'640', '645', '650', 'ALPINA B6', 'M6',
'735', '740', '740 e', '745', '750', '760', 'ActiveHybrid 7',
'ALPINA B7', 'M 760', '840', '850', 'i3', 'i8', 'M2', 'M 235',
'M 240', 'M3', 'M4', 'M5', 'M550', 'M6', 'M 760', 'X5 M', 'X6 M', 'Z4 M', 
'X6', 'X1', 'X2', 'X3', 'X4', 'X5 eDrive', 'X5 M', 'X5', 'X6', 'X6 M', 'Z3', 'Z4', 'Z8',
'1-Series', '2-Series', '3-Series', '4-Series', '5-Series', '6-Series', '7-Series']
for i in data_dic:
    a=[]
    for j in data_dic[i]:
        j=re.sub('[^\w\s]',' ', j)
        regex=re.compile(r'(\d+)',flags=re.IGNORECASE)
        j=regex.sub(r' \1 ',j)
        j=re.sub('\s+', ' ',j)        
        j=j.strip(' ')
        a.append(j)
    data_dic[i]=a

#data_dic['BMW'].sort(key = lambda s: -len(s))
def cmp(x,y):
    if x<y: return -1
    if x==y: return0
    if x>y: return 1
#data_dic['BMW'].sort(lambda x,y: cmp(len(x), len(y)))
print(data_dic['Audi'])
