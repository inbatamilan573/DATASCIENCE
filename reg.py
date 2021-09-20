import re
k=open("E:\courses\Data science\Day_005\simpsons_phone_book.txt",'r')
for i in k:
    if re.search('J\w+\WNeu\W\d{3}\W\d{4}',i):
        print(i)
