import streamlit as st
import plotly.graph_objects as go

# -----------------------------
# Nutrition Database
# -----------------------------
nutrition_db = {
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

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Food Recognition & Nutrition Estimator", layout="wide")
st.title("🍽️ Food Recognition & Nutrition Estimator")
st.write("Select a food item to see its nutritional values and macronutrient breakdown.")

# Food selection
food_options = ["-- Select a food item --"] + list(nutrition_db.keys())
food = st.selectbox("Select a food item", food_options)

if st.button("Predict Nutrition"):
    if food == "-- Select a food item --":
        st.warning("Please select a food item first.")
    else:
        # -----------------------------
        # Fetch food image dynamically from Unsplash
        # -----------------------------
        image_url = f"https://source.unsplash.com/400x300/?{food.replace(' ', '%20')}"
        
        # Create two columns for image and nutrition side by side
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(image_url, caption=food, use_column_width=True)
        
        with col2:
            nutrition = nutrition_db[food]
            st.subheader("🍴 Predicted Food:")
            st.write(food)
            
            st.subheader("🧮 Nutritional Values:")
            st.write(f"**Calories:** {nutrition['Calories']} kcal")
            st.write(f"**Protein:** {nutrition['Protein']} g")
            st.write(f"**Carbohydrates:** {nutrition['Carbs']} g")
            st.write(f"**Fat:** {nutrition['Fat']} g")
        
        # -----------------------------
        # Interactive donut chart for macronutrients
        # -----------------------------
        macro_nutrition = {k: v for k, v in nutrition.items() if k != "Calories"}
        
        fig = go.Figure(data=[go.Pie(
            labels=list(macro_nutrition.keys()),
            values=list(macro_nutrition.values()),
            hole=0.5,
            marker=dict(colors=['skyblue', 'lightgreen', 'salmon']),
            hoverinfo="label+percent+value"
        )])
        fig.update_layout(title_text="Macronutrient Breakdown")
        
        st.plotly_chart(fig, use_container_width=True)
