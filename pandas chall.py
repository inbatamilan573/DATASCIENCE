import pandas as pd
import functools as f
df = pd.read_csv(r'E:\courses\Data science\Day_010\titanic.csv')
df['Survived'].isnull()
m =list(df['Survived'])
Survived=m.count(1)
deth=m.count(0)

        


s_per=df['Survived'].mean()


male_su=list((df['Sex'] == 'male') & (df['Survived']==1))

malesurvived=male_su.count(True)
malepassed=male_su.count(False)

malegain=(malesurvived/(malepassed+malesurvived))*100
malepass=(malepassed/(malepassed+malesurvived))*100

female_su=list((df['Sex'] == 'female') & (df['Survived']==1))

femalesurvived=female_su.count(True)
femalepassed=female_su.count(False)

femalegain=(femalesurvived/(femalepassed+femalesurvived))*100
femalepass=(femalepassed/(femalepassed+femalesurvived))*100

df1=pd.read_csv(r'E:\courses\Data science\Day_010\titanic.csv')
df1['Age']=df1['Age'].fillna(int(df['Age'].mean()))
child_sur=list((df1['Age'] < 12)  & (df1['Survived']==1)) 
child_su=child_sur.count(True)
child_passed=list((df1['Age'] < 12)  & (df1['Survived']==0))
child_pas=child_passed.count(True)
child_per=(child_su/(child_su + child_pas))*100

print(round(Survived,2),"People Survived")
print(round(deth,2),"People deth")
print(round(s_per*100,2),"% People Survived")
print(round(100 -(s_per*100),2) ,"% People deth")
print("male_survived: ",round(malegain,2),"%")
print("male_deth: ",round(malepass,2),"%")
print("female_survived: ",round(femalegain,2),"%")
print("female_deth: ",round(femalepass,2),"%")
print("child_survived: ",round(child_per,2),"%")
print("\n")

print("my mis take value_counts =value_count i canot knew how to takethe value by index")

print("\n")
print("\n")



#####################################

p_survied=df['Survived'].value_counts()[1]
print(round(p_survied,2),"People Survived")
p_deth=df['Survived'].value_counts()[0]
print(round(p_deth,2),"People Deth")
p_survied_per=df['Survived'].value_counts(normalize='True')[1]
print(round(p_survied_per*100,2),"% People Survived")
p_deth_per=df['Survived'].value_counts(normalize='True')[0]
print(round(p_deth_per*100,2),"% People Deth")
m_survied=(df['Survived'][df['Sex']=='male']).value_counts(normalize='True')[1]
m_deth=(df['Survived'][df['Sex']=='male']).value_counts(normalize='True')[0]
print(round(m_survied*100,2),"% Male Survived")
print(round(m_deth*100,2),"% Male deth")
f_survied=(df['Survived'][df['Sex']=='female']).value_counts(normalize='True')[1]
f_deth=(df['Survived'][df['Sex']=='female']).value_counts(normalize='True')[0]
print(round(f_survied*100,2),"% Female Survived")
print(round(f_deth*100,2),"% Female deth")


c_survied=(df['Survived'][df['Age'] < 12]).value_counts(normalize='True')[1]

print(round(c_survied*100,2),"% Male Survived")
