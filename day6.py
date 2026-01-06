import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv(r"D:\Data Analytics using Python\netflix_data_cleaned.csv")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
movies = df[df['type'] == 'Movie'].copy()
tv = df[df['type'] == 'TV Show'].copy()

movies['duration_min'] = pd.to_numeric(
    movies['duration'].str.replace(' min','', regex=False),
    errors='coerce'
)

tv['seasons'] = pd.to_numeric(
    tv['duration'].str.extract(r'(\d+)')[0],
    errors='coerce'
)
corr_df = movies[['duration_min', 'release_year']].dropna()
corr = corr_df.corr()
print(corr)

plt.figure()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation: Movie Duration vs Release Year")
plt.show()

movie_durations = movies['duration_min'].dropna()
tv_seasons = tv['seasons'].dropna()

t_stat, p_value = stats.ttest_ind(movie_durations, tv_seasons, equal_var=False)

print("P-value:", p_value)
if p_value < 0.05:
    print("Significant difference → Movies are longer")
else:
    print("No significant difference")
t_stat, p_value = stats.ttest_ind(
    movies['release_year'],
    tv['release_year'],
    equal_var=False
)

print("P-value:", p_value)
contingency = pd.crosstab(df['type'], df['rating'])

chi2, p, dof, expected = stats.chi2_contingency(contingency)

print("P-value:", p)
if p < 0.05:
    print("Rating depends on content type")
else:
    print("Rating independent of content type")
plt.figure()
sns.boxplot(data=movies, y='duration_min')
plt.title("Movie Duration Distribution")
plt.show()
plt.figure()
sns.boxplot(data=tv, y='seasons')
plt.title("TV Show Seasons Distribution")
plt.show()
