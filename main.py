import streamlit as st
from streamlit_option_menu import option_menu
import patients, alerts, contacts

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

def about_us():
    st.write("## About Us")
    st.write("This is the About Us page.")
    st.write("Here, you can provide information about your application.")

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
            st.sidebar.write("## Menu")
            app = st.sidebar.radio("", ['Home', 'Patients', 'Alerts', 'Contacts', 'About Us'], index=1)

        if app == "Home":
            home()
        elif app == "Patients":
            patients.app()
        elif app == 'Alerts':
            alerts.app()
        elif app == 'Contacts':
            contacts.app()
        elif app == 'About Us':
            about_us()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
