'''
dic1={}
list1=[]
m=int(input('Enter the entries:'))
for i in range(m):
    key=input('Enter key:')
    value=int(input('Enter value:'))
    dic1[key]=value
    list1.append(key)
for i in dic1.keys():
   print(list1.count(i))
   if list1.count(i) ==1:
       print(i," ",dic1[i]*1)
   if list1.count(i) ==2:
       print(i," ",dic1[i]*2)
   if list1.count(i) ==3:
       print(i," ",dic1[i]*3)
   if list1.count(i) ==4 :
       print(i," ",dic1[i]*4)
       '''






from collections import OrderedDict






number_ = int(input())
odict = OrderedDict()
for i in range(number_):
    litem = input().split(' ')
    price = int(litem[-1])
    item_name = " ".join(litem[:-1])
    if odict.get(item_name):
        odict[item_name] += price
    else:
        odict[item_name] = price

for i,v in odict.items():
    print(i,v)
