# Pandas-Practices
🧾 README.md Content (for GitHub Upload)

# 🐼 Pandas DataFrame Practice — Selection, Filtering & Cleaning

This Python script demonstrates how to work with Pandas DataFrames — including selecting data, filtering rows, and handling missing values.

---

## 📘 Topics Covered
- Creating a Pandas DataFrame  
- Selecting Columns (Single & Multiple)  
- Selecting Rows using loc[] (Label-based)  
- Selecting Rows using iloc[] (Index-based)  
- Row & Column slicing  
- Conditional filtering using:
  - Comparison operators (<, ==, etc.)
  - Logical operators (&)
  - isin() method
- Handling missing data:
  - isnull()
  - dropna()
  - fillna() with custom values or mean

---

## 🧠 Code Example


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

🚀 How to Run

1. Install Pandas

pip install pandas


2. Save the script as pandas_practice.py


3. Run it:

python pandas_practice.py




---

📎 Author

Ashokkumar
💼 Aspiring Data Analyst
📍 India


---

🔗 Connect with Me

💻 LinkedIn Profile :(https://www.linkedin.com/in/ashok45/)

📂 GitHub Repository

📝 Dev.to Post : (https://dev.to/ashok_kumar_564581944e3ef)



---

⭐ If you find this helpful, star the repo!
