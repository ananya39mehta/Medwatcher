import streamlit as st
from streamlit_option_menu import option_menu
import patients, alerts, contacts
import pandas as pd

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "admin"

st.set_page_config(
    page_title="MedWatcher"
    # page_icon="C:\Users\asus\hackathonPICT\MedWatcher logo.jpg"
)

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.write("## Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password. Please try again.")

    return st.session_state.logged_in

def home():
    st.write("## Home Page")
    st.write("Welcome to MedWatcher!")
    st.write("Please navigate using the sidebar.")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        if not login():
            return

        with st.sidebar:
            app = option_menu(
                menu_title="MedWatcher",
                options=['Home', 'Patients', 'Alerts', 'Contacts'],  # Removed 'Individual Patient Data' option
                default_index=0,  # Set default index to 'Home'
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            home()
        elif app == "Patients":
            patient_data = patients.app()
            if patient_data is not None and isinstance(patient_data, pd.DataFrame):
                if not patient_data.empty:
                    st.subheader("Patient Information")
                    st.write(patient_data)
                else:
                    st.warning("Patient not found.")
            else:
                st.error("Error fetching patient data.")
        elif app == 'Alerts':
            alerts.app()
        elif app == 'Contacts':
            contacts.app()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
