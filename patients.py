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

            # Assuming 'Date' is the column containing date information
            glucose_data['Date'] = pd.to_datetime(glucose_data['Date'])
            glucose_data.set_index('Date', inplace=True)

            st.write("### Glucose Data:")
            st.write(glucose_data)

            st.write("### Glucose Graph:")
            # Create Altair line chart
            line = alt.Chart(glucose_data.reset_index()).mark_line().encode(
                x='Date:T',
                y='Glucose:Q'
            ).properties(
                width=600,
                height=400
            )

            # Add horizontal lines
            hline_180 = alt.Chart(pd.DataFrame({'y': [180]})).mark_rule(color='red', strokeDash=[3,3], strokeWidth=2).encode(
                y='y:Q'
            )

            hline_50 = alt.Chart(pd.DataFrame({'y': [50]})).mark_rule(color='red', strokeDash=[3,3], strokeWidth=2).encode(
                y='y:Q'
            )

            st.write(alt.layer(line, hline_180, hline_50).properties(title='Glucose Graph'))

            # Filter points not between 50 and 180
            filtered_data = glucose_data[(glucose_data['Glucose'] < 50) | (glucose_data['Glucose'] > 180)]

            if not filtered_data.empty:
                st.write("### Points Outside 50-180 Range:")
                st.write(filtered_data)

                # Create Altair scatter plot
                scatter = alt.Chart(filtered_data.reset_index()).mark_circle(color='red').encode(
                    x='Date:T',
                    y='Glucose:Q',
                    tooltip=['Date', 'Glucose', 'Task']
                ).properties(
                    width=600,
                    height=400
                ).interactive()

                st.write("### Points Outside 50-180 Range Graph:")
                st.write(scatter)

        else:
            st.error("Patient ID not found.")

patients()
