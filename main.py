import streamlit as st
from streamlit_option_menu import option_menu
import patients, preferancerange, alerts, contacts


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
                options=['Patients', 'Preferance Range', 'Alerts', 'Contacts'],
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

if _name_ == "_main_":
    multi_app = MultiApp()
    multi_app.run()
