import streamlit as st
import pandas as pd
import pickle
from PIL import Image

st.title("Loan Approval Prediction")
img = Image.open("C:\\Users\\personal\\Desktop\\Machine Learning\\household image.png")
st.image(img)
#load the model
model = pickle.load(open("C:\\Users\\personal\\Desktop\\Machine Learning\\model.pkl",'rb'))
# Input fields
gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.number_input('Applicant Income')
coapplicant_income = st.number_input('Coapplicant Income')
loan_amount = st.number_input('Loan Amount')
loan_amount_term = st.number_input('Loan Amount Term in days')
credit_history = st.selectbox('Credit History', [1.0, 0.0])
property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

# Manual Mapping of Input Values
gender_mapped = 1 if gender == 'Male' else 0
married_mapped = 1 if married == 'Yes' else 0
education_mapped = 1 if education == 'Graduate' else 0
self_employed_mapped = 1 if self_employed == 'Yes' else 0
property_area_mapped = 2 if property_area == 'Urban' else 1 if property_area == 'Semiurban' else 0

# Prepare input data for prediction
input_data = pd.DataFrame({
    'Gender': [gender_mapped],
    'Married': [married_mapped],
    'Education': [education_mapped],
    'Self_Employed': [self_employed_mapped],
    'ApplicantIncome': [applicant_income],
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_amount_term],
    'Credit_History': [credit_history],
    'Property_Area': [property_area_mapped]
})
# Prediction button
if st.button('Predict Loan Approval'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success('Loan Approved')
    else:
        st.error('Loan Not Approved')