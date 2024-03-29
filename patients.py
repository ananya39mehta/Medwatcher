import streamlit as st
import pandas as pd

def search_patient(patients_df, search_id):
    result = patients_df[patients_df["Patient ID"] == search_id]
    return result if not result.empty else None

def display_patient_info(patient_data):
    st.subheader("Patient Information")
    if patient_data is not None:
        st.write(patient_data)
    else:
        st.warning("Patient not found.")

def modify_patient_history(patient_data):
    st.subheader("Modify Patient History")
    if patient_data is not None:
        # Add functionality to modify patient history
        st.write("Patient history modification feature coming soon...")
    else:
        st.warning("Patient not found.")

def display_patient_phone_number(patient_data):
    st.subheader("Patient Phone Number")
    if patient_data is not None:
        phone_number = patient_data.iloc[0]["Phone Number"]
        st.write(f"Phone Number: {phone_number}")
    else:
        st.warning("Patient not found.")

def app():
    st.title("Patients")

    patients_data = pd.DataFrame({
        "Patient ID": [101, 102, 103],
        "Name": ["John Doe", "Jane Smith", "Alice Johnson"],
        "Age": [30, 35, 40],
        "Phone Number": ["123-456-7890", "987-654-3210", "555-555-5555"],
        "History": ["History 1", "History 2", "History 3"]
    })

    search_id = st.text_input("Search Patient ID")
    if st.button("Search"):
        patient_info = search_patient(patients_data, int(search_id))
        display_patient_info(patient_info)
        display_patient_phone_number(patient_info)
        modify_patient_history(patient_info)

if __name__ == "__main__":
    app()
