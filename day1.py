import pandas as pd
df = pd.read_csv(r"C:\Users\ACER\Documents\Excel\netflix_data.csv")

df.head()
print(df.head())
df.info()
df.describe()
print(df.describe())
df.isnull().sum() #missing values
print(df.isnull().sum()) 
print(df.nunique()) 
print(df['director'].unique())      # shows all unique director names
print(df['director'].nunique())     # counts the number of unique directors

# Count how many times each ratings appears
print(df['rating'].value_counts())
#to find datatype(string/object)
print(df['date_added'].dtype)

print("Numeric columns:")
print(df.select_dtypes(include=['number']).columns)

print("\nCategorical columns:")
print(df.select_dtypes(include=['object']).columns)


