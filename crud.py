import mysql.connector
import streamlit as st 
import mysql.connector


# Establishing the con to mysql server ( bassed on TiDB)---------------------------------------------

import mysql.connector
import streamlit as st

# Establishing MySQL connection---------------------------------------------
PROJECT_1 = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="7Z3SRE1xmB2xsHv.root",
    port=4000,
    password="593g7sDIAPe2H7Og",
    database="crud_1"
)

# Creating the cursor connection-------------------------------------------
mycursor = PROJECT_1.cursor()
print("Connection established")

# Creating the Streamlit application----------------------------------------------------------------
st.title("CRUD Operations with MySQL")

# Sidebar for CRUD options
option = st.sidebar.selectbox("Select your operation", ("Create", "Read", "Update", "Delete"))


# Perform selected CRUD operation---------------------------------------------------
if option == "Create":
    st.subheader("Create a Record")
    name = st.text_input("Please enter your name")
    email = st.text_input("Kindly enter your email ID")
    
    if st.button("Create Now"):
        if name and email:
            sql = "INSERT INTO users(name, email) VALUES(%s, %s)"
            val = (name, email)
            mycursor.execute(sql, val)
            PROJECT_1.commit()
            st.success("Record created successfully!")
        else:
            st.error("Please enter both Name and Email.")

elif option == "Read":
    st.subheader("Read Records")
    mycursor.execute("SELECT * FROM users")
    records = mycursor.fetchall()
    
    if records:
        for row in records:
            st.write(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    else:
        st.warning("No records found.")

elif option == "Update":
    st.subheader("Update a Record")
    user_id = st.number_input("Enter User ID to update", min_value=1, step=1)
    new_name = st.text_input("Enter new name")
    new_email = st.text_input("Enter new email")

    if st.button("Update Now"):
        if new_name and new_email:
            sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
            val = (new_name, new_email, user_id)
            mycursor.execute(sql, val)
            PROJECT_1.commit()
            st.success("Record updated successfully!")
        else:
            st.error("Please enter both new Name and Email.")

elif option == "Delete":
    st.subheader("Delete a Record")
    user_id = st.number_input("Enter User ID to delete", min_value=1, step=1)

    if st.button("Delete Now"):
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)
        mycursor.execute(sql, val)
        PROJECT_1.commit()
        st.success("Record deleted successfully!")


    
    
    
    
    
