import pandas as pd
df=pd.read_csv("C:/Users/ashok/OneDrive/Pictures/ipl_matches_data.csv")

### Datainspect and Cleaning:

print(df)
print(df.columns)
print(df.head(10))
print(df.tail())
print(df.describe())
print(df.info())
print(df.shape)
print(df.size)
print(df.isnull().sum())    ####count of empty values
print(df[df.isnull().any(axis=1)])
print(df.fillna("not available"))
print(df.duplicated())               ###check duplicate rows
print(df[df.duplicated()])           ###view duplicated rows
print(df.duplicated().sum())         ### count of duplicates
print(df.drop_duplicates())          ###drop duplicates

##---DATA TRANSFORMATION

print(df.rename(columns={'event_name':'Event_name'},inplace=True))
print(df)
df['balls_per_over'] = df['balls_per_over'].astype(float)
# print(df)
print(df.dtypes)
df['venue'] = df['venue'].str.strip().str.title()
print(df)
print(df['venue'])
##reorder,replace,new_column--------------------------------------------
print(df['venue'].unique())      ##unique venues
print(df['venue'].value_counts())    ###count of each venues
print(df.groupby('venue')['season_id'].mean())      #------not a good data but these steps for average,mean and mainly groupby.
print(df.sort_values(by='win_by_runs',ascending=False))    #---sorting
print(df[df['win_by_runs']>80.00])
print(df.corr(numeric_only=True))
print(df['venue'].value_counts().plot(kind='bar',title='values'))
#basic data analysis function----







