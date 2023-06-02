# I HATE THIS DB, WHY NOT MYSQL OR MARIADB?


# Import the necessary libraries
import psycopg2, csv, os, time, sys

# Establish connection to the PostgreSQL database
conn = psycopg2.connect(database="PhoneBook", user="postgres", password="qwe", host="localhost", port="5432")
cur = conn.cursor()

# Create tables for PhoneBook
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                phone TEXT NOT NULL)''')

# Insert data into the PhoneBook table from a csv file
def insert_from_csv(filename):
    with open("tsis10/"+filename, 'r') as file:
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

# Create a function that returns all records based on a pattern
def get_users_by_pattern(pattern):
    cur.execute("SELECT * FROM users WHERE firstname LIKE %s OR lastname LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Create a procedure to insert new user by name and phone, update phone if user already exists
def insert_or_update_user(firstname, lastname, phone):
    cur.execute("SELECT COUNT(*) FROM users WHERE firstname = %s AND lastname = %s", (firstname, lastname))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO users (firstname, lastname, phone) VALUES (%s, %s, %s)", (firstname, lastname, phone))
    else:
        cur.execute("UPDATE users SET phone = %s WHERE firstname = %s AND lastname = %s", (phone, firstname, lastname))
    conn.commit()

# Create a procedure to insert many new users by list of name and phone
def insert_many_users(users):
    incorrect_data = []
    for user in users:
        name, lastname, phone = user.split(',')
        lastname = lastname.strip()
        phone = phone.strip()
        if len(phone) != 10 or not phone.isdigit():
            incorrect_data.append(user)
            continue
        cur.execute("INSERT INTO users (firstname, lastname, phone) VALUES (%s, %s)", (name, lastname, phone))
    conn.commit()
    return incorrect_data

# Create a function to querying data from the tables with pagination (by limit and offset)
def query_data_with_pagination(filter, value, limit, offset):
    cur.execute("SELECT * FROM users WHERE {} = %s LIMIT %s OFFSET %s".format(filter), (value, limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Create a procedure to deleting data from tables by username or phone
def delete_user_by_filter(filter, value):
    cur.execute("DELETE FROM users WHERE {} = %s".format(filter), (value,))
    conn.commit()

def get_user_list():
    user_list = []
    while True:
        user_data = input("Enter user data in the format 'firstname, lastname, phone' (or enter 'done' when finished): ")
        if user_data.lower() == "done":
            break
        else:
            firstname, lastname, phone = user_data.split(",")
            user_list.append({"firstname": firstname.strip(), "lastname": lastname.strip(), "phone": phone.strip()})
    return user_list

# For console cleaning
clear = lambda: os.system("cls")

# Empty string
val = ""

while True:
    clear()
    print(val)
    option = input(
    """
    Choose what option you want to use:

    [1] - Insert from CSV
    [2] - Insert from Console
    [3] - Update data
    [4] - Query data
    [5] - Delete data
    [6] - Search by pattern
    [7] - Insert or update user
    [8] - Insert many new users
    [9] - Query data with pagination (by limit and offset)
    [10] - Delete data, but as number 10

    OR

    [0] - To leave

    """)

    match (int(option)):
        case 1:
            clear()
            fn = input("Input file name: ")
            insert_from_csv(fn)
            val = "Your .csv file's values were imported to database."
        case 2:
            clear()
            insert_from_console()
            val = "Your values were imported to database."
        case 3:
            clear()
            fn = input("Enter firstname: ")
            ln = input("Enter lastname: ")
            npn = input("Enter new phone number: ")
            update_data(fn, ln, npn)
            val = "Old data from database were updated with new one."
        case 4:
            clear()
            time_to_wait = input("Type time (in seconds) to wait for your data to load: ")
            filter = input("Enter by what filter data should be searched (firstname, lastname or phone): ")
            value = input("Enter filter's value: ")
            query_data(filter=filter, value=value)
            time.sleep(int(time_to_wait))
        case 5:
            clear()
            filter = input("Enter by what filter data should be searched to be deleted (firstname, lastname or phone): ")
            value = input("Enter filter's value: ")
            delete_data(filter=filter, value=value)
            val = "Deleted data from database."
        case 6:
            clear()
            value = input("Enter pattern's value: ")
            get_users_by_pattern(value)
            val = "Showing all data found by pattern " + value
        case 7:
            clear()
            value = input("Enter pattern's value: ")
            get_users_by_pattern(value)
            val = "Old phone number from database was updated with new one."
        case 8:
            clear()
            users = get_user_list()
            insert_many_users(users)
            val = "Added many users to database"
        case 9:
            clear()
            filter = input("Enter by what filter data should be searched (firstname, lastname or phone): ")
            value = input("Enter filter's value: ")
            l = input("Enter limit: ")
            o = input("Enter offset: ")
            query_data_with_pagination(filter=filter, value=value, limit=l, offset=o)
            val = ""
        case 10:
            clear()
            filter = input("Enter by what filter data should be searched (firstname, lastname or phone): ")
            value = input("Enter filter's value: ")
            delete_user_by_filter(filter=filter, value=value)
            val = ""
        case 0:
            clear()
            clear()
            print("Thank you and bye :)")
            time.sleep(3)
            # Close the database connection
            cur.close()
            conn.close()
            sys.exit()
        case _:
            val = ("""
            Choose number from 1 to 10
            """)