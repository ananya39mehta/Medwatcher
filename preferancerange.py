# preferancerange.py
import streamlit as st

def app():
    st.title("Preference Range")

    # Define the parameters and their initial ranges
    parameters = [
        {"name": "Parameter 1", "min_range": 0, "max_range": 100},
        {"name": "Parameter 2", "min_range": 0, "max_range": 100},
        {"name": "Parameter 3", "min_range": 0, "max_range": 100},
        {"name": "Parameter 4", "min_range": 0, "max_range": 100},
        {"name": "Parameter 5", "min_range": 0, "max_range": 100},
        {"name": "Parameter 6", "min_range": 0, "max_range": 100}
    ]

    # Display sliders for each parameter
    for parameter in parameters:
        st.write(f"### {parameter['name']}")
        min_val = st.slider("Minimum", min_value=0, max_value=100, value=parameter['min_range'])
        max_val = st.slider("Maximum", min_value=0, max_value=100, value=parameter['max_range'])

        # Update the parameter dictionary with new ranges
        parameter['min_range'] = min_val
        parameter['max_range'] = max_val

    # Display button to apply preferences
    if st.button("Apply Preferences"):
        # Process preferences here
        for parameter in parameters:
            st.write(f"{parameter['name']}: Min Range - {parameter['min_range']}, Max Range - {parameter['max_range']}")
app()