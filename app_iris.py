import streamlit as st
import numpy as np
import pickle
from sklearn import datasets
from PIL import Image

# Load the trained model
model = pickle.load(open("iris_model.pkl", "rb"))

# Set title
st.title("Iris Flower Classification 🌸")

# Input features
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.2)

# Convert inputs into numpy array
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Make prediction
prediction = model.predict(features)[0]
class_names = ["Setosa", "Versicolor", "Virginica"]
predicted_class = class_names[prediction]

# Display prediction result
st.write(f"### 🌼 Predicted Flower Type: {predicted_class}")

# Flower Images
image_dict = {
    "Setosa": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Iris_setosa_2.jpg",
    "Versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "Virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
}

# Show corresponding flower image
st.image(image_dict[predicted_class], caption=f"{predicted_class} Flower", use_column_width=True)
