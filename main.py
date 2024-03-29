import streamlit as st
from streamlit_option_menu import option_menu
import alerts
from patients import patients  # Importing the patients function

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "admin"

# Custom CSS styles
st.markdown(
    f"""
    <style>
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
    .background-image {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("https://gov-web-sing.s3.ap-southeast-1.amazonaws.com/uploads/2023/1/Wordpress-featured-images-48-1672795987342.jpg");
        background-size: cover;
        opacity: 0.5; /* Adjust the opacity value here (0.5 for 50% opacity) */
        z-index: -1; /* Ensure the background image is behind other content */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
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
