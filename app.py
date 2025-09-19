import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df = df.dropna(subset=["title", "publish_time"])
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# --- Giltech Online Cyber Branding ---
st.title("📊 Giltech Online Cyber: COVID-19 Data Explorer")
st.write("Welcome to Giltech Online Cyber’s interactive portal for exploring COVID-19 research papers.")

# Data Preview
st.subheader("🔎 Preview of Research Data")
st.write(df.head())

# Year Filter
years = df["year"].dropna().unique()
year_range = st.slider("Select Year Range", int(min(years)), int(max(years)), (2020, 2021))
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications per Year
st.subheader("📈 Publications per Year")
papers_per_year = filtered["year"].value_counts().sort_index()

fig, ax = plt.subplots()
sns.barplot(x=papers_per_year.index, y=papers_per_year.values, ax=ax, color="skyblue")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top Journals
st.subheader("🏛️ Top Journals")
top_journals = filtered["journal"].value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="Blues_r")
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# Word Cloud
st.subheader("☁️ Word Cloud of Titles")
titles = " ".join(filtered["title"].dropna())
if titles:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
