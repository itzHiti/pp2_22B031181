# Import the necessary libraries
import psycopg2
import csv

# Establish connection to the PostgreSQL database
conn = psycopg2.connect(database="PhoneBook", user="username", password="password", host="localhost", port="5432")
cur = conn.cursor()

# Create tables for PhoneBook
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                phone TEXT NOT NULL)''')

# Insert data into the PhoneBook table from a csv file
def insert_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        for row in reader:
            cur.execute("INSERT INTO users (firstname, lastname, phone) VALUES (%s, %s, %s)", row)
    conn.commit()
    
# Insert data into the PhoneBook table from console input
def insert_from_console():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO users (firstname, lastname, phone) VALUES (%s, %s, %s)", (firstname, lastname, phone))
    conn.commit()

# Update data in the PhoneBook table
def update_data(firstname, lastname, new_phone):
    cur.execute("UPDATE users SET phone = %s WHERE firstname = %s AND lastname = %s", (new_phone, firstname, lastname))
    conn.commit()

# Query data from the PhoneBook table
def query_data(filter, value):
    cur.execute("SELECT * FROM users WHERE {} = %s".format(filter), (value,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Delete data from the PhoneBook table by username or phone
def delete_data(filter, value):
    cur.execute("DELETE FROM users WHERE {} = %s".format(filter), (value,))
    conn.commit()

# Close the database connection
cur.close()
conn.close()
