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

            # Print columns of the glucose_data DataFrame
            st.write("### Glucose Data Columns:")
            st.write(glucose_data.columns.tolist())

            # Assuming 'Time' is the column containing time information
            glucose_data['Time'] = pd.to_datetime(glucose_data['Time'])
            glucose_data.set_index('Time', inplace=True)

            st.write("### Glucose Data:")
            st.write(glucose_data)

            st.write("### Glucose Graph:")
            st.line_chart(glucose_data['Glucose'])

        else:
            st.error("Patient ID not found.")

patients()
