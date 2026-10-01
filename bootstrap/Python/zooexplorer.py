import sqlite3
connection = sqlite3.connect("zoo.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS zoo_animal (
    id INTEGER PRIMARY KEY,
    name TEXT,
    species TEXT,
    weight REAL
)
""")
animal = [
    (1, "Leo", "Lion", 3, 190.5),
    (2, "Simba", "Lion", 5, 190.5),
    (3, "Sheru", "Tiger", 3, 210.0),
    (4, "Tara", "Tiger", 6, 180.0),
    (5, "Ellie", "Elephant", 4, 500.0),
    (6, "Zara", "Zebra", 7, 250.0),
    (7, "Milo", "Monkey", 2, 12.5),
    (8, "Coco", "Monkey", 4, 15.0)
]
cursor.executemany()
cursor.executemany("""
INSERT INTO zoo_animal
VALUES (?, ?, ?, ?, ?)
""", animals)
connection.commit()
print("\nALL ANIMALS")
cursor.execute("SELECT * FROM zoo_anim")
for row in cursor.fetchall():
    print(row)
print("\nUNIQUE SPECIES")

cursor.execute("""
SELECT DISTINCT species
FROM zoo_animal
""")
for row in cursor.fetchall():
    print(row[0])
print("\nTOTAL ANIMALS")
cursor.execute("""
SELECT COUNT(*)
FROM zoo_animal
WHERE species = 'Lion'
""")
print(cursor.fetchone()[0])
print("\nTOTAL WEIGHT")
cursor.execute("""
SELECT SUM(weight)
FROM zoo_animal
""")
print(cursor.fetchone()[0])
print("\nAVERAGE WEIGHT")
cursor.execute("""
SELECT AVG(weight)
FROM zoo_animal
""")
print(round(cursor.fetchone()[0], 2))
print("\nZOO SUMMARY")
cursor.execute("""
SELECT
    COUNT(*) AS total_animals,
    SUM(weight) AS total_weight,
    AVG(weight) AS average_weight
FROM zoo_animal
""")
result = cursor.fetchone()
print("Total animals:", result[0])
print("Total weight:", result[1])
print("Average weight:", round(result[2], 2))
connection.close()