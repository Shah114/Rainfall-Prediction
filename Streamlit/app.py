# Importing Modules
import streamlit as st
import pickle
import pandas as pd

# Load the trained model and feature names
with open('model/rainfall_prediction.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data["model"]
feature_names = model_data["feature_names"]

# Streamlit app
st.title("Rainfall Prediction🌦️")

st.sidebar.header("Input Features")
# Create input fields for each feature
input_data = []
for feature in feature_names:
    value = st.sidebar.number_input(
        f"Enter value for {feature}",
        value=0.0 if feature != "Humidity" else 50.0  # Example default values
    )
    input_data.append(value)

# Predict button
if st.button("Predict"):
    try:
        # Create DataFrame for prediction
        input_df = pd.DataFrame([input_data], columns=feature_names)
        
        # Make prediction
        prediction = model.predict(input_df)
        result = "Rainfall" if prediction[0] == 1 else "No Rainfall"
        
        # Display result
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
