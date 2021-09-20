list=[]
t=True
print('What Should we pick up  at the store?') 
print("Enter 'DONE' to stop adding items.")
while t:
    k=input("ADD Item:")
    if k == "DONE":
        print("\n")
        t=False
        
    else:
        list.append(k) 
print("Here's your products: \n")
for i in list:
     print(i)