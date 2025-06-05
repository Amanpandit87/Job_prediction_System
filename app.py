import streamlit as st
import pandas as pd
import re
import string
import pickle

# Load model, transformer, and label encoder
model = pickle.load(open("Job_prediction_system.pkl", "rb"))
trans = pickle.load(open("column_transformer.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

# Text cleaning
def text_cleaning(text):
    text = text.lower()
    text = re.sub(r"\[.*?\]", " ", text)
    text = re.sub(r"\W", " ", text)
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<.*?>+", " ", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), " ", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\w*\d\w*", " ", text)
    return text

def remove_commas(text):
    return text.replace(",", "").lower()

# Streamlit GUI
st.title("💼 Job Role Prediction System")

salary = st.number_input("Expected Salary (in INR)", min_value=0)
experience = st.number_input("Experience (in Years)", min_value=0)
requirement = st.text_area("Job Requirement")
description = st.text_area("Job Description")

if st.button("Predict"):
    if not requirement or not description:
        st.error("Please enter both requirement and description.")
    else:
        req_clean = remove_commas(requirement)
        desc_clean = text_cleaning(description)

        input_df = pd.DataFrame({
            "salary": [salary],
            "experience": [experience],
            "requirment": [req_clean],
            "description": [desc_clean]
        })

        x_input = trans.transform(input_df)
        y_pred = model.predict(x_input)
        job_role = label_encoder.inverse_transform(y_pred)[0]

        st.success(f"Predicted Job Role: **{job_role}**")
