# Giltech Online Cyber: COVID-19 Research Explorer

import pandas as pd

# Load dataset (CORD-19 metadata)
df = pd.read_csv("metadata.csv")

print("📊 Giltech Online Cyber - Initial Data Overview")
print("Shape of dataset:", df.shape)
print("\nFirst 5 records:")
print(df.head())

# Check column info
print("\nData structure:")
print(df.info())

# Check missing values
print("\nMissing values summary:")
print(df.isnull().sum())

# Basic stats
print("\nStatistics:")
print(df.describe())

# Clean missing values
df = df.dropna(subset=["title", "publish_time"])

# Convert dates
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract year for trend analysis
df["year"] = df["publish_time"].dt.year

# Add new column: abstract word count
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

print("✅ Giltech Online Cyber - Data cleaned and ready for analysis")

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Papers per year
papers_per_year = df["year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
sns.barplot(x=papers_per_year.index, y=papers_per_year.values, color="skyblue")
plt.title("Giltech Online Cyber: COVID-19 Publications per Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# Top Journals
top_journals = df["journal"].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="Blues_r")
plt.title("Giltech Online Cyber: Top 10 Journals")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()

# Word Cloud
titles = " ".join(df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Giltech Online Cyber: Frequent Words in Paper Titles")
plt.show()

