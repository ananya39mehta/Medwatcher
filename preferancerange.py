import streamlit as st

def app():
    st.title("Patients Matching Preference Range")

    # Allow user to input preference range
    parameters = [
        "Heart rate",
        "Systolic blood pressure",
        "Diastolic blood pressure",
        "Respiratory rate",
        "Blood glucose",
        "Oxygen saturation",
        "Body temperature"
    ]
    preference_range = {}
    for parameter in parameters:
        min_val = st.slider(f"Minimum {parameter}", key=f"min_{parameter}", min_value=0, max_value=200, value=0)
        max_val = st.slider(f"Maximum {parameter}", key=f"max_{parameter}", min_value=0, max_value=200, value=200)
        preference_range[parameter] = (min_val, max_val)

    # Read main CSV file
    main_df = pd.read_csv("main.csv")

    # Initialize an empty DataFrame to store matching patients' details
    matching_patients_details = pd.DataFrame(columns=main_df.columns)

    # Iterate through each patient's data
    for index, row in main_df.iterrows():
        # Get the patient's ID
        patient_id = row['Patient ID']
        # Read the patient's individual CSV file
        patient_data_filename = f"{patient_id}.csv"
        try:
            patient_data_df = pd.read_csv(patient_data_filename, parse_dates=[0])
            # Get the last record of patient's data
            last_record = patient_data_df.iloc[-1]
            # Check if the last record matches the preference range for all parameters
            match_preference = True
            for parameter in parameters:
                if not (preference_range[parameter][0] <= last_record[parameter] <= preference_range[parameter][1]):
                    match_preference = False
                    break
            if match_preference:
                matching_patients_details = matching_patients_details.append(row)
        except FileNotFoundError:
            pass

    # Display matching patients' details
    if not matching_patients_details.empty:
        st.write(matching_patients_details)
    else:
        st.write("No patients found matching the preference range.")
app()


