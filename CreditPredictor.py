# -*- coding: utf-8 -*-
"""
Created on Thu April 28 19:15:01 2023

@author: pranayak
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('F:/Projects/Credit card/trained_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Eligible for Credit'
    else:
      return 'Not Eligible for Credit'
  
    
  
def main():
    
    
    # giving a title
    st.title('Credit Allowance Predictor Web App')
    
    
    # getting the input data from the user
    duration = st.number_input('Age of the Person', min_value=0, max_value=120, step=1)
    duration = st.number_input('Duration (months)', min_value=0, max_value=96, step=1)
    credit_amount = st.number_input('Credit Amount (EUR)', min_value=0, max_value=20000, step=1)
    installment_commitment = st.number_input('Installment Commitment', min_value=0, max_value=4, step=1)
    residence_since = st.number_input('Residence Since (years)', min_value=0, max_value=4, step=1)
    age = st.number_input('Age (years)', min_value=18, max_value=100, step=1)
    existing_credits = st.number_input('Number of Existing Credits', min_value=0, max_value=4, step=1)
    num_dependents = st.number_input('Number of Dependents', min_value=0, max_value=2, step=1)
    checking_status_encoder = st.number_input('Checking Account Status', min_value=0, max_value=3, step=1)
    credit_history_encoder = st.number_input('Credit History', min_value=0, max_value=4, step=1)
    purpose_encoder = st.number_input('Purpose', min_value=0, max_value=9, step=1)
    savings_status_encoder = st.number_input('Savings Account/Bonds Status', min_value=0, max_value=4, step=1)
    employment_encoder = st.number_input('Employment Status', min_value=0, max_value=4, step=1)
    other_parties_encoder = st.number_input('Other Parties Involved', min_value=0, max_value=2, step=1)
    property_magnitude_encoder = st.number_input('Property Magnitude', min_value=0, max_value=3, step=1)
    other_payment_plans_encoder = st.number_input('Other Payment Plans', min_value=0, max_value=2, step=1)
    housing_encoder = st.number_input('Housing', min_value=0, max_value=2, step=1)
    job_encoder = st.number_input('Job', min_value=0, max_value=3, step=1)
    own_telephone_encoder = st.number_input('Own Telephone', min_value=0, max_value=1, step=1)
    foreign_worker_encoder = st.number_input('Foreign Worker', min_value=0, max_value=1, step=1)
    gender_encoder = st.number_input('Gender', min_value=0, max_value=1, step=1)
    marital_status_encoder = st.number_input('Marital Status', min_value=0, max_value=3, step=1)
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Check Credit Result'):
       
        diagnosis = diabetes_prediction([duration, credit_amount, installment_commitment, residence_since, age, existing_credits, num_dependents, checking_status_encoder, credit_history_encoder, purpose_encoder, savings_status_encoder, employment_encoder, other_parties_encoder, property_magnitude_encoder, other_payment_plans_encoder, housing_encoder, job_encoder, own_telephone_encoder, foreign_worker_encoder, gender_encoder, marital_status_encoder])

        
    st.success(diagnosis)
    
    predict_button = st.session_state.get('predict_button')
    if predict_button:
        st.markdown(f'<style>.css-3xq2te{{color: #FFF; background-color: #673AB7; border-radius: 0.75rem; padding: 0.6rem 1rem; font-size: 1rem; font-weight: 500; border: none;}}</style>', unsafe_allow_html=True)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  