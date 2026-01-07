# =========================
# DAY 7: ADVANCED VISUAL ANALYTICS
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. Load Dataset
# -------------------------
df = pd.read_csv(r"D:\Data Analytics using Python\netflix_data_cleaned.csv")
print("Dataset loaded:", df.shape)

# -------------------------
# 2. Data Preparation
# -------------------------

# Convert duration
df_movies = df[df['type'] == 'Movie'].copy()

df_movies['duration_min'] = (
    df_movies['duration']
    .str.replace(' min', '', regex=False)
)

df_movies['duration_min'] = pd.to_numeric(
    df_movies['duration_min'],
    errors='coerce'
)

df_movies.dropna(subset=['duration_min'], inplace=True)

# Extract primary genre
df_movies['primary_genre'] = (
    df_movies['listed_in']
    .str.split(',')
    .str[0]
)

print("Prepared movie dataset for visualization")

# -------------------------
# 3. Distribution Analysis
# -------------------------

plt.figure(figsize=(10, 5))
sns.histplot(df_movies['duration_min'], bins=30, kde=True)
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# 4. Boxplot: Genre vs Duration
# -------------------------

top_genres = df_movies['primary_genre'].value_counts().head(5).index
df_top = df_movies[df_movies['primary_genre'].isin(top_genres)]

plt.figure(figsize=(12, 6))
sns.boxplot(
    data=df_top,
    x='primary_genre',
    y='duration_min'
)
plt.title("Movie Duration by Top Genres")
plt.xlabel("Genre")
plt.ylabel("Duration (minutes)")
plt.xticks(rotation=30)
plt.show()

# -------------------------
# 5. Trend Analysis Over Time
# -------------------------

yearly_avg = (
    df_movies
    .groupby('release_year')['duration_min']
    .mean()
)

plt.figure(figsize=(10, 5))
yearly_avg.plot()
plt.title("Average Movie Duration Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Duration (minutes)")
plt.show()

# -------------------------
# 6. Correlation Heatmap
# -------------------------

corr_df = df_movies[['release_year', 'duration_min']]

plt.figure(figsize=(6, 4))
sns.heatmap(
    corr_df.corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.show()

# -------------------------
# 7. Multivariate Scatter Plot
# -------------------------

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_top,
    x='release_year',
    y='duration_min',
    hue='primary_genre',
    alpha=0.7
)
plt.title("Movie Duration vs Release Year (by Genre)")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")
plt.show()

# -------------------------
# END OF DAY 7
# -------------------------
