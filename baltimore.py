# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 08:41:34 2021

@author: Inbat
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
df=pd.read_csv('E:\courses\Data science\Day_010\Baltimore.csv')

str_salary=df['AnnualSalary'].astype(str)
df['AnnualSalary']=str_salary.apply(lambda x:x.replace("$",""))
df['AnnualSalary']=df['AnnualSalary'].astype(float)
grouped=df.groupby(['JobTitle'])['AnnualSalary']

aggre=grouped.agg([np.sum,np.mean])

df["JobTitle"].value_counts()[0:11].plot(kind='bar')

k=df[['Agency','AgencyID']]
k.drop_duplicates(inplace=True)
print(k)

missinng=df['GrossPay'].isnull()
l=missinng.value_counts()[1]
print(l)