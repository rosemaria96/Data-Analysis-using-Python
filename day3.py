import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\Data Analytics using Python\netflix_data_cleaned.csv")

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type')
plt.title("Distribution: Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

genre_counts = df['listed_in'].str.split(', ').explode().value_counts().head(10)

plt.figure(figsize=(10,5))
genre_counts.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year

plt.figure(figsize=(12,4))
df['year_added'].value_counts().sort_index().plot(kind='line')
plt.title("Netflix Titles Added per Year")
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,4))
sns.histplot(df['release_year'], bins=40, kde=True)
plt.title("Release Year Distribution")
plt.show()

plt.figure(figsize=(12,6))
df['rating'].value_counts().plot(kind='bar')
plt.title("Content Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

movies = df[df['type'] == 'Movie'].copy()
movies['minutes'] = movies['duration'].str.extract(r'(\d+)').astype(float)

plt.figure(figsize=(10,4))
sns.histplot(movies['minutes'], bins=40, kde=True)
plt.title("Movie Duration Distribution (Minutes)")
plt.show()

tv = df[df['type'] == 'TV Show'].copy()
tv['seasons'] = tv['duration'].str.extract(r'(\d+)').astype(int)

plt.figure(figsize=(6,4))
sns.countplot(x=tv['seasons'])
plt.title("TV Shows by Number of Seasons")
plt.show()

countries = df['country'].str.split(', ').explode().value_counts().head(10)

plt.figure(figsize=(10,4))
countries.plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.show()

df[df['director'] != "Unknown"]['director'].value_counts().head(10)

from wordcloud import WordCloud

text = " ".join(df['description'])
wc = WordCloud(width=1000, height=500).generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wc)
plt.axis("off")
plt.show()


