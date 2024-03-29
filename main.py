import streamlit as st
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
        pass

    def run(self):
        if not login():
            return

        st.sidebar.title("MedWatcher")
        app = st.sidebar.radio("Navigation", ['Home', 'Patients'])

        if app == "Home":
            home()
        elif app == "Patients":
            patients.app()
        elif app == 'Alerts':
            alerts.app()
        elif app == 'Contacts':
            contacts.app()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
