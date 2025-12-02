
# Module 1: Data Loading & Inspection
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

# module 2: cleaning the datasets
df.fillna({'director': 'Unknown','cast': 'Unknown','rating': 'Unknown','country': 'Unknown','date_added': 'Unknown','duration': 'Unknown'}, inplace=True)
print(df.isnull().sum()) #verification

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added_raw'] = df['date_added'].dt.strftime('%Y-%m-%d')
df['date_added_raw'] = df['date_added_raw'].fillna("Unknown")  # date to string


print(df['date_added'].dtype)
print(df['date_added'].head())

print(df['duration'].unique()[:20]) #to print duration of first 20 
print(df.groupby('type')['duration'].unique()) # durations per time
print(df['duration'].str.contains('min', na=False).sum())  # chack patterns
print(df['duration'].str.contains('Season',na=False).sum()) # check patterns

text_cols = ['title', 'director', 'cast', 'country', 'listed_in', 'description']
df[text_cols] = df[text_cols].apply(lambda x: x.str.lower())
print(df['title'].head())  # convert text columns to lowercase

df.drop_duplicates(inplace =True) 
df.reset_index(drop=True, inplace=True) #remove duplicate rows
print(df.shape) #verification

