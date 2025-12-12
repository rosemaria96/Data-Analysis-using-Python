# module 2: cleaning the datasets
import pandas as pd
# Data loading
df = pd.read_csv(r"C:\Users\ACER\Documents\Excel\netflix_data.csv")
print("\n--- BEFORE CLEANING: Missing Values ---")
print(df.isnull().sum())
print("--MISSING VALUES--")
df.fillna({'director': 'Unknown','cast': 'Unknown','rating': 'Unknown','country': 'Unknown','date_added': 'Unknown','duration': 'Unknown'}, inplace=True)
print("\n--AFTER FILL: MISSING VALUES--")
print(df.isnull().sum()) #verification
print("--CONVERT DATE_ADDED TO DATETIME--")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce') # convert date added to datetime
df['date_added_raw'] = df['date_added'].dt.strftime('%Y-%m-%d').fillna("Unknown") 
print("\n--DATE COLUMN (Converted)--")
print(df['date_added'].dtype) # to find datatype of date_added
print(df['date_added'].head())
print("\n--SAMPLE DURATIONS--")
print(df['duration'].unique()[:20]) #to print duration of first 20 
print(df.groupby('type')['duration'].unique()) # durations per time
print(df['duration'].str.contains('min', na=False).sum())  # chack patterns #DURATION COUNT(MOVIES)
print(df['duration'].str.contains('Season',na=False).sum()) # check patterns #duration count(TV Shows)
# TEXT NORMALIZATION
print("--CONVERT TO LOWERCASE--")
text_cols = ['title', 'director', 'cast', 'country', 'listed_in', 'description']
df[text_cols] = df[text_cols].apply(lambda x: x.str.lower()) # convert text columns to lowercase
print("\n--Sample titles after lowercase--")
print(df['title'].head())  
print("\n--REMOVE DUPLICATES--")
df.drop_duplicates(inplace =True) 
df.reset_index(drop=True, inplace=True) #remove duplicate rows
print("--FINAL SHAPE AFTER CLEANING--")
print(df.shape) #verification
#cleaned file
df.to_csv(r"D:\Data Analytics using Python\netflix_data_cleaned.csv", index=False)

