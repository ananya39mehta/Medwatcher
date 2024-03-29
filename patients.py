import streamlit as st
import pandas as pd
import altair as alt

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

            # Plot the glucose data using Altair
            chart = alt.Chart(glucose_data).mark_line().encode(
                x='Date:T',
                y='Glucose:Q',  # This encodes the 'Glucose' column as the y-axis values
                tooltip=['Date:T', 'Glucose:Q']  # This includes the 'Date' and 'Glucose' values in the tooltip
            ).properties(width=600, height=400)

            st.write("### Glucose Graph:")
            st.altair_chart(chart, use_container_width=True)

        else:
            st.error("Patient ID not found.")

patients()
