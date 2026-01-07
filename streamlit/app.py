import pandas as pd
from fastai.tabular.all import *
import streamlit as st

# Load the trained model
learn = load_learner('/workspaces/codespaces-jupyter/streamlit/churn_model.pkl', cpu=True)

# Streamlit app
st.title('Churn Predictor')

# User inputs
tenure = st.number_input('Number of months: ', min_value=0, max_value=72)

contract = st.selectbox('Contract type:', ['Month-to-month', 'One year', 'Two year'])

monthly_charges = st.number_input('Amount paid each month: ', min_value=19, max_value=118)

internet_service = st.selectbox('Type of internet service:', ['DSL', 'Fiber optic', 'No'])

# Determine if internet-related services should be disabled
has_no_internet = (internet_service == 'No')

# Options for services
service_options = ['Yes', 'No', 'No internet service']

# Set locked index based on internet service availability
locked_index = 2 if has_no_internet else 0

online_sec = st.selectbox(
    'Online Security:', 
    options=service_options, 
    index=locked_index, 
    disabled=has_no_internet
)

payment_method = st.selectbox('Payment Method:', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

paperless_billing = st.selectbox('Paperless billing:', ['Yes', 'No'] )

total_charges = st.number_input(
    'Total Charges:', 
    min_value=19,
    max_value=8684,
    step=1
)

streaming_tv = st.selectbox(
    'Streaming TV:', 
    options=service_options, 
    index=locked_index, 
    disabled=has_no_internet
)

tech_support = st.selectbox(
    'Tech Support:', 
    options=service_options, 
    index=locked_index, 
    disabled=has_no_internet
)


# Prepare input data for prediction
input_data = {
    'tenure': tenure,
    'Contract': contract,
    'MonthlyCharges': monthly_charges,
    'InternetService': internet_service,
    'StreamingTV': streaming_tv,
    'OnlineSecurity': online_sec,
    'PaymentMethod': payment_method,
    'PaperlessBilling': paperless_billing,
    'TotalCharges': total_charges,
    'TechSupport': tech_support
}

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Make prediction on button click
if st.button('Predict Churn'):
    row, pred, probs = learn.predict(input_df.iloc[0])

    st.write(f"Prediction: {pred}")
    st.write(f"Probability: {probs}")