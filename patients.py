import streamlit as st
import pandas as pd

def patients():
    st.write("## Patients Page")
    patient_id = st.text_input("Enter Patient ID:")
    if patient_id:
        main_df = pd.read_csv("main.csv")
        patient_details = main_df[main_df['Patient ID'] == int(patient_id)]
        if not patient_details.empty:
            st.write("### Patient Details:")
            st.write(patient_details)

            # Plotting graphs related to glucose from respective PatientX.csv file
            patient_file = f"Patient{patient_id}.csv"
            glucose_data = pd.read_csv(patient_file)
            st.write("### Glucose Data:")
            st.write(glucose_data)

            # Plot only every alternate three labels on the x-axis
            glucose_data_subset = glucose_data.iloc[::3, :]  # Select every alternate three rows
            st.write("### Glucose Graph:")
            st.line_chart(glucose_data_subset.set_index('Date')['Glucose'])

        else:
            st.error("Patient ID not found.")

patients()
