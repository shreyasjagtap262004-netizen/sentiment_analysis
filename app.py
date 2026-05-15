import streamlit as st
import pickle
import numpy as np

# Load the model
def load_model():
    with open('sentiment.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# UI Setup
st.set_page_config(page_title="Sentiment Analysis App", layout="centered")
st.title("Sentiment Analysis")
st.write("Enter text below to predict whether the sentiment is Positive or Negative.")

# Input area
user_input = st.text_area("User Text", placeholder="Type your message here...")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            # IMPORTANT: Your model expects exactly 16 features.
            # You must use the same Vectorizer or feature extraction used during training.
            
            # Example Placeholder (Replace this with your actual vectorizer.transform):
            # processed_input = vectorizer.transform([user_input]) 
            
            # For demonstration, we assume you have a function or object that returns a (1, 16) array
            # If you don't have a vectorizer, you need to map your text to those 16 features here.
            
            # Placeholder for transformation logic:
            # features = transform_text_to_16_features(user_input)
            
            # Temporarily showing an error if features aren't defined
            st.error("Missing Preprocessing: Please define the vectorizer that converts text into the 16 features the model expects.")
            
            # Once you have 'features' as a numpy array of shape (1, 16):
            # prediction = model.predict(features)
            # st.success(f"Prediction: {prediction[0].upper()}")
            
        except Exception as e:
            st.error(f"Error during prediction: {e}")

# Sidebar info
st.sidebar.title("Model Info")
st.sidebar.info(f"Model Type: MultinomialNB\n\nExpected Features: 16")
