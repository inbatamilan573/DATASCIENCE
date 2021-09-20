import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
df=pd.read_csv('E:\courses\Data science\Day_010\Automobile.csv')

df['price']=df['price'].fillna(int(df['price'].mean()))

k=df['price'].values
#x=np.ndarray(df['price'])
#x=x.reshape(102,102)
x=df['price'].max()
y=df['price'].min()
z=df['price'].mean()
w=df['price'].std()
print("Maximum price: ",x)
print("Minimum price: ",y)
print("Average price: ",round(z,2))
print("Standard price: ",round(w,2))

branches=df['make'].unique()
m=list(df['make'].value_counts())
sizes=m
pt.pie(sizes,labels=branches,autopct='%.1f%%')

pt.show()


branches10=df['make'].unique()[0:11]
m1=list(df['make'].value_counts()[0:11])
sizes1=m1
pt.pie(sizes1,labels=branches10,autopct='%.1f%%')
pt.show()


branches1=df['make'].value_counts().index[0:11]
m0=df['make'].value_counts().values[0:11]
sizes0=m1
pt.pie(sizes0,labels=branches1,autopct='%.1f%%')
pt.show()