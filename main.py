import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(
    page_title="MedWatcher"
    # page_icon="C:\Users\asus\hackathonPICT\MedWatcher logo.jpg"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="MedWatcher",
                options=['Patients', 'Preferance Range', 'Alerts', 'Contacts', 'Individual Patient Data'],  # Added 'Individual Patient Data' option
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Patients":
            display_all_patients()

        elif app == "Preferance Range":
            display_patients_by_preference()

        # Add other app sections as needed

def display_all_patients():
    st.write("### All Patients")

    # Read main CSV file
    main_df = pd.read_csv("main.csv")

    # Display all patients
    st.write(main_df)

def display_patients_by_preference():
    st.write("### Patients Matching Preference Range")

    # Allow user to input preference range
    preference_range = st.slider("Enter Preference Range", min_value=0, max_value=100, value=(0, 100))

    # Read main CSV file
    main_df = pd.read_csv("main.csv")

    # Initialize an empty list to store patients matching the preference range
    matching_patients = []

    # Iterate through each patient's data
    for index, row in main_df.iterrows():
        # Get the patient's ID
        patient_id = row['Patient ID']
        # Read the patient's individual CSV file
        patient_data_filename = f"{patient_id}.csv"
        patient_data_df = pd.read_csv(patient_data_filename)
        # Check if the last record matches the preference range
        last_record = patient_data_df.iloc[-1]
        if all(preference_range[0] <= value <= preference_range[1] for value in last_record.values):
            matching_patients.append(row)

    # Display matching patients
    if matching_patients:
        matching_patients_df = pd.DataFrame(matching_patients)
        st.write(matching_patients_df)
    else:
        st.write("No patients found matching the preference range.")

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
