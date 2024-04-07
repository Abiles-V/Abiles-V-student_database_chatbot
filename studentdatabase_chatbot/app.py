from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3
import openai

## Set your OpenAI API Key
openai.api_key ="openaiapikey"

## Function to authenticate user
def authenticate(username, password, department):
    # You may want to replace this with a more secure authentication mechanism
    # For simplicity, we'll use hardcoded usernames and passwords
    ai_department_users = {"user1": "password1", "user2": "password2"}
    data_science_department_users = {"user3": "password3", "user4": "password4"}

    if department == "AI":
        if username in ai_department_users and ai_department_users[username] == password:
            return True
    elif department == "Data Science":
        if username in data_science_department_users and data_science_department_users[username] == password:
            return True
    
    return False

## Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

## Streamlit App
st.set_page_config(page_title="Analytical Query Chatbot")
st.header("Analytical Query Chatbot")

# User authentication
username = st.text_input("Username: ")
password = st.text_input("Password: ", type="password")
department = st.selectbox("Select Department", ["AI", "Data Science"])

form = st.form(key='query_form')
question = form.text_input("Input: ", key="input")

# Add submit button
submit_button = form.form_submit_button("Ask the question")

# Only display "Ask the question" button if a question is entered
if question and submit_button:
    if authenticate(username, password, department):
        st.success("Login Successful!")

        # Generate SQL query using GPT-3.5
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Use Davinci for better understanding
            prompt=f"Faculty {department} asks: {question}\nSQL query:",
            max_tokens=100,
            stop=None
        )
        sql_query = response.choices[0].text.strip()
        
        # Execute SQL query and retrieve data
        data = read_sql_query(sql_query, "student.db")
        
        # Display response
        st.subheader("The Response is")
        for row in data:
            st.write(row)
    else:
        st.error("Login Failed. Invalid username or password.")
