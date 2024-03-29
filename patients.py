import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def patients():
    #st.write("## Patients Page")
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
            st.line_chart(glucose_data['Glucose'])

            st.write("### Glucose Graph:")
            

            # Filter points not between 50 and 180
            filtered_data = glucose_data[(glucose_data['Glucose'] < 50) | (glucose_data['Glucose'] > 180)]

            if not filtered_data.empty:
                st.write("### Points Outside 50-180 Range:")
                st.write(filtered_data)

                # Count occurrences of each task
                task_counts = filtered_data['Task'].value_counts()

                # Create a pie chart using Matplotlib
                fig, ax = plt.subplots()
                ax.pie(task_counts, labels=task_counts.index, autopct='%1.1f%%')
                ax.set_title("Tasks Leading to Deviations from 50-180 Range")
                
                # Display the pie chart using Streamlit
                st.write("### Tasks Leading to Deviations from 50-180 Range:")
                st.pyplot(fig)

        else:
            st.error("Patient ID not found.")

patients()
