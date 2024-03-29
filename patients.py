import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def patients():
    st.write("## Patients Page")
    patient_id = st.text_input("Enter Patient ID:")
    if patient_id:
        main_df = pd.read_csv("main.csv")
        patient_details = main_df[main_df['patientid'] == int(patient_id)]
        if not patient_details.empty:
            st.write("### Patient Details:")
            st.write(patient_details)

            # Plotting graphs related to glucose from respective PatientX.csv file
            patient_file = f"Patient{patient_id}.csv"
            glucose_data = pd.read_csv(patient_file)
            st.write("### Glucose Data:")
            st.write(glucose_data)
            st.write("### Glucose Graph:")
            plt.plot(glucose_data['Date'], glucose_data['Glucose'])
            st.pyplot(plt)

        else:
            st.error("Patient ID not found.")
