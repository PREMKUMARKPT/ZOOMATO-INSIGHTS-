import streamlit as st
import mysql.connector

# Establish Database Connection
conn = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="7Z3SRE1xmB2xsHv.root",
    port=4000,
    password="593g7sDIAPe2H7Og",
    database="PROJECT_1"
)
cursor = conn.cursor()

# Streamlit UI
st.title("Simple SQL Query Explorer")

# Query Selection
query_options = {
    "1. View All Customers": "SELECT * FROM customers;",
    "2. View Customer Names & Emails": "SELECT name, email FROM customers;",
    "3. Count Customers by City": "SELECT city, COUNT(*) FROM customers GROUP BY city;",
    "4. View All Orders": "SELECT * FROM orders;",
    "5. View Orders with Customer ID & Total": "SELECT customer_id, total_amount FROM orders;",
    "6. Count Orders by Status": "SELECT status, COUNT(*) FROM orders GROUP BY status;",

    "7. View All Order Details": "SELECT * FROM order_details;",
    "8. View Food Items for Each Order": "SELECT order_id, food_item FROM order_details;",
    "9. Count Orders for Each Food Item": "SELECT food_item, COUNT(*) FROM order_details GROUP BY food_item;"
}

selected_query = st.selectbox("Choose a Query:", list(query_options.keys()))

# Execute Query
if st.button("Run Query"):
    query = query_options[selected_query]
    cursor.execute(query)
    result = cursor.fetchall()
    
    if result:
        st.write("### Query Results:")
        st.table(result)
    else:
        st.write("No data found.")

# Close Database Connection
cursor.close()
conn.close()
