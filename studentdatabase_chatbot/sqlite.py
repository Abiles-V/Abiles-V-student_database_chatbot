import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE STUDENT (
    ROLL_NUMBER INT PRIMARY KEY,
    NAME VARCHAR(100),
    DEPARTMENT VARCHAR(20),
    SUBJECT1 VARCHAR(100),
    MARKS1 INT,
    SUBJECT2 VARCHAR(100),
    MARKS2 INT,
    SUBJECT3 VARCHAR(100),
    MARKS3 INT
);
"""
cursor.execute(table_info)

# Insert records for Data Science students
data_science_students = [
    (1, 'Krish', 'Data Science', 'Mathematics', 90, 'Physics', 85, 'Chemistry', 88),
    (2, 'Sudhanshu', 'Data Science', 'Biology', 95, 'Computer Science', 92, 'Statistics', 87),
    (3, 'Daksina', 'Data Science', 'Economics', 78, 'English', 80, 'Geography', 82),
    (4, 'John', 'Data Science', 'History', 75, 'Art', 85, 'Music', 80),
    (5, 'priya', 'Data Science', 'Physics', 90, 'Chemistry', 88, 'Biology', 85),
    (6, 'Abrna', 'Data Science', 'Computer Science', 95, 'Statistics', 90, 'Mathematics', 85),
    (7, 'David', 'Data Science', 'English', 82, 'Geography', 80, 'History', 78),
    (8, 'Esther', 'Data Science', 'Chemistry', 88, 'Biology', 85, 'Physics', 80),
    (9, 'Ryan', 'Data Science', 'Mathematics', 92, 'Computer Science', 90, 'Statistics', 85),
    (10, 'Sophia', 'Data Science', 'Geography', 80, 'History', 78, 'Art', 85)
]

for student in data_science_students:
    cursor.execute('INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', student)

# Insert records for AI students
ai_students = [
    (11, 'Vikash', 'AI', 'Mathematics', 75, 'Physics', 70, 'Computer Science', 80),
    (12, 'Dipesh', 'AI', 'Chemistry', 65, 'Biology', 60, 'Statistics', 75),
    (13, 'Rahul', 'AI', 'English', 78, 'Geography', 80, 'History', 75),
    (14, 'Amit', 'AI', 'Physics', 70, 'Chemistry', 65, 'Biology', 60),
    (15, 'Anjali', 'AI', 'Computer Science', 85, 'Statistics', 80, 'Mathematics', 75),
    (16, 'Rohan', 'AI', 'Geography', 80, 'History', 75, 'Art', 78),
    (17, 'Priya', 'AI', 'Biology', 60, 'Physics', 70, 'Chemistry', 65),
    (18, 'Aryan', 'AI', 'Statistics', 75, 'Mathematics', 70, 'Computer Science', 80),
    (19, 'Kiran', 'AI', 'History', 75, 'Art', 78, 'Music', 80),
    (20, 'Meera', 'AI', 'Physics', 70, 'Chemistry', 65, 'Biology', 60)
]

for student in ai_students:
    cursor.execute('INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', student)

# Display all the records
print("The inserted records are:")
data = cursor.execute('SELECT * FROM STUDENT')
for row in data:
    print(row)

# Commit changes to the database
connection.commit()
connection.close()
