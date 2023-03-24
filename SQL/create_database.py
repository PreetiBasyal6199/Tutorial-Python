import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection=sqlite3.connect(path)            # Connection to database
        print("Connection to database success")
        cu =connection.cursor()
        #---------------Creating a table----------------------------
        cu.execute("""                              
        CREATE TABLE IF NOT EXISTS position(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        name TEXT NOT NULL
        ) 
        """)
        cu.execute("""
        CREATE TABLE  IF NOT EXISTS EMPLOYEE(
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        address TEXT NOT NULL,
        position_id INTEGER NOT NULL,
        FOREIGN KEY (position_id) REFERENCES position (id) 
        )
        """)

    except Error as e:
        print(e)
    return connection

create_connection("Test_db.sqlite")