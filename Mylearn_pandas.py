import pandas as pd
df = pd.DataFrame({"A": [12, 12, 12, None, 12], 
                   "B": [12, 12, 12, None, 12], 
                   "C": [12, 12, 12, None, 12], 
                   "D": [12, 12, 12, None, 12]})
print(df)
df.isnull()
print(df.isnull())                      ###same as isna()
print(df.isna())                        ###its return boolean true for null values
print(df.fillna(1))                     ### 1 will the value for null places
print(df.fillna(method='pad'))          ####pad is for previous row value set
print(df.fillna(method='bfill'))        ###bfill for next row will be value
print(df.fillna(value=23))              ###values set
print(df.fillna(value=23,inplace=True))   ##-----values will updated in dataframe
print(df)
print(df.replace(to_replace=3,value=250))    ##replacevalue in 3 of 250 
print(df['C'].replace(to_replace=16,value=250))    ##specific values replace in particular columns
print(df)
print(df['C'])


s=([0,1,2,None,4])
df=pd.Series(s)
print(df)
print(df.interpolate())
s=([2,4,None,8,10])
df=pd.Series(s)
print(df)
print(df.interpolate())
print(df.interpolate)          ### interpolate for autofill method ### method= linear,ffill,bfill,limitdirection='both' or 'single' ,polynamia interpolate  ####-----FILLNA   vs    INTERPOLATE difference try later today

#removing Duplicates

df.dropna()
print(df.dropna())    
print(df.drop_duplicates())
print(df.drop_duplicates(subset=['C']))

##data type view,change,delete
print(df.dtypes)      #np.nan
#astype
#datetime
df.dropna(how='any')
df['name'].str.upper   
#str.lower   
#str.strip  
#pattern matching 
#str.repeat 
#str.softcase
#str.len  
#str.count(a)









