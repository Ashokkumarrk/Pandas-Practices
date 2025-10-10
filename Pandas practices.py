import pandas as pd
file={'name':["rohit","ashok","kumar"],
      'age':[23,24,25],
      'city':["chennai","madurai","cuddalore"]
}
df=pd.DataFrame(file)
print(df)


##selecting single columns
print(df['name'])
print(df["age"])

##selecting multiple columns
print(df[["name","city"]])
print(df[['name','age','city']])

##selecting rows with loc based(label based)
print(df.loc[1])
print(df.loc[0])
print(df.loc)
print(df.loc[2])

##specific rows with column
print(df.loc[1,'name'])
print(df.loc[2,'city'])
print(df.loc[0,'age'])

#--slice rows
print(df.loc[0:1])
print(df.loc[1:2])
print(df.loc[0:2])

##--multiple rows
print(df.loc[[1,2]])
print(df.loc[[0,1]])

##-------selecting rows with iloc( index-based)
print(df.iloc[1])
print(df.iloc[2])

print(df.iloc[0,1])
print(df.iloc[0,2])
print(df.iloc[0,0])
print(df.iloc[1,0])
print(df.iloc[2,0])

print(df.iloc[0:3])
print(df.iloc[1:2])
print(df.iloc[1:3])           ######-----iloc index based slice doubt.
print(df.iloc[:1])
print(df.iloc[2:])

####filtering rows(conditional selection)
print(df[df['age']<25])
print(df[df['city']=='chennai'])

##using &
print(df[(df['age']<25) & (df['city'] == 'chennai')])

#isin for multiple matches
print(df[df['city'].isin(['chennai','cuddalore'])])    ####isna,isnull not used

##using not null
print(df[df['city'].notnull()])   ##without null values rows and columns only shows

#data cleaning ---isnull,dropna,fillna,fillwithmean
print(df.isnull())
print (df.isnull().sum())    ##for count the missing values
print(df.dropna())
print(df.fillna({"age" : 0,'city':'unknown'}) )         ##--for fill custom values inplace of missing values
print(df['age'].fillna(df['age'].mean(),inplace = True))












