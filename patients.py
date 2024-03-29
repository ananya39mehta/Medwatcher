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

            # Plot the glucose data
            st.write("### Glucose Graph:")
            glucose_chart = st.line_chart(glucose_data.set_index('Date')['Glucose'])

            # Customize x-axis ticks to display only every alternate three labels
            num_ticks = len(glucose_data)
            x_ticks = glucose_data.index[::3]  # Select every alternate three indices
            glucose_chart.pyplot().set_xticks(range(num_ticks))
            glucose_chart.pyplot().set_xticklabels(glucose_data['Date'][::3], rotation=45, ha='right')

        else:
            st.error("Patient ID not found.")

patients()
