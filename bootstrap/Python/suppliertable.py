import sqlite3
connection = sqlite3.connect("supplier.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLEVIF NOT EXSITS supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
)
""")
cursor.execute("""
INSERT INTO supplier (SN0, SNAME, STATUS, CITY) VALUES
('S1', 'Smith', 20, 'London',)
('S2', 'Jones', 10, 'Paris',)
('S3', 'Blake', 30, 'Paris',)
('S4', 'Clarke', 20, 'Athlens',)
('S5', 'Smith', 30, 'London',)
""")

('S5', 'Adams', 30, 'Athens')

""")

connection.commit()

cursor.execute("SELECT * FROM supplier")

rows = cursor.fetchall()

for row in rows:

print(row)

connection.close()