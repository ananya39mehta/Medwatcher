import pandas as pd
from github import Github
import streamlit as st
from streamlit_option_menu import option_menu

# Hardcoded username and password
USERNAME = "admin"
PASSWORD = "admin"

# Function to add new patient
def add_new_patient(patient_id, name, age, gender, phone_number):
    # Load main.csv from GitHub
    g = Github("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")
    repo = g.get_repo("Medwatcher")
    contents = repo.get_contents("main.csv")
    main_csv = pd.read_csv(contents.download_url)

    # Check if patient_id already exists
    if patient_id in main_csv['Patient ID'].values:
        return "Error: Patient ID already exists"

    # Add new patient to main.csv
    new_patient = {'Patient ID': patient_id, 'Name': name, 'Age': age, 'Gender': gender, 'Phone Number': phone_number}
    main_csv = main_csv.append(new_patient, ignore_index=True)

    # Update main.csv on GitHub
    with open('main.csv', 'w') as f:
        main_csv.to_csv(f, index=False)
    repo.update_file(contents.path, "Updated main.csv", open('main.csv').read())

    # Create new patient CSV file
    patient_csv = pd.DataFrame(columns=['Date', 'Code', 'Glucose', 'Task'])
    patient_csv.to_csv(f'{patient_id}.csv', index=False)

    # Upload new patient CSV to GitHub
    repo.create_file(f'{patient_id}.csv', f"Added {patient_id}.csv", open(f'{patient_id}.csv').read())

    return "Patient added successfully"

# Function to delete patient
def delete_patient(patient_id):
    # Load main.csv from GitHub
    g = Github("YOUR_GITHUB_TOKEN")
    repo = g.get_repo("YOUR_REPOSITORY_NAME")
    contents = repo.get_contents("main.csv")
    main_csv = pd.read_csv(contents.download_url)

    # Check if patient_id exists
    if patient_id not in main_csv['Patient ID'].values:
        return "Error: Patient ID does not exist"

    # Remove patient from main.csv
    main_csv = main_csv[main_csv['Patient ID'] != patient_id]

    # Update main.csv on GitHub
    with open('main.csv', 'w') as f:
        main_csv.to_csv(f, index=False)
    repo.update_file(contents.path, "Updated main.csv", open('main.csv').read())

    # Delete patient CSV from GitHub
    repo.delete_file(f"{patient_id}.csv", f"Deleted {patient_id}.csv")

    return "Patient deleted successfully"

# Define the MultiApp class
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
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

            return

        with st.sidebar:
            app = option_menu(
                menu_title="MedWatcher",
                options=['Home', 'Add Patients', 'Delete Patients', 'About Us'],  # Added 'About Us' option
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            self.home()
        elif app == 'About Us':
            self.about_us()
        elif app == 'Add Patients':  
            self.add_patients() 
        elif app == 'Delete Patients':  
            self.delete_patients()   

    def home(self):
        st.write("# Home Page")
        st.write("Welcome to MedWatcher!")
        st.write("MedWatcher is a dashboard application designed to help diabetic patients and healthcare providers monitor and manage glucose levels effectively.")
        st.write("With MedWatcher, you can:")
        st.write("- View detailed patient information, including glucose data and relevant tasks.")
        st.write("- Analyze glucose trends over time with interactive charts.")
        st.write("- Receive alerts for glucose levels outside the normal range.")
        st.write("To get started, navigate using the sidebar on the left.")

    def about_us(self):
        st.write("# About Us")
        st.write("MedWatcher is a platform dedicated to improving diabetes management for patients and healthcare providers.")
        st.write("Our mission is to provide tools and insights to empower individuals to better understand and control their glucose levels.")
        st.write("For any inquiries or feedback, please contact us at contact@medwatcher.com.")
        st.write("## Meet the Team")
        st.write("**Dhwani Bhavankar** - dhwani.bhavankar.btech2022@sitpune.edu.in")
        st.write("**Ananya Mehta** - ananya39mehta@gmail.com")
        st.write("**Harsimran Kaur** - harsimrankaur2493@gmail.com")
        st.write("**Mayank Sahai** - smayank2412@gmail.com")

    def add_patients(self):
        st.write("# Add Patients")
        # Input fields for adding new patient
        patient_id = st.text_input("Patient ID")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=150)
        gender = st.selectbox("Gender", ["Male", "Female"])
        phone_number = st.text_input("Phone Number")

        # Button to add new patient
        if st.button("Add Patient"):
            result = add_new_patient(patient_id, name, age, gender, phone_number)
            st.write(result)

    def delete_patients(self):
        st.write("# Delete Patients")
        # Input field for deleting patient
        patient_id_to_delete = st.text_input("Patient ID to delete")

        # Button to delete patient
        if st.button("Delete Patient"):
            result = delete_patient(patient_id_to_delete)
            st.write(result)

# Create instance of MultiApp and add apps
multi_app = MultiApp()
multi_app.run()
