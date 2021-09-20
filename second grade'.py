list1=[['Harry', 37.2], ['Berry', 37.2], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 
k=[]
for i in range(len(list1)):
    for j in range(0,2):
      k.append(list1[i][1])
      print(k)
k.sort()
print(k)  
min1=k[1]
#print(min1)
for i in range(len(k)):
    if k[i] != min1:
        se=k[i]
        break
m=[]
for i in range(len(list1)):
    if list1[i][1] == se:
        m.append((list1[i][0]))
m.sort()
print(m)