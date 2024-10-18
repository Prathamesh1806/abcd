import streamlit as st

# Initialize session state to track user login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}
if 'donor_data' not in st.session_state:
    st.session_state['donor_data'] = []

# Simulated database (dictionary) to store registered users
user_database = st.session_state['user_data']
donor_database = st.session_state['donor_data']

# Registration Function
def register_user(name, password):
    if name in user_database:
        st.warning("User already exists! Try logging in.")
    else:
        user_database[name] = {'password': password}  # Removed mobile number
        st.success("Registration successful! Please log in.")

# Login Function
def login_user(name, password):
    if name in user_database and user_database[name]['password'] == password:
        st.session_state['logged_in'] = True
        st.session_state['username'] = name
        st.success(f"Welcome {name}, you are logged in!")
    else:
        st.error("Incorrect username or password. Please try again.")

# Logout Function
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = None
    st.info("You have been logged out.")

# Donate Function
def donate_blood(name, blood_group, disease_status):
    donor_database.append({
        'name': name,
        'blood_group': blood_group,
        'disease': disease_status
    })
    st.success("Donation information saved successfully!")

# Receive Function
def find_donors(blood_group):
    donors = [donor for donor in donor_database if donor['blood_group'] == blood_group]
    if donors:
        st.write("Here are the available donors:")
        for donor in donors:
            st.write(f"Name: {donor['name']}, Blood Group: {donor['blood_group']}, Disease Status: {donor['disease']}")
    else:
        st.info("No donors available for this blood group.")

# Main Logic
st.title("Blood Bank Management System")

if not st.session_state['logged_in']:
    # Option to choose between Login or Registration
    option = st.sidebar.selectbox("Choose Action", ["Login", "Register"])

    if option == "Login":
        st.subheader("Login to your account")
        name = st.text_input("Enter your name")
        password = st.text_input("Enter your password", type="password")

        if st.button("Login"):
            login_user(name, password)

    elif option == "Register":
        st.subheader("Register a new account")
        name = st.text_input("Enter your name for registration")
        password = st.text_input("Enter your password", type="password")

        if st.button("Register"):
            register_user(name, password)

else:
    # After login, show the welcome page
    st.subheader(f"Welcome {st.session_state['username']}!")
    st.write("What would you like to do?")

    action = st.selectbox("Choose Action", ["Donate", "Receive"])

    if action == "Donate":
        st.subheader("Donate Blood")
        blood_group = st.selectbox("Select your blood group", ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        disease_status = st.radio("Do you have any blood-related disease or disorder?", ("Yes", "No"))

        if st.button("Submit Donation"):
            donate_blood(st.session_state['username'], blood_group, disease_status)

    elif action == "Receive":
        st.subheader("Receive Blood")
        blood_group_needed = st.selectbox("Select the blood group you need", ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])

        if st.button("Find Donors"):
            find_donors(blood_group_needed)

    # Logout option
    if st.button("Logout"):
        logout()
