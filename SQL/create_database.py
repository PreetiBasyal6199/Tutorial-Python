import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection=sqlite3.connect(path)            # Connection to database
        print("Connection to database success")
    except Error as e:
        print(e)
    return connection

create_connection("Test_db.sqlite")