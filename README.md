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

```python
import pandas as pd

file = {
    'name': ["rohit", "ashok", "kumar"],
    'age': [23, 24, 25],
    'city': ["chennai", "madurai", "cuddalore"]
}

df = pd.DataFrame(file)

# Example: Selecting columns
print(df['name'])
print(df[['name', 'city']])

# Example: Filtering
print(df[df['age'] < 25])
print(df[df['city'].isin(['chennai', 'cuddalore'])])


---

🧹 Data Cleaning

print(df.isnull())             # Check missing values
print(df.isnull().sum())       # Count missing values
print(df.dropna())             # Drop missing values
print(df.fillna({'age': 0, 'city': 'unknown'}))  # Fill with custom values


---

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
