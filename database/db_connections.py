import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('database/database.db')
        return con
    except Error:
        print(Error)
