import streamlit as st
import numpy as np
import joblib

# Load models
reg_model = joblib.load('prs_predictor.pkl')
clf_model = joblib.load('pain_classifier.pkl')

# Title
st.title("PRS & Pain Prediction App")

st.write("Enter C1 to C4 values for a new person:")

# User input
# User input with 10-digit precision
c1 = st.number_input("C1", value=0.0, step=1e-10, format="%.10f")
c2 = st.number_input("C2", value=0.0, step=1e-10, format="%.10f")
c3 = st.number_input("C3", value=0.0, step=1e-10, format="%.10f")
c4 = st.number_input("C4", value=0.0, step=1e-10, format="%.10f")


# Predict button
if st.button("Predict"):
    input_data = np.array([[c1, c2, c3, c4]])

    # Predictions
    predicted_prs = reg_model.predict(input_data)[0]
    predicted_pain = clf_model.predict(input_data)[0]
    pain_label = "Pain" if predicted_pain == 1 else "No Pain"

    # Display results
    st.subheader("Results")
    st.write(f"**Predicted PRS**: {predicted_prs:.2f}")
    st.write(f"**Predicted Pain**: {pain_label}")
