import streamlit as st
import pickle
import pandas as pd

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
# Load model & data
# -------------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Example: load your food dataset (adjust path/name if needed)
df = pd.read_csv("food_dataset.csv")

# -------------------------------
# User input section
# -------------------------------
st.sidebar.header("User Preferences")

diet_type = st.sidebar.selectbox(
    "Select Diet Type",
    df["Diet"].unique()
)

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    df["Cuisine"].unique()
)

max_calories = st.sidebar.slider(
    "Maximum Calories",
    int(df["Calories"].min()),
    int(df["Calories"].max()),
    500
)

# -------------------------------
# Prediction / Recommendation
# -------------------------------
if st.sidebar.button("Get Recommendations"):
    st.subheader("✅ Recommended Food Items")

    # --- Example filtering logic (replace with your ML prediction if needed)
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

            # Create Unsplash dynamic image URL
            query = food_name.replace(" ", "+")
            image_url = f"https://source.unsplash.com/600x400/?{query},food"

            col.image(image_url, use_column_width=True)
            col.markdown(f"**{food_name}**")
            col.write(f"Calories: {row['Calories']}")
            col.write(f"Cuisine: {row['Cuisine']}")

# -------------------------------
# Footer note (important academically)
# -------------------------------
st.markdown("---")
st.caption(
    "📌 Note: Food images are fetched dynamically from a public image service "
    "for visualization only. The machine learning model uses structured data only."
)