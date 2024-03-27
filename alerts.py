import streamlit as st
import pandas as pd

def view_alerts():
    st.subheader("View Alerts")
    # Load alerts from database or any other source
    # For demo purposes, here's a sample list of alerts
    alerts = [
        {"ID": 1, "Message": "Alert 1: High Temperature"},
        {"ID": 2, "Message": "Alert 2: Low Oxygen Saturation"},
        {"ID": 3, "Message": "Alert 3: High Blood Pressure"}
    ]

    df = pd.DataFrame(alerts)
    df.index += 1  # Start indexing from one
    st.table(df.style.set_properties(**{'text-align': 'center'}))  # Remove height parameter

def add_alert():
    st.subheader("Add Alert")
    message = st.text_area("Alert Message")

    if st.button("Add"):
        new_alert = pd.DataFrame({"ID": [None], "Message": [message]})
        st.write("New Alert Added:")
        st.write(new_alert)

def delete_alert():
    st.subheader("Delete Alert")
    # You can provide options to select alerts for deletion
    # For demo purposes, let's assume we have a single alert to delete
    alert_to_delete = st.selectbox("Select alert to delete", ["Alert 1: High Temperature", "Alert 2: Low Oxygen Saturation", "Alert 3: High Blood Pressure"])

    if st.button("Delete"):
        # Delete alert from database or perform any other action
        st.success(f"Alert deleted: {alert_to_delete}")

def app():
    st.title("Alerts")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["View Alerts", "Add Alert", "Delete Alert"])

    if page == "View Alerts":
        view_alerts()
    elif page == "Add Alert":
        add_alert()
    elif page == "Delete Alert":
        delete_alert()

if __name__ == "__main__":
    app()
