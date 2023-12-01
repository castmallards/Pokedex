import os
from flask import Flask
from .views import views # importing the views.py
import sqlite3
from sqlite3 import Error

# create flask app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')

    return app


def create_connection(db_filename):
    ''' This creates a connection to the database using sqlite3
        :param db_filename: Database file name
        :return: Returns the conenection to database or None
    '''    
    conn = None

    try:
        conn = ""
    except Error as e:
        print(e)

    return None

conn = create_connection("hello.txt")