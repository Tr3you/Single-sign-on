import sqlite3
from sqlite3 import Error
import json
from flask import g


class User ():
    def __init__(self, email, password, name, last_name, is_logged_in):
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name
        self.is_logged_in = is_logged_in

    def create_user(self):
        try:
            with open('database.json') as file:
                c = file.read().encode()
                data = json.loads(c)
            data[self.email] = {'password': self.password,'name': self.name, 'last_name':self.last_name, 'is_logged_in':self.is_logged_in}
            f = open('database.json', 'w')
            c = f.write(json.dumps(data, indent=4))
            f.close()
            return [0, 'User was created']
        except Error:
            return [1, Error]

    def get_user (self, email, password):
        with open('database.json') as file:
            c = file.read().encode()
            data = json.loads(c)
        if(data[email] and data[email]['password'] == password):
            return [0, 'User is logged in now'] 
        else:
            return [1, 'Login had failed']



