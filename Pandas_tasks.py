import pandas as pd
df=pd.read_csv('C:/Users/ashok/Downloads/sales_data.csv')    #Load file
print(df)

#---Data Understanding:

print(df.head(2))       # Top Rows(2)  
print(df.columns)       # Column names
print(df.dtypes)        # Data Types
print(df.size)          # Total Size
print(df.shape)         # Rows & Columns
print(len(df.columns))  # Column count
print(len(df.index))    # Index count
print(df)
print(df.isnull())            # Checking Null values
print(df.isnull().sum())      # Count of the Null Values
print(df.duplicated())        # Checking Duplicated Values
print(df.duplicated().sum())  # count of Duplicated values
print(df.describe())          # Basic Numeric Checks
print(df.info())              # Full info of our data
df['Date']= pd.to_datetime(df['Date'],errors='coerce')  # Changing Datetime dtype to Date Column         errors='coerce' - its uses for missing and Invalid values will be Replaced by NaT or NaN.
print(df.info())                                        # check again for dtype
df['Discount'] = df['Discount'] * 100                   # For round values    
df['Discount'] = df['Discount'].astype(str) + ' %'      # Add percentage values in Discount column
print(df)
print(df.info())
df['Discount'] = pd.to_numeric(df['Discount'],errors='coerce')    # Changing Data Type in Float
print(df.info())

##---Data Cleaning:

df_original=df.copy()
print(df.describe(include='all').T)                       # It gives all column details with Transpose.Not only Numerical
missing=df.isnull().sum().sort_values(ascending=False)    # Checking null values and count 
print(missing)
print(df.duplicated())                                       # Checking Duplicate values
print(df.duplicated().sum())                                 # count fo Duplicate values
print(df['Date'].min(),df['Date'].max())                      # for checking realistic values in Date
print(df.nunique())                                            # checking Real unique values ( Number of unique )
print(df)

##---Data Preparation:

df['Total_sales']=df['Quantity'] * df['UnitPrice'] * (1- df['Discount'])     # New column Created (Total sales) using math Formula
df['Profit_margin'] = df['Profit'] / df['Total_sales'] * 100                 # Profit_margin column created
df['Profit_margin']=df['Profit_margin'].round(2)                             # Round(2) 
df['Profit_margin']=df['Profit_margin'].astype(str) + ' %'                   # Percentage Added
print(df)
df['Month'] = df['Date'].dt.month                                        # Month extraction
print(df)                         
df['Year']=df['Date'].dt.year                                            # Year Extraction
print(df)
df.rename(columns={'OrderID':'Order ID','UnitPrice':'Unit Price','SalesPerson':'Sales_Person'},inplace=True)         # Rename specific columns if we need all columns use Replace.
print(df.columns)
df.columns=df.columns.str.replace('_',' ')         # Its for all columns.
df.to_csv('sales_data.csv',index=False)
#regex = True means use Pattern
#regex = False means exact Match          #regular expression.

#---Data Exploration.


print(df.groupby('Region')['Profit'].sum())                                     # Total profit for Each Region
print(df)
print(df.groupby('SalesPerson')['Quantity'].sum())                              # Total Quantity sold by Each Person
print(df.groupby('Category')['Discount'].mean().round(2))                       # Average Discount Per category
print(df.columns)
high=df.iloc[df['Profit'].idxmax()]
print(high)
low=df.loc[df['Profit'].idxmin()]                                                                   # Highest and Lowest profit with the uses of Loc and Iloc.
print(low)
region_profit_most=df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(region_profit_most.index[0])
most_profit_salesperson=df.groupby('SalesPerson')['Profit'].sum().sort_values(ascending=False)        # Most Profitable salesperson & Region.
print(most_profit_salesperson.index[0])

#---Aggregation & Insights.
#  1. calculate the total and average profit by category ?

total_profit_category=df.groupby('Category')['Profit'].sum().reset_index().sort_values('Profit',ascending=False)
print(total_profit_category)
avg_profit_category=df.groupby('Category')['Profit'].mean().reset_index().sort_values('Profit',ascending=False)                       # reset index uses for output becomes a normal data frame.
print(avg_profit_category)

# 2.Compare Sales and Profit across regions ?

region_summary=df.groupby('Region').agg(
    Total_sales=('Total_sales','sum'),
    Profit=('Profit','sum')
).reset_index()
print(region_summary)                               # Aggregation for region wise 

# Rough uses:

print(df.columns)
print(df.groupby('Region').sum())
print(df['Profit'].sum())
print(df.groupby('Region')['Profit'].sum().reset_index())

# 3. Analyze how Discount affects Total profit ?
discount_profit = (df.groupby('Discount')['Profit'].sum().reset_index().sort_values('Discount'))
print(discount_profit)                                                                                         # Analyzed how discount affects Total_profit.
print(df)

# 4. Identify the Top 5 products contibuting to Profit ?

print(df.groupby('Product')['Profit'].sum().reset_index().sort_values('Profit',ascending=False).head(5).reset_index(drop=True))
# Groupby Product and Profit 
# SUM
# Reset_index() for output view will be in Normal DataFrame.
# Sort_values with the column name of Profit and ascending = False.
# Head for Top 5 rows
# Reset_index(drop=True) its used for index name orderly.

# 5. Group Sales By Month to find monthly trends ?
monthly_trend=(df.groupby(['Year','Month']).agg(
    Total_sales=('Total_sales','sum'),
    Profit=('Profit','sum')
).reset_index().sort_values(['Year','Month']).round(2))                       # Aggregation used for monthly trend .
print(df.columns)
print(monthly_trend)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------