import os
from flask import Flask
from .views import views # importing the views.py
import pymssql
from pymssql import Error
import getpass

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
    try:
        username = input("Enter your username\n")
        password = getpass.getpass("Enter password\n")
    except Exception as error:
        print("Wrong input")
    conn = pymssql.connect('uranium.cs.umanitoba.ca',username, password, 'cs3380')
    conn.autocommit(True)
    cursor = conn.cursor()
    
    '''
        1) IF EXISTS, DROP ALL TABLES
        2) CREATE THE TABLES
        3) INSERT INTO TABLES
    '''
    # cursor.execute('CREATE table myTable(mynum int not Null, primary key (mynum))')
    # cursor.execute('INSERT INTO myTable VALUES (1)')
    # cursor.execute('INSERT INTO myTable VALUES (2)')
    # cursor.execute('INSERT INTO myTable VALUES (3)')
    # cursor.execute('INSERT INTO myTable VALUES (4)')
    # cursor.execute('SELECT * from myTable')
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    
    try:
        conn = ""
    except Error as e:
        print(e)

    return None

conn = create_connection("hello.txt")

# import sql file
# read sql file and store it in a variable
#cur = conn.cursor()
#cur.execute(sqlfile)