# DAY 5: Relationship Analysis & Pattern Discovery (PROFESSIONAL VERSION)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# -----------------------------
# Load cleaned dataset
# -----------------------------
df = pd.read_csv(r"D:\Data Analytics using Python\netflix_data_cleaned.csv")

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# -----------------------------
# Feature Engineering
# -----------------------------
movies = df[df['type'] == 'Movie'].copy()
tv = df[df['type'] == 'TV Show'].copy()

movies['duration_min'] = pd.to_numeric(
    movies['duration'].str.replace(' min', '', regex=False),
    errors='coerce'
)

tv['seasons'] = pd.to_numeric(
    tv['duration'].str.extract(r'(\d+)')[0],
    errors='coerce'
)

df['decade'] = (df['release_year'] // 10) * 10

# ======================================================
# Movies vs TV Shows by DECADE (FIXED VISIBILITY)
# ======================================================
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='decade', hue='type')
plt.title("Movies vs TV Shows by Decade")
plt.xlabel("Decade")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ======================================================
# Growth Trend Over Time (CORRECT TREND ANALYSIS)
# ======================================================
year_type = (
    df.groupby(['release_year', 'type'])
    .size()
    .reset_index(name='count')
)

plt.figure(figsize=(10,5))
sns.lineplot(data=year_type, x='release_year', y='count', hue='type')
plt.title("Growth Trend of Movies vs TV Shows Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# ======================================================
#  Movie Duration vs Release Year (AGGREGATED)
# ======================================================
movie_year_avg = (
    movies.groupby('release_year')['duration_min']
    .mean()
    .reset_index()
)

plt.figure(figsize=(10,5))
sns.lineplot(data=movie_year_avg, x='release_year', y='duration_min')
plt.title("Average Movie Duration Over Time")
plt.xlabel("Release Year")
plt.ylabel("Average Duration (minutes)")
plt.tight_layout()
plt.show()

# ======================================================
#  TV Show Seasons Distribution (CLEAN & READABLE)
# ======================================================
plt.figure(figsize=(8,5))
sns.boxplot(data=tv, y='seasons')
plt.title("Distribution of TV Show Seasons")
plt.ylabel("Number of Seasons")
plt.tight_layout()
plt.show()

# ======================================================
#  Top Genres (NO CLUTTER)
# ======================================================
genres = df['listed_in'].str.split(',').explode().str.strip()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

# ======================================================
# Content Rating Distribution
# ======================================================
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    y='rating',
    order=df['rating'].value_counts().index
)
plt.title("Content Rating Distribution")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

# ======================================================
# Movie Duration Distribution
# ======================================================
plt.figure(figsize=(8,5))
sns.histplot(movies['duration_min'].dropna(), bins=30, kde=True)
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ======================================================
# Top Content Producing Countries
# ======================================================
countries = df['country'].str.split(',').explode().str.strip()
top_countries = countries.value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
