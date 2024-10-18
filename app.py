import streamlit as st
import mysql.connector
from mysql.connector import Error

# Initialize session state to track user login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None

# Function to establish MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='blood',
            user='root',  # Replace with your DB username
            password='123456'  # Replace with your DB password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error while connecting to MySQL: {e}")
        return None

# Fetch data
def fetch_data(query):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        records = cursor.fetchall()
        connection.close()
        return records

# Add a new donor
def add_donor(name, number, mail, age, gender, blood_group, address):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        INSERT INTO donor_details (donor_name, donor_number, donor_mail, donor_age, donor_gender, donor_blood, donor_address)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, number, mail, age, gender, blood_group, address)
        cursor.execute(query, values)
        connection.commit()
        connection.close()
        st.success("Donor added successfully!")

# Registration Function
def register_user(name, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (name, password))
        connection.commit()
        connection.close()
        st.success("Registration successful! Please log in.")

# Login Function
def login_user(name, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (name, password))
        user = cursor.fetchone()
        connection.close()
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = name
            st.success(f"Welcome {name}, you are logged in!")
        else:
            st.error("Incorrect username or password.")

# Main Streamlit UI
def main():
    st.title("Blood Bank Management System")

    if not st.session_state['logged_in']:
        option = st.sidebar.selectbox("Login/Register", ["Login", "Register"])

        if option == "Login":
            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                login_user(username, password)

        elif option == "Register":
            st.subheader("Register")
            username = st.text_input("Enter your username")
            password = st.text_input("Enter your password", type="password")
            if st.button("Register"):
                register_user(username, password)

    else:
        st.subheader(f"Welcome {st.session_state['username']}!")

        # Menu options after login
        menu = ["Home", "View Donors", "Add Donor", "Logout"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Home":
            st.subheader("Welcome to the Blood Bank Management System")

        elif choice == "View Donors":
            st.subheader("List of Donors")
            donors = fetch_data("SELECT * FROM donor_details")
            if donors:
                for donor in donors:
                    st.write(f"Name: {donor['donor_name']}, Age: {donor['donor_age']}, Blood Group: {donor['donor_blood']}")
            else:
                st.info("No donors available.")

        elif choice == "Add Donor":
            st.subheader("Add a New Donor")
            donor_name = st.text_input("Donor Name")
            donor_number = st.text_input("Donor Contact Number")
            donor_mail = st.text_input("Donor Email")
            donor_age = st.number_input("Donor Age", min_value=18, max_value=65, step=1)
            donor_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            donor_blood = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
            donor_address = st.text_area("Donor Address")

            if st.button("Submit"):
                add_donor(donor_name, donor_number, donor_mail, donor_age, donor_gender, donor_blood, donor_address)

        elif choice == "Logout":
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.info("You have been logged out.")

if __name__ == '__main__':
    main()
