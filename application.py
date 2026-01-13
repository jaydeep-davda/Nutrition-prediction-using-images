# application.py
import streamlit as st

# -------------------
# Install missing packages if needed
# -------------------
def install_package(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    install_package("beautifulsoup4")
    from bs4 import BeautifulSoup

try:
    import pandas as pd
except ModuleNotFoundError:
    install_package("pandas")
    import pandas as pd

try:
    import requests
except ModuleNotFoundError:
    install_package("requests")
    import requests

# -------------------
# Streamlit App Starts
# -------------------
st.set_page_config(page_title="Nutrition Prediction", page_icon="🍎", layout="wide")
st.title("🍏 Nutrition Prediction Using Images")
st.write("Upload a food image to predict nutrition, or explore nutrition data from a sample table or a webpage.")

# -------------------
# Nutrition Table
# -------------------
nutrition_data = {
    "Pizza": {"Calories": 285, "Protein": 12, "Carbs": 36, "Fat": 10},
    "Pasta": {"Calories": 310, "Protein": 11, "Carbs": 42, "Fat": 9},
    "Risotto": {"Calories": 320, "Protein": 8, "Carbs": 45, "Fat": 10},
    "Lasagna": {"Calories": 350, "Protein": 18, "Carbs": 30, "Fat": 18},
    "Caprese Salad": {"Calories": 220, "Protein": 10, "Carbs": 6, "Fat": 18},
    "Burger": {"Calories": 354, "Protein": 17, "Carbs": 33, "Fat": 20},
    "Fried Chicken": {"Calories": 400, "Protein": 25, "Carbs": 10, "Fat": 30},
    "French Fries": {"Calories": 312, "Protein": 3, "Carbs": 41, "Fat": 15},
    "Mac and Cheese": {"Calories": 450, "Protein": 18, "Carbs": 40, "Fat": 22},
    "Hot Dog": {"Calories": 290, "Protein": 10, "Carbs": 24, "Fat": 18},
    "Sushi": {"Calories": 200, "Protein": 8, "Carbs": 28, "Fat": 4},
    "Ramen": {"Calories": 436, "Protein": 18, "Carbs": 62, "Fat": 12},
    "Tempura": {"Calories": 350, "Protein": 10, "Carbs": 40, "Fat": 18},
    "Miso Soup": {"Calories": 80, "Protein": 5, "Carbs": 8, "Fat": 3},
    "Onigiri": {"Calories": 180, "Protein": 4, "Carbs": 38, "Fat": 2},
    "Tacos": {"Calories": 226, "Protein": 12, "Carbs": 20, "Fat": 12},
    "Burrito": {"Calories": 320, "Protein": 15, "Carbs": 35, "Fat": 14},
    "Quesadilla": {"Calories": 290, "Protein": 14, "Carbs": 28, "Fat": 16},
    "Nachos": {"Calories": 360, "Protein": 10, "Carbs": 40, "Fat": 18},
    "Guacamole": {"Calories": 160, "Protein": 2, "Carbs": 8, "Fat": 15},
    "Butter Chicken": {"Calories": 430, "Protein": 28, "Carbs": 14, "Fat": 28},
    "Paneer Tikka": {"Calories": 250, "Protein": 18, "Carbs": 6, "Fat": 16},
    "Dal Makhani": {"Calories": 300, "Protein": 15, "Carbs": 30, "Fat": 12},
    "Chole": {"Calories": 280, "Protein": 14, "Carbs": 32, "Fat": 10},
    "Biryani": {"Calories": 400, "Protein": 20, "Carbs": 50, "Fat": 15},
    "Bratwurst": {"Calories": 320, "Protein": 15, "Carbs": 2, "Fat": 28},
    "Sauerbraten": {"Calories": 450, "Protein": 35, "Carbs": 20, "Fat": 25},
    "Pretzel": {"Calories": 300, "Protein": 9, "Carbs": 58, "Fat": 3},
    "Kartoffelsalat": {"Calories": 200, "Protein": 4, "Carbs": 28, "Fat": 8},
    "Wiener Schnitzel": {"Calories": 400, "Protein": 30, "Carbs": 10, "Fat": 28},
    "Ice Cream": {"Calories": 207, "Protein": 3, "Carbs": 24, "Fat": 11},
    "Chocolate Cake": {"Calories": 352, "Protein": 4, "Carbs": 46, "Fat": 18},
    "Smoothie": {"Calories": 180, "Protein": 5, "Carbs": 34, "Fat": 1},
    "Brownie": {"Calories": 320, "Protein": 5, "Carbs": 45, "Fat": 15},
    "Cookies": {"Calories": 150, "Protein": 2, "Carbs": 20, "Fat": 7},
    "Steak": {"Calories": 679, "Protein": 62, "Carbs": 0, "Fat": 48},
    "Omelette": {"Calories": 154, "Protein": 10, "Carbs": 2, "Fat": 12},
    "Grilled Fish": {"Calories": 232, "Protein": 22, "Carbs": 0, "Fat": 15},
    "Quinoa Bowl": {"Calories": 250, "Protein": 9, "Carbs": 35, "Fat": 7}
}

# Convert dictionary to DataFrame
nutrition_df = pd.DataFrame(nutrition_data).T.reset_index()
nutrition_df.rename(columns={"index": "Food"}, inplace=True)
st.subheader("🍽️ Nutrition Table")
st.dataframe(nutrition_df)

# -------------------
# Image Upload & Prediction Section
# -------------------
st.subheader("Upload a Food Image to Predict Nutrition")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Simple "prediction" based on food name input
    food_name = st.text_input("Enter the food name (as shown in table) for prediction:")
    if food_name:
        food_name = food_name.strip()
        if food_name in nutrition_data:
            st.success(f"Nutrition for **{food_name}**:")
            st.json(nutrition_data[food_name])
        else:
            st.error("Food not found in table. Check spelling or choose a different item.")

# -------------------
# Optional: Web Scraping Section
# -------------------
st.subheader("Optional: Scrape Nutrition Info from a Website")
url = st.text_input("Enter a URL to scrape (optional):", key="url_input")

if url:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        st.write("✅ Webpage fetched successfully!")
        st.write("Page Title:", soup.title.string if soup.title else "No title found")
    except Exception as e:
        st.error(f"Error fetching the page: {e}")

# -------------------
# Footer
# -------------------
st.markdown("---")
st.write("Developed with ❤️ using Streamlit")
