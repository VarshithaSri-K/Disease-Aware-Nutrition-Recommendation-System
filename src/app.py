import streamlit as st
import pickle
import pandas as pd

# Load model
with open("nutrition_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load disease mapping
with open("disease_map.pkl", "rb") as f:
    disease_map = pickle.load(f)

# Load recommendations
with open("recommendations.pkl", "rb") as f:
    recommendations = pickle.load(f)

st.title("Disease-Aware Nutrition Recommendation System")

# Input Fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

height = st.number_input("Height (cm)", value=170)

weight = st.number_input("Weight (kg)", value=70)

activity = st.selectbox(
    "Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active",
        "Extremely Active"
    ]
)

diet = st.selectbox(
    "Dietary Preference",
    [
        "Omnivore",
        "Vegetarian",
        "Vegan",
        "Pescatarian"
    ]
)

daily_calorie_target = st.number_input(
    "Daily Calorie Target",
    value=2000
)

protein = st.number_input("Protein", value=50)

sugar = st.number_input("Sugar", value=20.0)

sodium = st.number_input("Sodium", value=1500.0)

calories = st.number_input("Calories", value=2000)

carbohydrates = st.number_input(
    "Carbohydrates",
    value=250
)

fiber = st.number_input("Fiber", value=25.0)

fat = st.number_input("Fat", value=60)

# Encodings
gender_map = {
    "Female": 0,
    "Male": 1
}

activity_map = {
    "Extremely Active": 0,
    "Lightly Active": 1,
    "Moderately Active": 2,
    "Sedentary": 3,
    "Very Active": 4
}

diet_map = {
    "Omnivore": 0,
    "Pescatarian": 1,
    "Vegan": 2,
    "Vegetarian": 3
}

if st.button("Predict Disease"):

    input_data = pd.DataFrame([[
        age,
        gender_map[gender],
        height,
        weight,
        activity_map[activity],
        diet_map[diet],
        daily_calorie_target,
        protein,
        sugar,
        sodium,
        calories,
        carbohydrates,
        fiber,
        fat
    ]], columns=[
        'Ages',
        'Gender',
        'Height',
        'Weight',
        'Activity Level',
        'Dietary Preference',
        'Daily Calorie Target',
        'Protein',
        'Sugar',
        'Sodium',
        'Calories',
        'Carbohydrates',
        'Fiber',
        'Fat'
    ])

    prediction = model.predict(input_data)[0]

    disease = disease_map[prediction]

    st.success(f"Predicted Disease: {disease}")

    if disease in recommendations:

        st.subheader("Recommended Meals")

        st.write(
            f"🍽 Breakfast: {recommendations[disease]['Breakfast']}"
        )

        st.write(
            f"🥗 Lunch: {recommendations[disease]['Lunch']}"
        )

        st.write(
            f"🍛 Dinner: {recommendations[disease]['Dinner']}"
        )

        st.write(
            f"🍎 Snack: {recommendations[disease]['Snack']}"
        )