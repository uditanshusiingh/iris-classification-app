import streamlit as st
import pickle
import numpy as np
from sklearn import datasets

# Load the trained model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.title("🌸 Iris Flower Classification App")

st.write("""
### Enter the flower details below:
Adjust the values using the sliders and click 'Predict' to classify the flower.
""")

# User input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.2)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.1)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)

# Make prediction
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    
    # Convert numerical prediction to flower name
    iris = datasets.load_iris()
    class_name = iris.target_names[prediction]

    st.success(f"🌼 Predicted Flower: **{class_name}**")


