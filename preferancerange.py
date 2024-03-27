import streamlit as st

def app():
    st.title("Preference Range")

    # Define the parameters and their initial ranges
    parameters = [
        {"name": "Heart Rate", "min_range": 60, "max_range": 100},
        {"name": "Blood Pressure", "min_range": 80, "max_range": 120},
        {"name": "Respiratory Rate", "min_range": 10, "max_range": 20},
        {"name": "Blood Glucose", "min_range": 70, "max_range": 110},
        {"name": "Oxygen Saturation", "min_range": 95, "max_range": 100},
        {"name": "Body Temperature", "min_range": 97, "max_range": 99}
    ]

    # Display sliders for each parameter
    for parameter in parameters:
        st.write(f"### {parameter['name']}")
        min_val = st.slider(f"Minimum {parameter['name']}", key=f"min_{parameter['name']}", min_value=0, max_value=150, value=parameter['min_range'])
        max_val = st.slider(f"Maximum {parameter['name']}", key=f"max_{parameter['name']}", min_value=0, max_value=150, value=parameter['max_range'])

        # Update the parameter dictionary with new ranges
        parameter['min_range'] = min_val
        parameter['max_range'] = max_val

    # Display button to apply preferences
    if st.button("Apply Preferences"):
        # Process preferences here
        with open("parameter_ranges.txt", "w") as file:
            file.write("Parameter Ranges:\n")
            for parameter in parameters:
                file.write(f"{parameter['name']}:\n")
                file.write(f"\tMinimum: {parameter['min_range']}\n")
                file.write(f"\tMaximum: {parameter['max_range']}\n")
                file.write("\n")

        st.markdown("[Download Parameter Ranges](./parameter_ranges.txt)")
app()


