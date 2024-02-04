import sqlite3

# connect to database
conn = sqlite3.Connection('customer.db')

# creating a cursor
cursor = conn.cursor()

# creating a table into the database
query = """
    CREATE TABLE IF NOT EXISTS customers(
        first_name text,
        last_name text,
        email text
    )
"""
# DataTypes in sql [NULL, INTEGER, REAL, TEXT, BLOB]
cursor.execute(query)

# # inserting data into customers table
# cursor.execute("""INSERT INTO customers VALUES('nehal', 'ahamad', 'nehalahamad@gmail.com');""")
# cursor.execute("""INSERT INTO customers VALUES('jamal', 'ahamad', 'jamalahamad@gmail.com');""")
# cursor.execute("""INSERT INTO customers VALUES('belal', 'ahamad', 'belalahamad@gmail.com');""")

# fetching the data from the database table
cursor.execute("SELECT * FROM customers")

data = cursor.fetchone() # it will fetch only one row
# data = cursor.fetchmany() # it will fetch only two rows
# data = cursor.fetchall()
print(data)

conn.commit()
conn.close()





