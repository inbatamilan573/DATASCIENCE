# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:42:28 2021

@author: Inbat
"""

import numpy as np
list1=[1,2,3,4,5,6,7,8,9]
k=np.array(list1)
m=np.ones([3,4])
np.zeros((5,5))

import matplotlib.pyplot as plt

x=('CSE','ECE','IT','EEE')
size=[10,5,5,3]
apart=[0,0,0.1,0]

plt.pie(size,labels=x,explode=apart,autopct='%0.1f%%')

#p.scatter(x,y)
#p.plot(x,y) autopct='%1.1f%%'
plt.show()