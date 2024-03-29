import streamlit as st
import sqlite3

# Create a connection to SQLite database
conn = sqlite3.connect('medwatcher.db')
c = conn.cursor()

# Create table to store user credentials
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

# Create table to store blood glucose data
c.execute('''CREATE TABLE IF NOT EXISTS blood_glucose
             (patient_id TEXT, glucose_level REAL, FOREIGN KEY(patient_id) REFERENCES users(username))''')
conn.commit()

def login(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone() is not None

def add_blood_glucose_data(patient_id, glucose_level):
    c.execute("INSERT INTO blood_glucose VALUES (?, ?)", (patient_id, glucose_level))
    conn.commit()

def main():
    st.sidebar.title("MedWatcher")
    page = st.sidebar.radio("Navigation", ["Login", "Add Blood Glucose Data"])

    if page == "Login":
        st.title("Login to MedWatcher")
        patient_id = st.text_input("Patient ID")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if login(patient_id, password):
                st.success("Logged in successfully!")
                st.sidebar.success("Logged in!")
            else:
                st.error("Incorrect patient ID or password. Please try again.")
    elif page == "Add Blood Glucose Data":
        st.title("Add Blood Glucose Data")
        if st.sidebar.button("Logout"):
            st.sidebar.warning("Logged out!")
        else:
            if st.sidebar.info("Enter Patient ID and Blood Glucose Level to add data:"):
                patient_id = st.text_input("Patient ID")
                glucose_level = st.number_input("Blood Glucose Level", min_value=0.0)

                if st.button("Submit"):
                    add_blood_glucose_data(patient_id, glucose_level)
                    st.success("Blood Glucose Data added successfully!")

if __name__ == "__main__":
    main()
