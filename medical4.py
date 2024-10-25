import streamlit as st
import pandas as pd
import os

# Create a title for the app
st.title("User Data Collection App")

# Create a form with input fields
with st.form("user_data_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    height = st.number_input("height", min_value=0 , step=1)
    weight =st.number_input("weight", min_value=0, step=1)
    submit_button = st.form_submit_button("Submit")

# Create a CSV file to store the user data
csv_file = "ihub.csv"

# Check if the form has been submitted
if submit_button:
    # Create a dictionary to store the user data
    ihub = {"Name": name, "Age": age, "height": height,"weight":weight}

    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        # Create a new CSV file with the header row
        pd.DataFrame(columns=["Name", "Age" , "height","weight"]).to_csv(csv_file, index=False)

    # Append the new user data to the CSV file
    pd.DataFrame([ihub]).to_csv(csv_file, mode="a", header=False, index=False)

    # Display a success message
    st.success("Data submitted successfully!")

# Display a table with the collected user data
if os.path.exists(csv_file):
    user_data_df = pd.read_csv(csv_file)
    
else:
    st.write("No data collected yet!")
