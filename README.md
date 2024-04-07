#studen_database_chatbot


#problem_satement
Given a database table of students exam marks, create a chatbot which will answer analytical queries from the table.

The fields are 
(student roll number, name, department, subject, mark)

There will be only two departments (AI, Data Science).

The chatbot will be used by two faculties (one from AI department and another from Data Science).
When AI faculty queries the chatbot, it should return information only about AI students.
When Data Science faculty queries, it should answer only about Data Science students.
AI faculty should not be able to see data from Data Science and vice versa.

Create a single model which can do this.

Example questions to chatbot will be like:

1. How many students scored above 75%?
2. How many are weak in subject X?
3. Which two subjects have similarity in marks i.e. if a student does good in one subject they are also good in the other subject?


#Requirements

 streamlit

 openai api

 google-generativeai
 
 python-dotenv
 
 sqlite3
 
 python

#Technologies 

Python

Streamlit

SQLite

OpenAI API

dotenv

#WORKFLOW
![image](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/025b2db6-d6c7-4361-943a-110660eecbbd)

#Sample outputs
![Screenshot(41)](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/60cce48f-9701-434a-a34c-4e63b338fdd2)

 ![Screenshot (35)](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/f7d5d346-8ccf-4339-b72e-ff534074dfc8)

![Screenshot (36)](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/dba3a39f-91c1-41aa-8408-2cec2725b258)

![Screenshot (37)](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/b057a58b-787a-46ab-a68b-31c7a9295459)

![Screenshot (38)](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/ca045a32-6fa1-4cc8-bd67-55160ac00c92)

![Screenshot (39)](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/65b99d21-0cee-404e-9d3d-0e0c8699f1ea)

![Screenshot (40)](https://github.com/Abiles-V/Abiles-V-student_database_chatbot/assets/137181669/011964d9-74b5-4399-8a3a-9b878fcdcf76)

  
