import sqlite3
connection = sqlite3.connect("book_club.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL,
    pages INTEGER NOT NULL,
    pub_year INTEGER NOT FULL
)
""")
cursor.execute("DELETE FROM book")
books = [
    (1, 'Dragon Quest', 'Fantasy', 9.2, 312, 2021),
    (2, 'Code Wizards', 'Sci-Fi', 8.5, 280, 2020),
    (3, 'Ocean Deep', 'Adventure', 7.8, 195, 2022),
    (4, 'Star Rangers', 'Sci-Fi', 9.5, 340, 2019),
    (5, 'Forest Secrets', 'Fantasy', 8.1, 228, 2023),
    (6, 'Robot City', 'Sci-Fi', 7.2, 260, 2023),
    (7, 'Time Jumpers', 'Adventure', 8.9, 398, 2022),
    (8, 'Magic Academy', 'Fantasy', 9.0, 398, 2020),
]
cursor.executemany("""
INSERT INTO book VALUES (?, ?, ?, ?, ?, ?)
""", books)
connection.commit()
print("\nALL BOOKS")
cursor.execute("SELECT * FROM book")
for row in cursor.fetchall():
    print(row)
print("\nRATING: LOWEST TO HIGHEST")
cursor.execute("SELECT title, rating FROM book ORDER BY rating ASC")
for row in cursor.fetchall():
    print(row)
print("\nRATING: HIGHEST TO LOWEST")
cursor.execute("SELECT title, rating FROM book ORDER BY rating DESC")
for row in cursor.fetchall():
    print(row)
print("\nGENRE A-Z, RATING HIGH-LOW")
cursor.execute("""
SELECT title, genre, rating
FROM book
ORDER BY genre ASC, rating DESC
""")
for  row in cursor.fetchall():
    print(row)
print("\nTOP 3")
cursor.execute("""
SELECT title, rating
FROM book
ORDER BY rating DESC
LIMIT 3
""")
for  row in cursor.fetchall():
    print(row)
print("\n5 OLDEST BOOKS")
cursor.execute("""
SELECT title, pub_year
FROM book
ORDER BY pub_year ASC
LIMIT 5
""")
for  row in cursor.fetchall():
    print(row)
print("\nBOOKS PER GENRE")
cursor.execute("""
SELECT genre, COUNT(*)
FROM book
GROUP BY genre
""")
for  row in cursor.fetchall():
    print(row)
print("\nPAGES AND AVERAGE RATING")
cursor.execute("""
SELECT genre, SUM(pages, AVG(rating)
FROM book
GROUP BY genre
""")
for row in cursor.fetchall():

print(row)

print("\nGENRES WITH MORE THAN 2 BOOKS")

cursor.execute("""

SELECT genre, COUNT(*)

FROM book

GROUP BY genre

HAVING COUNT(*) > 2

""")

for row in cursor.fetchall():

print(row)

print("\nGENRES WITH AVERAGE RATING >= 8.5")

cursor.execute("""

SELECT genre, AVG(rating)

FROM book

GROUP BY genre

HAVING AVG(rating) >= 8.5

""")

for row in cursor.fetchall():

print(row)

connection.close()