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

            # Assuming 'Time' is the column containing time information
            glucose_data['Date'] = pd.to_datetime(glucose_data['Date'])
            glucose_data.set_index('Date', inplace=True)

            st.write("### Glucose Data:")
            st.write(glucose_data)

            st.write("### Glucose Graph:")
            chart = st.line_chart(glucose_data['Glucose'])
            # Add horizontal lines
            hline_180 = alt.Chart(pd.DataFrame({'y': [180]})).mark_rule(color='red', strokeDash=[3,3]).encode(
                y='y:Q'
            )

            hline_50 = alt.Chart(pd.DataFrame({'y': [50]})).mark_rule(color='red', strokeDash=[3,3]).encode(
                y='y:Q'
            )

        else:
            st.error("Patient ID not found.")

patients()
