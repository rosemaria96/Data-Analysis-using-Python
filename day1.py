# Module 1: Data Loading
import pandas as pd
#Load Dataset
df = pd.read_csv(r"C:\Users\ACER\Documents\Excel\netflix_data.csv")
print("\n---HEAD---")
df.head()  
print(df.head())

print("\n---INFO--")
df.info()

print("\n---DESCRIBE--")
df.describe()
print(df.describe())
print(df.describe(include='all'))

print("\n--MISSING VALUES--")
df.isnull().sum() #missing values
print(df.isnull().sum()) 

print("\n--UNIQUE COUNTS--")
print(df.nunique()) 

print("Numeric columns:")
print(df.select_dtypes(include=['number']).columns)
print(df.select_dtypes(include=['number']).columns.tolist())

print("\nCategorical columns:")
print(df.select_dtypes(include=['object']).columns)
print(df.select_dtypes(include=['object']).columns.tolist())

print("\n--SAMPLE UNIQUE DIRECTORS--")
print(df['director'].unique()[:10]) #show only first 10
print(df['director'].unique())      # shows all unique director names
print(df['director'].nunique())     # counts the number of unique directors/display total unique directors

print("\n--RATING VALUE COUNTS--")
print(df['rating'].value_counts()) # Count how many times each ratings appears

print("\n--DATE DATA TYPE--")
print(df['date_added'].dtype) #to find datatype(string/object)



