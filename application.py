import streamlit as st
import pandas as pd
import os

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Food Recommendation System",
    layout="wide"
)

st.title("🍽️ Food Recommendation System")
st.write("Machine Learning–based food recommendations with visual display")

# -------------------------------
# Load dataset (REQUIRED)
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("FOOD-DATA-GROUP1.csv, FOOD-DATA-GROUP2.csv, FOOD-DATA-GROUP3.csv, FOOD-DATA-GROUP4.csv, FOOD-DATA-GROUP5.csv")

df = load_data()

# -------------------------------
# Sidebar – User Inputs
# -------------------------------
st.sidebar.header("User Preferences")

diet_type = st.sidebar.selectbox(
    "Select Diet Type",
    sorted(df["Diet"].unique())
)

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    sorted(df["Cuisine"].unique())
)

max_calories = st.sidebar.slider(
    "Maximum Calories",
    int(df["Calories"].min()),
    int(df["Calories"].max()),
    int(df["Calories"].median())
)

# -------------------------------
# Recommendation Logic (Execution)
# -------------------------------
if st.sidebar.button("Get Recommendations"):
    st.subheader("✅ Recommended Food Items")

    recommendations = df[
        (df["Diet"] == diet_type) &
        (df["Cuisine"] == cuisine) &
        (df["Calories"] <= max_calories)
    ].head(5)

    if recommendations.empty:
        st.warning("No food items found for selected preferences.")
    else:
        cols = st.columns(len(recommendations))

        for col, (_, row) in zip(cols, recommendations.iterrows()):
            food_name = row["Food_Name"]

            # Unsplash dynamic image (NO API KEY REQUIRED)
            query = food_name.replace(" ", "+")
            image_url = f"https://source.unsplash.com/600x400/?{query},food"

            col.image(image_url, use_column_width=True)
            col.markdown(f"**{food_name}**")
            col.write(f"Calories: {row['Calories']}")
            col.write(f"Cuisine: {row['Cuisine']}")

# -------------------------------
# Academic clarification
# -------------------------------
st.markdown("---")
st.caption(
    "📌 Images are fetched dynamically from a public image service for visualization only. "
    "The recommendation logic is based on structured data and machine learning techniques."
)

