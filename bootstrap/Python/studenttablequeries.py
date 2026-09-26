import sqlite3
connection = sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXSITS STUDENT (
    ROLL_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
)
""")
cursor.executemany("""
INSERT OR IGNORE INTO STUDENT
(ROLL_NO, NAME, ADDRESS, PHONE, AGE)
VALUES (?, ?, ?, ?, ?)
""", [
    ('1', 'RAM', 'DELHI', '******', 18),
    ('2', 'RAMESH', 'GURGAON', '******', 18),
    ('3', 'SUJIT', 'ROHTAK', '******', 20),
    ('4', 'SURMESH', 'DELHI', '******', 18),
    ('5', 'AMAN', 'ROHTAK', '******', 20),
    ('6', 'HARSH', 'GURGAON', '******', 18)
])
cursor.execute("SELECT * FROM STUDENT")
for student in cursor.fetchall():
    print(student)
connection.commit()
connection.close()