## Student Database Chatbot

This chatbot is built using two different language models:

1. OpenAI's GPT-3.5 Turbo Instruct
2. Google's GenerativeAI Gemini-Pro

Both models are utilized for processing user queries and retrieving information from the database. However, Google GenerativeAI Gemini-Pro outperforms GPT-3.5 Turbo Instruct due to its more up-to-date capabilities.

### Problem Statement

The task is to create a chatbot that can provide analytical responses based on a database table of students' exam marks. The fields in the database include:
- Student roll number
- Name
- Department
- Subject
- Mark

There are only two departments: AI and Data Science. The chatbot should respond differently depending on the querying faculty's department:
- AI faculty should only receive information about AI students.
- Data Science faculty should only receive information about Data Science students.
- Each faculty should not have access to data from the other department.

### Example Queries

Here are some example queries that the chatbot should be able to handle:
1. How many students scored above 75%?
2. How many are weak in subject X?
3. Which two subjects have similarity in marks, i.e., if a student does well in one subject, they are also likely to do well in the other subject?

### Requirements

The following technologies and libraries are required to run the chatbot:
- Streamlit
- OpenAI API
- Google GenerativeAI
- Python-dotenv
- SQLite3
- Python

### Technologies Used

The chatbot is built using the following technologies:
- Python
- Streamlit
- SQLite
- OpenAI API
- dotenv

---

Feel free to reach out for any questions or concerns regarding the setup or functionality of the chatbot.


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

  
