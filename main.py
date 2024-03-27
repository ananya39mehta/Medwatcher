import streamlit as st
from streamlit_option_menu import option_menu
import patients, preferancerange, alerts, contacts
import pandas as pd

st.set_page_config(
    page_title="MedWatcher"
    # page_icon="C:\Users\asus\hackathonPICT\MedWatcher logo.jpg"
)

class MultiApp:
    def _init_(self):
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
            patients.app()
        elif app == "Preferance Range":
            preferancerange.app()
        elif app == 'Alerts':
            alerts.app()
        elif app == 'Contacts':
            contacts.app()
        elif app == 'Individual Patient Data':
            display_individual_patient_data()

def display_individual_patient_data():
    st.write("### Individual Patient Data")

    # Allow user to input patient ID
    patient_id = st.text_input("Enter Patient ID:")
    
    # Read main CSV file
    main_df = pd.read_csv("main.csv")

    # Read individual patient CSV file based on entered patient ID
    filename = f"{patient_id}.csv"
    try:
        patient_data_df = pd.read_csv(filename)
        patient_info = main_df[main_df["Patient ID"] == int(patient_id)].iloc[0]
        
        # Display patient information
        st.write("#### Patient Information:")
        st.write(f"*Name:* {patient_info['Name']}")
        st.write(f"*Age:* {patient_info['Age']}")
        st.write(f"*Gender:* {patient_info['Gender']}")
        st.write(f"*Label:* {patient_info['Label']}")
        
        # Display graphs related to patient's health data
        st.write("#### Health Data:")
        # Add code here to display graphs based on patient's health data
        # For example:
        st.line_chart(patient_data_df['Heart rate'])
        st.line_chart(patient_data_df['Systolic blood pressure'])
    except FileNotFoundError:
        st.write("Please enter a valid Patient ID.")

if _name_ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
