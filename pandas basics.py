import pandas as pd

df=pd.read_csv('E:\courses\Data science\Day_007\Salaries.csv')
dfo=pd.read_csv('E:\courses\Data science\Day_007\Salaries 1.csv')

#return df shape(rows,columns)
df.shape

#df.head() returns first 5 datas in csv file 
#we can also secefic the df.head(2) it print first two data.
df.head()
df.head(3)

#df.tail() returns last 5 datas in csv file 
#we can also secefic the df.tail(2) it print last two data.
df.tail()
df.tail(2)

#df.sample() print the random index data in csv file. return only one...
#we can also specify the return data more then one.
df.sample()
df.sample(2)# it print randomly two data in the csv file...

#if we want specific column means 
df['rank']
df['discipline']
#if we want print two colunms or more df[['columns name','columns name']]
df[['rank','discipline','phd']]

#if we want unique value in certain column
df['rank'].unique()
df['sex'].unique()

#if we want uniquely present total number 
#for example professor total number present in this collage is 56
#ex:total number of male and female present in this collage....
df['rank'].value_counts()
df['sex'].value_counts()

#if we want that total in percentage
df['rank'].value_counts(normalize='True')
df['sex'].value_counts(normalize='True')

#if we want find max salary give by the collage or min or average salary
df['salary'].max()
df['salary'].min()
df['salary'].mean()


#if we want salary greater than 1L means
df['salary'] >100000 # it just returns TRue Or False...

# if u want values means
# it will returns all rows and columns 
#but in range of greater than 1L....
df[df['salary'] >100000] 

# if u want values means
# it will returns all rows and columns 
#but in range of greater than 1L and sex=male....
df[(df['salary'] > 100000)  & (df['sex']=='Male') ]

'''
if you want to return the missing values or nan  in coloumn wise
but it return in true or false
we canot return original value
'''
df.isnull().any(axis=0)
'''
if you want to return the missing values or nan  in row wise
but it return the whole rows and columns
'''
df.isnull().any(axis=1) # it return true or false value
df[df.isnull().any(axis=1)]#it return the whole rows and columns
'''
if u want fill nan or missing values in data
we can use fillna metod in df
---fillna only used to overwrite the nan values 
if numbers are the it will not overwrite it----
'''
df.fillna(1) # it just set the vale no assing to file
df2=df.fillna(1) # it will assing the nan to 1
df3=df['phd'].fillna(df['phd'].mean())# it will assign phd nan to avg of phd value

'''
dropna is used to dro the nan value rows or delete the rows if nan is present
we want topass ths parameteres inplace = true it means nan present means 
it will delete the whole row
'''
df4=df.dropna(inplace=True)
df5=df.copy()
df5.dropna(inplace=False)

'''
iloc --->is the way to acess the dataframe with specific rows 
and rows specifid coloumns
'''
df.iloc[0:10,2:4]#[row selection,column selection]
df.iloc[10,2]
df.iloc[7,2]
df.iloc[:,2:]
df.iloc[:,:3]
df.iloc[10,:2]
df.iloc[[1,15],2] # if u want 2 rows but second column only
df.iloc[10,[0,3]]
df.iloc[[1,15],[0,3]]



















