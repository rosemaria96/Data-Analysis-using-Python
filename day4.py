# -----------------------------
# DAY 4: Feature Engineering + Advanced EDA
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(r"D:\Data Analytics using Python\netflix_data_cleaned.csv")

# -----------------------------
# Split Movies and TV Shows
# -----------------------------
movies = df[df['type'] == 'Movie'].copy()
tv = df[df['type'] == 'TV Show'].copy()

# -----------------------------
# Duration Feature Engineering
# -----------------------------
# Movies: duration in minutes
movies['duration_min'] = pd.to_numeric(movies['duration'].str.replace(' min','', regex=False), errors='coerce')

# TV Shows: number of seasons
tv['seasons'] = pd.to_numeric(tv['duration'].str.extract(r'(\d+)')[0], errors='coerce')

# -----------------------------
# Date Features
# -----------------------------
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['added_month'] = df['date_added'].dt.month
df['added_weekday'] = df['date_added'].dt.day_name()

# -----------------------------
# Most common year added
# -----------------------------
most_common_year = df['year_added'].mode()[0]

# -----------------------------
# Genre count
# -----------------------------
df['num_genres'] = df['listed_in'].str.split(',').apply(len)
genre_counts = df['listed_in'].str.split(',').explode().str.strip().value_counts()

# -----------------------------
# Director & Lead Actor counts
# -----------------------------
# Director counts
director_counts = df['director'].value_counts()
df['director_count'] = df['director'].map(director_counts)

# Lead actor (first in cast)
df['lead_actor'] = df['cast'].str.split(',').str[0]
actor_counts = df['lead_actor'].value_counts()
df['lead_actor_count'] = df['lead_actor'].map(actor_counts)

# Flag unknowns
df['director_unknown'] = df['director'].apply(lambda x: 1 if x=='Unknown' else 0)
df['cast_unknown'] = df['cast'].apply(lambda x: 1 if x=='Unknown' else 0)

# -----------------------------
# Most prolific directors & actors (exclude 'Unknown')
# -----------------------------
top_director = df[df['director'] != 'Unknown']['director'].value_counts().idxmax()
top_director_count = df[df['director'] != 'Unknown']['director'].value_counts().max()

top_actor = df[df['lead_actor'] != 'Unknown']['lead_actor'].value_counts().idxmax()
top_actor_count = df[df['lead_actor'] != 'Unknown']['lead_actor'].value_counts().max()

# -----------------------------
# Average durations
# -----------------------------
avg_movie_duration = movies['duration_min'].dropna().mean()
avg_tv_seasons = tv['seasons'].dropna().mean()

# -----------------------------
# Print insights
# -----------------------------
print(f"Average movie duration (min): {avg_movie_duration:.2f}")
print(f"Average TV Show seasons: {avg_tv_seasons:.2f}")
print(f"Most common year added: {most_common_year}")
print(f"Most prolific director: {top_director} ({top_director_count} titles)")
print(f"Most prolific lead actor: {top_actor} ({top_actor_count} titles)")
print("\nTop 10 genres by number of titles:")
print(genre_counts.head(10))

# -----------------------------
# VISUALIZATIONS
# -----------------------------
sns.set_style("whitegrid")

# Top 10 Genres
plt.figure(figsize=(10,6))
sns.barplot(y=genre_counts.head(10).index, x=genre_counts.head(10).values, palette="viridis")
plt.title("Top 10 Genres by Number of Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Genres")
plt.show()

# Top 5 Directors
top5_directors = df[df['director'] != 'Unknown']['director'].value_counts().head(5)
plt.figure(figsize=(10,5))
sns.barplot(y=top5_directors.index, x=top5_directors.values, palette="magma")
plt.title("Top 5 Directors by Number of Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.show()

# Top 5 Lead Actors
top5_actors = df[df['lead_actor'] != 'Unknown']['lead_actor'].value_counts().head(5)
plt.figure(figsize=(10,5))
sns.barplot(y=top5_actors.index, x=top5_actors.values, palette="coolwarm")
plt.title("Top 5 Lead Actors by Number of Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Actor")
plt.show()

# Year Added Distribution
plt.figure(figsize=(10,5))
sns.countplot(x='year_added', data=df, palette="Set2", order=sorted(df['year_added'].dropna().unique()))
plt.title("Number of Titles Added per Year")
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# ---------------------------
# Save feature-engineered dataset
# ---------------------------
df.to_csv(r"D:\Data Analytics using Python\netflix_data_features.csv", index=False)
print("\nFeature-engineered dataset saved successfully!")