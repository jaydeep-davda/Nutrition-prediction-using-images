import streamlit as st
import matplotlib.pyplot as plt

# -----------------------------
# Nutrition Database
# -----------------------------
nutrition_db = {
    "Pizza": {"Calories": 285, "Protein": 12, "Carbs": 36, "Fat": 10},
    "Pasta": {"Calories": 310, "Protein": 11, "Carbs": 42, "Fat": 9},
    "Burger": {"Calories": 354, "Protein": 17, "Carbs": 33, "Fat": 20},
    "Biryani": {"Calories": 400, "Protein": 20, "Carbs": 50, "Fat": 15},
    "Ice Cream": {"Calories": 207, "Protein": 3, "Carbs": 24, "Fat": 11},
    "Steak": {"Calories": 679, "Protein": 62, "Carbs": 0, "Fat": 48},
    "Omelette": {"Calories": 154, "Protein": 10, "Carbs": 2, "Fat": 12},
    "Quinoa Bowl": {"Calories": 250, "Protein": 9, "Carbs": 35, "Fat": 7}
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Food Nutrition Estimator", layout="wide")
st.title("🍽️ Food Nutrition Estimator")

food = st.selectbox(
    "Select a food item",
    ["-- Select --"] + list(nutrition_db.keys())
)

if st.button("Predict Nutrition"):
    if food == "-- Select --":
        st.warning("Please select a food item.")
    else:
        # -------- IMAGE (SAFE, NO REQUESTS) --------
        image_url = f"https://source.unsplash.com/600x400/?{food},food"

        col1, col2 = st.columns(2)

        with col1:
            st.image(image_url, caption=food, use_column_width=True)

        with col2:
            n = nutrition_db[food]
            st.subheader("Nutritional Values")
            st.write(f"Calories: {n['Calories']} kcal")
            st.write(f"Protein: {n['Protein']} g")
            st.write(f"Carbohydrates: {n['Carbs']} g")
            st.write(f"Fat: {n['Fat']} g")

        # -------- DONUT CHART --------
        macros = {
            "Protein": n["Protein"],
            "Carbs": n["Carbs"],
            "Fat": n["Fat"]
        }

        fig, ax = plt.subplots()
        ax.pie(
            macros.values(),
            labels=macros.keys(),
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops=dict(width=0.4)
        )
        ax.set_title("Macronutrient Breakdown")

        st.pyplot(fig)
