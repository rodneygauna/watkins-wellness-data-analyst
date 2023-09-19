"""Generates a warehouse database from the raw data.
This script will generate a warehouse database from the three sales databases.
The database will be named:
    - warehouse.db
"""

# Imports
import sqlite3


# Connect to the databases
conn_sales_10 = sqlite3.connect('sales-10.db')
cursor_sales_10 = conn_sales_10.cursor()

conn_sales_100 = sqlite3.connect('sales-100.db')
cursor_sales_100 = conn_sales_100.cursor()

conn_sales_1000 = sqlite3.connect('sales-1000.db')
cursor_sales_1000 = conn_sales_1000.cursor()


# Create a warehouse database
conn_warehouse = sqlite3.connect('warehouse.db')
cursor_warehouse = conn_warehouse.cursor()


# Create the table
cursor_warehouse.execute("""CREATE TABLE IF NOT EXISTS warehouse (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            customer VARCHAR(50),
                            product VARCHAR(50),
                            date DATE,
                            quantity INTEGER,
                            amount FLOAT
                            )""")


# Extract data from the sales databases
cursor_sales_10.execute("""SELECT * FROM sales""")
cursor_sales_100.execute("""SELECT * FROM sales""")
cursor_sales_1000.execute("""SELECT * FROM sales""")
data_sales_10 = cursor_sales_10.fetchall()
data_sales_100 = cursor_sales_100.fetchall()
data_sales_1000 = cursor_sales_1000.fetchall()


# Transform data
def transform_data(data):
    """Transform the data for the warehouse database"""

    # Create a list to hold the transformed data
    transformed_data = []

    # Create a loop to iterate through the data
    for record in data:
        transformed_data.append(
            (record[1], record[2], record[3], record[4], record[5]))

    # Return the transformed data
    return transformed_data


# Load data into the warehouse database
cursor_warehouse.executemany("""INSERT INTO warehouse (
                                customer,
                                product,
                                date,
                                quantity,
                                amount
                                )
                                VALUES (?, ?, ?, ?, ?)""",
                             transform_data(data_sales_10))
cursor_warehouse.executemany("""INSERT INTO warehouse (
                                customer,
                                product,
                                date,
                                quantity,
                                amount
                                )
                                VALUES (?, ?, ?, ?, ?)""",
                             transform_data(data_sales_100))
cursor_warehouse.executemany("""INSERT INTO warehouse (
                                customer,
                                product,
                                date,
                                quantity,
                                amount
                                )
                                VALUES (?, ?, ?, ?, ?)""",
                             transform_data(data_sales_1000))


# Commit changes
conn_warehouse.commit()


# Close connections
conn_sales_10.close()
conn_sales_100.close()
conn_sales_1000.close()
conn_warehouse.close()

# Print message
print("Warehouse database generated successfully!")
