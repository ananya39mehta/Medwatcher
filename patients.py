import streamlit as st
import pandas as pd
import altair as alt

def patients():
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
            # Create a line chart using Altair
            line = alt.Chart(glucose_data.reset_index()).mark_line().encode(
                x='Date:T',
                y='Glucose:Q'
            ).properties(
                width=600,
                height=400
            )

            # Add horizontal lines
            hline_180 = alt.Chart(pd.DataFrame({'y': [180]})).mark_rule(color='red', strokeDash=[3,3]).encode(
                y='y:Q'
            )

            hline_50 = alt.Chart(pd.DataFrame({'y': [50]})).mark_rule(color='red', strokeDash=[3,3]).encode(
                y='y:Q'
            )

            st.write(alt.layer(line, hline_180, hline_50).properties(title='Glucose Graph'))

            # Filter points not between 50 and 180
            filtered_data = glucose_data[(glucose_data['Glucose'] < 50) | (glucose_data['Glucose'] > 180)]

            if not filtered_data.empty:
                st.write("### Points Outside 50-180 Range:")
                st.write(filtered_data)

                # Count occurrences of each task
                task_counts = filtered_data['Task'].value_counts().reset_index()
                task_counts.columns = ['Task', 'Count']

                # Create a pie chart using Altair
                pie_chart = alt.Chart(task_counts).mark_bar().encode(
                    x=alt.X('Task:N', title='Task'),
                    y=alt.Y('Count:Q', title='Count'),
                    tooltip=['Task', 'Count']
                ).properties(
                    width=600,
                    height=400
                )

                st.write("### Tasks Leading to Deviations from 50-180 Range:")
                st.write(pie_chart)

        else:
            st.error("Patient ID not found.")

patients()
