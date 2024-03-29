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

            # Plot the glucose data using Altair chart
            chart = alt.Chart(glucose_data).mark_line().encode(
                x='Date:T',
                y='Glucose:Q'
            ).properties(
                width=600,
                height=400
            )

            # Label only every alternate three points on x-axis
            x_labels = glucose_data.iloc[::3]['Date'].tolist()

            # Render the chart with Altair and Streamlit
            st.altair_chart(chart, use_container_width=True)

            # Set x-axis labels
            st.write("### Glucose Graph:")
            st.write("Alternate three points on x-axis labeled:")
            st.write(x_labels)

        else:
            st.error("Patient ID not found.")

patients()
