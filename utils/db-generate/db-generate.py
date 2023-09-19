"""Generate Sales Databases
This script will generate three sales databases.
Each database will have a different number of records.
The databases will be named:
    - sales-10.db
    - sales-100.db
    - sales-1000.db
"""

# Imports
import sqlite3
import random
from faker import Faker


# Database - Create Databases
def create_db(db_name):
    """Create the three sales databases"""

    # Create a connection object
    conn = sqlite3.connect(db_name)

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table
    cursor.execute("""CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer VARCHAR(50),
                    product VARCHAR(50),
                    date DATE,
                    quantity INTEGER,
                    amount FLOAT
                    )""")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Database - Insert Data
def insert_data(db_name, num_records):
    """Insert data into the sales database"""

    # Create a connection object
    conn = sqlite3.connect(db_name)

    # Create a cursor object
    cursor = conn.cursor()

    # Create a Faker object
    fake = Faker()

    # Create a list to hold the data
    data = []

    # Create a loop to generate data
    for i in range(num_records):
        data.append((fake.company(), fake.word(), fake.date(),
                    random.randint(1, 100), random.randint(100, 5000)))

    # Insert data into table
    cursor.executemany(
        """
        INSERT INTO sales (customer, product, date, quantity, amount)
        VALUES (?, ?, ?, ?, ?)
        """, data)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Genearte the databases
def generate_db():
    """Main program function"""

    # Create the databases
    create_db("sales-10.db")
    create_db("sales-100.db")
    create_db("sales-1000.db")

    # Insert data into the databases
    insert_data("sales-10.db", 10)
    insert_data("sales-100.db", 100)
    insert_data("sales-1000.db", 1000)


# Call the main function
generate_db()
