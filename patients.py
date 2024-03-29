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

            # Create an Altair line chart
            chart = alt.Chart(glucose_data).mark_line().encode(
                x='Time:T',  # Assuming 'Time' is the column containing time information
                y='Glucose:Q'  # Assuming 'Glucose' is the column containing glucose values
            ).properties(
                title='Glucose Graph'
            )
            st.write("### Glucose Graph:")
            st.altair_chart(chart, use_container_width=True)

        else:
            st.error("Patient ID not found.")

patients()
