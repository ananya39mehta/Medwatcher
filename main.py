import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import alerts
from patients import patients  # Importing the patients function

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "admin"

# Load background image
@st.cache
def load_image(image_path):
    img = Image.open(image_path)
    return img

background_image = load_image("Login.jpeg")

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.image(background_image, use_column_width=True)

        st.write("# Welcome to MedWatcher")
        st.write("Please log in")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
            else:
                st.error("Incorrect username or password. Please try again.")

    return st.session_state.logged_in

def home():
    st.write("# Home Page")
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
                options=['Home', 'Patients', 'Alerts'],  # Added 'Patients' option
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
        elif app == 'Alerts':
            alerts.app()
        elif app == 'Patients':
            st.write("# Patients")
            patients()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
