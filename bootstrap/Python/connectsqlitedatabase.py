import sqlite3
connection = sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
student_id INTEGER PRIMARY KEY,
name TEXT NOT FULL,
age INTEGER,
marks REAL
)
"""
)
cursor.execute(
    "INSERT INTO Students (student_id, name, age, marks) VALUES (?, ?, ?, ?)",
    (101, "EJ", 15, 98)
)
connection.commit()
cursor.execute("SELECT * FROM Students")
students = cursor.fetchall()
for i in students:
    print(i)
connection.close()