import sqlite3
from sqlite3 import Error
from database.db_connections import sql_connection

class User ():
    def __init__(self, email, password, name, last_name, is_logged_in):
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name
        self.is_logged_in = is_logged_in

    def create_user(self):
        try:
            connecction = sql_connection()
            cursor_obj = connecction.cursor()
            cursor_obj.execute("INSERT INTO users VALUES({}, {}, {}, {}, {})".format(
                self.email, 
                self.password, 
                self.name,
                self.last_name,
                self.is_logged_in))
            connecction.close()
            return 0, "User registered!"
        except Error:
            return 1, Error

    def get_user (self, email, password):
        try:
            connecction = sql_connection()
            cursor_obj = connecction.cursor()
            cursor_obj.execute("SELECT * FROM users WHERE email = {} and password = {}".format(email, password))
            results = cursor_obj.fetchall()
            for row in results:
                user = User(row.mail, row.password, row.name, row.last_name, row.is_logged_in)
            return 0, user
        except Error:
            return 1, Error


