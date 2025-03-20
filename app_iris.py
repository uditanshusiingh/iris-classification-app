import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Load the trained model
model = pickle.load(open("iris_model.pkl", "rb"))

# Flower names and corresponding images
flower_info = {
    "Iris Setosa": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Iris_setosa_2.jpg",
    "Iris Versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "Iris Virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
}

# Streamlit UI
st.title("🌸 Iris Flower Predictor")

st.write("Enter the flower measurements below to predict its type.")

# User inputs
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.2)

# Prepare input features
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict the flower type
prediction = model.predict(features)[0]
flower_names = ["Iris Setosa", "Iris Versicolor", "Iris Virginica"]
predicted_flower = flower_names[prediction]

# Display Prediction
st.subheader(f"🌼 Predicted Flower: {predicted_flower}")
st.image(flower_info[predicted_flower], caption=f"{predicted_flower}", use_column_width=True)
