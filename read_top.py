import json
import re
from collections import defaultdict
with open('top_firstused.txt') as dataFile:
    mlist=[]
    for i in dataFile:   
        i=i.rstrip('\n')
        mlist.append(i)

#data_dic['BMW'].sort(key = lambda s: -len(s))
def cmp(x,y):
    if x<y: return -1
    if x==y: return0
    if x>y: return 1
#data_dic['BMW'].sort(lambda x,y: cmp(len(x), len(y)))
print(mlist)
