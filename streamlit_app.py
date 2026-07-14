import streamlit as st
import pickle


st.set_page_config(page_title="Predictor",page_icon="💰")
st.title("DA11 Salary Predictor")


with open("model.pkl", "rb") as file:
    model = pickle.load(file)

yoe = st.number_input(label="Enter years of experience", min_value=1, max_value=10)

if st.button("Predict"):
    prediction = model.predict([[yoe]])
    st.success(prediction[0])