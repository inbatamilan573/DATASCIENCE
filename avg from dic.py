# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:55:06 2021

@author: Inbat
"""
dic={'Krishna':[67,68,69],'Arjun':[ 70,98,63],
'Malika':[52,56,60]}
k=len(dic['Malika'])
m=0
for i in dic['Malika']:
   m=m+i
print(format(m/k,'.2f'))