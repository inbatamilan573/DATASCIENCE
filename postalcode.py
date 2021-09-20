import re
dic={}
l=open('E:\courses\Data science\Day_005\largest_cities_germany.txt')
pattern = re.compile('\s[\w\s]+\s')
m=l.readlines()
cities=[]
for i in m:
    name=pattern.findall(i)[0]
    cities.append(name.strip())
 
p=open('E:\courses\Data science\Day_005\postal_codes_germany.txt','r')
e=p.read()
#ps=[]
pattern1 = re.compile('\s\d+\s')
for i in cities:
    #print(i)
    exp='\s'+i+'\s[\d]+\s'
    code=re.findall(exp,e)[0:3]
   # ps.append(code)
    code_one="".join(code)
    num=re.findall('\d+',code_one)
    dic[i]=re.findall('\d+',code_one)
    
p.close()
l.close()                   