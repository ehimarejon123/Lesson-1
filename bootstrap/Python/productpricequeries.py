import sqlite3
connection = sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXSITS PRODUCT (
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT,
    PRO_PRICE INTEGER
    PRO_COM TEXT
)
""")
products = [
    ("101", "MOTHER BOARD", 3200, "15"),
    ("102", "KEY BOARD", 450, "16"),
    ("103", "ZIP DRIVE", 250, "14"),
    ("104", "SPEAKER", 550, "16"),
    ("105", "MONITOR", 5000, "11"),
    ("106", "DVD DRIVE", 900, "12"),
    ("107", "CD DRIVE", 800, "12"),
    ("108", "PRINTER", 2600, "13"),
    ("109", "REFILL CARTRIDGE", 350, "13"),
    ("110", "MOUSE", 250, "12")
]
cursor.executemany("""
INSERT OR IGNORE INTO PRODUCT
(PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM)
VALUES (?, ?, ?, ?)
""", products)
print("ALL PRODUCTS")

print("-" * 40)

cursor.execute("SELECT * FROM PRODUCT")

products = cursor.fetchall()

for product in products:

print(product)

print("\nPRODUCT WITH MINIMUM PRICE")

print("-" * 40)

cursor.execute("""

SELECT PRO_NAME, PRO_PRICE

FROM PRODUCT

WHERE PRO_PRICE = (

SELECT MIN(PRO_PRICE)

FROM PRODUCT

)

""")

result = cursor.fetchall()

for product in result:

print("Product:", product[0])

print("Price:", product[1])

print("\nPRODUCT WITH MAXIMUM PRICE")

print("-" * 40)

cursor.execute("""

SELECT PRO_NAME, PRO_PRICE

FROM PRODUCT

WHERE PRO_PRICE = (

SELECT MAX(PRO_PRICE)

FROM PRODUCT

)

""")

result = cursor.fetchall()

for product in result:

print("Product:", product[0])

print("Price:", product[1])

connection.commit()

connection.close()