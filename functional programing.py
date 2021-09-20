list2=[1,2,3,4,5]
list1=[]
print("___________FOR LOOP METHOD:____________\n")
for i in list2:
    list1.append(i%2 == 0)
print(list1,"\n")   


def square(x):
    return x%2 == 0

k=map(square,list2)
type_cast_of_k = list(map(square,list2))
print("_____________USING MAP FUNCTION:-_____________\n")
print("Going to print map function it give only Object Adress:\n")
print(k,"\n")
print("Using Typecast List() then it print values inside it.\n")
print(type_cast_of_k,"\n")


fil=filter(square,list2)
print("___________USING FILTER FUNCTION:-____________\n")
print("Going to print Filter function it give only Object Adress:\n")
print(fil,"\n")
print("Using Typecast List() then it print values inside it and it only return TRUE values.\n")
print(list(fil),"\n")


lam=filter(lambda x:x%2 == 0,list2)
lam1=map(lambda x:x%2 == 0,list2)
print("___________USING LAMBDA FUNCTION:-Only used inside(Map,Filter)____________\n")
print("Going to print Filter Or Map function it give only Object Adress:\n")
print(lam,"Using Filter with lambda...\n")
print(lam1,"Using Map with lambda...\n")
print("Using Typecast List() then it print values inside it and it only return TRUE values in filter and all values in map.\n")
print("Filter with lambda -->",list(lam),"\n")
print("Map with lambda -->",list(lam1),"\n")

print("_________________________________________________________________\n")
import functools
def reduce(x,y):
    return x+y


print("Using reduce ---------\n",
      functools.reduce(reduce, list2))
"""
iteration 1 --> 1+2 return 3
iteration 2 --> 3+3 return 6
iteration 3 --> 6+4 return 10
iteration 4 --> 10+5 return 15

finally returns 15.




"""
print("------------------Lambda using If statement.....------------------------\n")
lam3=map(lambda x:x+x if x%2 == 0 else x,list2)
print(list(lam3))

print(str(fil),"\n")



























