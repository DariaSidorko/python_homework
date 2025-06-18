

import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Oldest Living MLB Players")
st.title("📊 Oldest Living Baseball Players Dashboard")


@st.cache_data
def load_data():
    conn = sqlite3.connect("oldest_living_players_cleaned.csv")  
    df = pd.read_sql_query("SELECT * FROM oldest_living_players", conn)
    conn.close()

    # Clean and convert age to number
    df["Age_Num"] = pd.to_numeric(df["Age"].str.extract(r'(\d+)')[0], errors="coerce")

    # Extract numeric years from dates
    df["Debut_Year"] = pd.to_datetime(df["Debut"], errors="coerce").dt.year
    df["Final_Year"] = pd.to_datetime(df["Final Game"], errors="coerce").dt.year

    # Drop rows with NaNs in key filter fields
    df = df.dropna(subset=["Age_Num", "Debut_Year", "Team"])
    
    return df

df = load_data()

st.write("Columns in df:", df.columns.tolist())

# Sidebar filters
with st.sidebar:
    st.header("🔧 Filters")

    team_options = sorted(df["Team"].dropna().unique())
    selected_team = st.selectbox("Select Team", ["All"] + team_options)

    # Use only numeric values for sliders
    min_age = int(df["Age_Num"].min())
    max_age = int(df["Age_Num"].max())
    age_range = st.slider("Select Age Range", min_age, max_age, (min_age, max_age))

    min_debut = int(df["Debut_Year"].min())
    max_debut = int(df["Debut_Year"].max())
    debut_range = st.slider("Debut Year Range", min_debut, max_debut, (1930, 1970))

# Apply filters
filtered_df = df[
    (df["Age_Num"] >= age_range[0]) &
    (df["Age_Num"] <= age_range[1]) &
    (df["Debut_Year"] >= debut_range[0]) &
    (df["Debut_Year"] <= debut_range[1])
]

if selected_team != "All":
    filtered_df = filtered_df[filtered_df["Team"] == selected_team]

# Dashboard layout
st.markdown("## 👴 Top Oldest Living Players")
sorted_df = filtered_df.sort_values(by="Age_Num", ascending=False)
st.dataframe(sorted_df[["Name", "Age", "Team", "Debut", "Final Game"]])

# Chart 1: Age distribution
st.markdown("## 📈 Age Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df["Age_Num"], bins=10, kde=True, ax=ax1)
ax1.set_xlabel("Age")
ax1.set_ylabel("Number of Players")
st.pyplot(fig1)

# Chart 2: Count by team
st.markdown("## ⚾ Players by Team")
team_counts = filtered_df["Team"].value_counts().head(10)
fig3, ax3 = plt.subplots()
team_counts.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Player Count")
st.pyplot(fig3)


# Chart 3: 
# Ensure numeric values and drop rows with missing data
career_df = df.dropna(subset=["Debut_Year", "Final_Year", "Age_Num"]).copy()
career_df["Career_Length"] = career_df["Final_Year"] - career_df["Debut_Year"]

# Keep only positive career lengths
career_df = career_df[career_df["Career_Length"] >= 0]

# Get top 20 by career length
top20_career = career_df.sort_values(by="Career_Length", ascending=False).head(20)

# Chart
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top20_career, x="Career_Length", y="Name", palette="coolwarm", ax=ax4)
ax4.set_xlabel("Career Length (Years)")
ax4.set_ylabel("Player Name")
ax4.set_title("Top 20 Oldest Living Players with Longest MLB Careers")
st.pyplot(fig4)


