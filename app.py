import streamlit as st
import numpy as np


st.title("Welcome to the Heart Disease predicting Model")
st.info("Note: This is just for Educational/Research Purposes and should not be used to account for anything serious")
st.write("Made by: Syed Fazeel")


def predict_heart_disease(age, alco, cigs):
    # These are the coefficients you calculated in your analysis
    intercept = -8.7705
    b_age = 0.0906
    b_alco = 0.0884
    b_cigs = 0.0481

    # Logistic Regression Formula (z)
    z = intercept + (b_age * age) + (b_alco * alco) + (b_cigs * cigs)

    # Sigmoid function to get probability
    probability = 1 / (1 + np.exp(-z))
    return probability * 100


col1, col2 = st.columns(2)

with col1:
    st.header("Enter Details")
    user_age = st.number_input("Age", min_value=1, max_value=120, value=25)
    user_alco = st.slider("Alcohol consumption (Liters/week)", 0.0, 40.0, 1.0)
    user_cigs = st.slider("Cigarettes per week", 0, 500, 0)

with col2:
    st.header("Prediction Result")
    if st.button("Calculate Probability"):
        result = predict_heart_disease(user_age, user_alco, user_cigs)

        # Display the result with a metric
        st.metric(label="Risk Likelihood", value=f"{result:.2f}%")

        # Progress bar for visual effect
        st.progress(int(result))

        if result > 50:
            st.error("High Risk Detected based on this model.")
        else:
            st.success("Low Risk Detected based on this model.")

        st.caption("Model Pseudo R-square: 0.1182 (Acceptably good accuracy)")