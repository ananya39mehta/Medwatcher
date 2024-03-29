import streamlit as st
import mysql.connector
from datetime import datetime

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mayank@0501",
    database="stmw"
)

cursor = db.cursor()

# Function to create patient table
def create_patient_table(patient_id):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {patient_id} (date VARCHAR(15), glucose float , task VARCHAR(255))")
    db.commit()

# Function to insert patient data
def insert_data(username, glucose, task):
    table_name = f"{username}"
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task = task_labels[task] if task in task_labels else "Unknown Task"
    cursor.execute(f"INSERT INTO {table_name} (date ,glucose, task) VALUES (%s, %s, %s)", (date, glucose, task))
    db.commit()

# Dictionary of pre-made usernames and passwords for both patients and doctors
user_credentials = {
    "p1": "password1",
    "p2": "password2",
    "p3": "password3"
}

# Dictionary mapping task IDs to their corresponding task labels
task_labels = {
    33: "Regular insulin dose",
    34: "NPH insulin dose",
    35: "UltraLente insulin dose",
    36: "Unspecified blood glucose measurement",
    37: "Pre-breakfast blood glucose measurement",
    38: "Post-breakfast blood glucose measurement",
    39: "Pre-lunch blood glucose measurement",
    40: "Post-lunch blood glucose measurement",
    41: "Pre-supper blood glucose measurement",
    42: "Post-supper blood glucose measurement",
    43: "Pre-snack blood glucose measurement",
    44: "Hypoglycemic symptoms",
    45: "Typical meal ingestion",
    46: "More-than-usual meal ingestion",
    47: "Less-than-usual meal ingestion",
    48: "Typical exercise activity",
    49: "More-than-usual exercise activity",
    50: "Less-than-usual exercise activity",
    51: "Unspecified special event"
}

# Main function for Streamlit app
def main():
    st.title("Patient Monitoring System")

    # Session State to keep track of user state
    session_state = st.session_state
    if 'logged_in' not in session_state:
        session_state.logged_in = False

    # Login section
    if not session_state.logged_in:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in user_credentials and password == user_credentials[username]:
                session_state.logged_in = True
                session_state.username = username
                st.success("Login successful!")
            else:
                st.error("Invalid username or password. Please try again.")

    # If user is logged in
    else:
        # Check if logged in user is a doctor
        if session_state.username.startswith("login"):
            st.sidebar.subheader(f"Welcome, {session_state.username}")
            st.sidebar.write("You are logged in as a doctor.")
            if st.sidebar.button("Logout"):
                session_state.logged_in = False
                st.success("Logged out successfully!")
                st.experimental_rerun()
        # Otherwise, user is a patient
        else:
            st.sidebar.subheader(f"Welcome, {session_state.username}")
            st.sidebar.write("You are logged in as a patient.")
            if st.sidebar.button("Logout"):
                session_state.logged_in = False
                st.success("Logged out successfully!")
                st.experimental_rerun()

            # Data submission form
            st.subheader("Enter Patient Data")
            blood_sugar = st.number_input("Blood Sugar Level")
            task_id = st.selectbox("Task", list(task_labels.keys()), format_func=lambda x: task_labels[x])

            if st.button("Submit"):
                insert_data(session_state.username, blood_sugar, task_id)
                st.success("Data submitted successfully!")

if __name__ == '__main__':
    main()
