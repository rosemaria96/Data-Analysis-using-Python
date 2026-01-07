
import pandas as pd
from pathlib import Path

# -------------------------------
# PATH SETUP
# -------------------------------

BASE_DIR = Path("D:/Data Analytics using Python")

RAW_DATA = BASE_DIR / "data" / "raw" / "netflix_data.csv"
PROCESSED_DATA = BASE_DIR / "data" / "processed" / "netflix_cleaned_day8.csv"
REPORT_PATH = BASE_DIR / "reports" / "summary_day8.txt"


# Create folders if missing
PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)
REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

# -------------------------------
# LOAD DATA
# -------------------------------
def load_data(path):
    df = pd.read_csv(path)
    return df

# -------------------------------
# CLEAN DATA
# -------------------------------
def clean_data(df):
    df = df.copy()

    df.fillna({
        'director': 'Unknown',
        'cast': 'Unknown',
        'country': 'Unknown',
        'rating': 'Unknown'
    }, inplace=True)

    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    return df

# -------------------------------
# FEATURE ENGINEERING
# -------------------------------
def feature_engineering(df):
    df = df.copy()

    # Content age
    df['content_age'] = 2025 - df['release_year']

    # Genre count
    df['num_genres'] = df['listed_in'].str.split(',').apply(len)

    # Lead actor
    df['lead_actor'] = df['cast'].str.split(',').str[0]

    return df

# -------------------------------
# ANALYTICS SUMMARY
# -------------------------------
def generate_insights(df):
    insights = []

    insights.append(f"Total titles: {len(df)}")
    insights.append(f"Movies: {(df['type']=='Movie').sum()}")
    insights.append(f"TV Shows: {(df['type']=='TV Show').sum()}")

    most_common_year = df['release_year'].mode()[0]
    insights.append(f"Most common release year: {most_common_year}")

    top_genre = (
        df['listed_in']
        .str.split(',')
        .explode()
        .str.strip()
        .value_counts()
        .idxmax()
    )
    insights.append(f"Top genre: {top_genre}")

    top_director = df['director'].value_counts().idxmax()
    insights.append(f"Most prolific director: {top_director}")

    return insights

# -------------------------------
# SAVE OUTPUTS
# -------------------------------
def save_outputs(df, insights):
    df.to_csv(PROCESSED_DATA, index=False)

    with open(REPORT_PATH, "w") as f:
        f.write("DAY 8 ANALYTICS SUMMARY\n")
        f.write("-" * 30 + "\n")
        for line in insights:
            f.write(line + "\n")

# -------------------------------
# MAIN PIPELINE
# -------------------------------
def run_pipeline():
    print("Starting Day 8 Pipeline...")

    df = load_data(RAW_DATA)
    df = clean_data(df)
    df = feature_engineering(df)
    insights = generate_insights(df)
    save_outputs(df, insights)

    print("Pipeline completed successfully.")
    print(f"Cleaned data saved to: {PROCESSED_DATA}")
    print(f"Report saved to: {REPORT_PATH}")

# -------------------------------
# EXECUTE
# -------------------------------
if __name__ == "__main__":
    run_pipeline()
