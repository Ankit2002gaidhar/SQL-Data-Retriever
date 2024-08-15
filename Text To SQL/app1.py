from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key="Google API")

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
   The SQL database is named STUDENT and has the following columns: NAME, CLASS, SECTION, and MARKS.

For example:

1. "How many entries of records are present?" 
   The SQL command will be: SELECT COUNT(*) FROM STUDENT;

2. "Tell me all the students studying in Data Science class."
   The SQL command will be: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

3. "Rank students based on their marks within each class."
   The SQL command will be: 
   SELECT NAME, CLASS, MARKS, 
          RANK() OVER (PARTITION BY CLASS ORDER BY MARKS DESC) AS RANK 
   FROM STUDENT;

4. "Show the average marks for each class along with the difference from the highest marks in that class."
   The SQL command will be:
   SELECT CLASS, AVG(MARKS) AS AVG_MARKS, 
          MAX(MARKS) - AVG(MARKS) AS DIFF_FROM_MAX 
   FROM STUDENT 
   GROUP BY CLASS;

5. "Retrieve all students who have marks higher than the average marks in their class."
   The SQL command will be:
   SELECT NAME, CLASS, MARKS 
   FROM STUDENT 
   WHERE MARKS > (SELECT AVG(MARKS) FROM STUDENT WHERE CLASS = STUDENT.CLASS);

6. "Display the cumulative sum of marks for students in Data Science class."
   The SQL command will be:
   SELECT NAME, MARKS, 
          SUM(MARKS) OVER (ORDER BY MARKS) AS CUMULATIVE_SUM 
   FROM STUDENT 
   WHERE CLASS = 'Data Science';

7. "List students who scored above the 75th percentile in their section."
   The SQL command will be:
   SELECT NAME, SECTION, MARKS 
   FROM (
       SELECT NAME, SECTION, MARKS, 
              PERCENT_RANK() OVER (PARTITION BY SECTION ORDER BY MARKS DESC) AS PERCENTILE_RANK 
       FROM STUDENT
   ) WHERE PERCENTILE_RANK > 0.75;

    also the sql code should not have ``` in beginning or end and sql word in output
    """

]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("SQL Data Retriever")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("Output")
    for row in response:
        print(row)
        st.header(row)
