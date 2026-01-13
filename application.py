import streamlit as st
import matplotlib.pyplot as plt
import random

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
# Food Images (MULTIPLE)
# -----------------------------
food_images = {
    "Pizza": [
        "https://i.imgur.com/6R6KJ9g.jpg",
        "https://i.imgur.com/7pOqH2L.jpg",
        "https://i.imgur.com/LwQzX4U.jpg"
    ],
    "Pasta": [
        "https://i.imgur.com/oYiTqum.jpg",
        "https://i.imgur.com/zKQ6H1Z.jpg",
        "https://i.imgur.com/0XKznJY.jpg"
    ],
    "Burger": [
        "https://i.imgur.com/8GQZ7pQ.jpg",
        "https://i.imgur.com/eZ5yGqO.jpg",
        "https://i.imgur.com/QZ9YQ7N.jpg"
    ],
    "Biryani": [
        "https://i.imgur.com/wYJrHfL.jpg",
        "https://i.imgur.com/tmJH5eM.jpg"
    ],
    "Ice Cream": [
        "https://i.imgur.com/5M0p5Ks.jpg",
        "https://i.imgur.com/MZkR3P2.jpg"
    ],
    "Steak": [
        "https://i.imgur.com/y2K4VxP.jpg",
        "https://i.imgur.com/Dp3w6gM.jpg"
    ],
    "Omelette": [
        "https://i.imgur.com/4C0uYgU.jpg",
        "https://i.imgur.com/qL3Y8vB.jpg"
    ],
    "Quinoa Bowl": [
        "https://i.imgur.com/dz3Fh5E.jpg",
        "https://i.imgur.com/1B0Z9tL.jpg"
    ]
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
        col1, col2 = st.columns(2)

        # -------- IMAGE --------
        with col1:
            image_list = food_images.get(food)
            random_image = random.choice(image_list)
            st.image(random_image, caption=food, use_container_width=True)

        # -------- NUTRITION --------
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
