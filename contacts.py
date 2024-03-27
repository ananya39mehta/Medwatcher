import streamlit as st
import pandas as pd

def add_contact():
    st.subheader("Add Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")

    if st.button("Add"):
        new_contact = pd.DataFrame({"Name": [name], "Phone": [phone], "Email": [email]})
        st.write("New Contact Added:")
        st.write(new_contact)

def view_contacts():
    st.subheader("View Contacts")
    # Load contacts from database or any other source
    # For demo purposes, here's a sample list of contacts
    contacts = [
        {"Name": "John Doe", "Phone": "123-456-7890", "Email": "john@example.com"},
        {"Name": "Jane Smith", "Phone": "987-654-3210", "Email": "jane@example.com"},
        {"Name": "Alice Johnson", "Phone": "555-555-5555", "Email": "alice@example.com"}
    ]

    df = pd.DataFrame(contacts)
    df.index += 1  # Start indexing from one
    st.write(df.to_html(index=False), unsafe_allow_html=True)  # Render DataFrame as HTML

def delete_contact():
    st.subheader("Delete Contact")
    # You can provide options to select contacts for deletion
    # For demo purposes, let's assume we have a single contact to delete
    contact_to_delete = st.selectbox("Select contact to delete", ["John Doe", "Jane Smith", "Alice Johnson"])

    if st.button("Delete"):
        # Delete contact from database or perform any other action
        st.success(f"Contact deleted: {contact_to_delete}")

def app():
    st.title("Contacts")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Add Contact", "View Contacts", "Delete Contact"])

    if page == "Add Contact":
        add_contact()
    elif page == "View Contacts":
        view_contacts()
    elif page == "Delete Contact":
        delete_contact()

if __name__ == "__main__":
    app()

