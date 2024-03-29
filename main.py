import streamlit as st
from streamlit_option_menu import option_menu
import alerts
from patients import patients  # Importing the patients function

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "admin"

# Custom CSS styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
    }
    .stButton>button {
        background-color: #02ab21;
        color: white;
    }
    .stButton>button:hover {
        background-color: #028c19;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fgovinsider.asia%2Fintl-en%2Farticle%2Fdata-is-giving-rise-to-better-medical-practice-heres-how&psig=AOvVaw38OKVpTQ2gMtm7Keu46kyU&ust=1711819174055000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMjzlcX9mYUDFQAAAAAdAAAAABAJ");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
        st.write("<div align='center'><h1>Welcome to MedWatcher</h1></div>", unsafe_allow_html=True)
        st.markdown("---")
        st.write("<h2>Login</h2>", unsafe_allow_html=True)

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
