import json
import re
from collections import defaultdict
with open('top_firstused.txt') as dataFile:
    mlist=[]
    for i in dataFile:   
        i=i.rstrip('\n')
        mlist.append(i)
    a=[]

    for j in mlist:
        j=re.sub('[^\w\s]',' ', j)
        
        regex=re.compile(r'(\d+)',flags=re.IGNORECASE)
        j=regex.sub(r' \1 ',j)
        j=re.sub('\s+', ' ',j)        
        j=j.strip(' ')
        a.append(j)
#data_dic['BMW'].sort(key = lambda s: -len(s))
def cmp(x,y):
    if x<y: return -1
    if x==y: return0
    if x>y: return 1
#data_dic['BMW'].sort(lambda x,y: cmp(len(x), len(y)))
print(a)
