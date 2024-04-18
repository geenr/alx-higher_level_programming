#!/usr/bin/python3
"""Function that lists all states from the  database"""
import sys
import MySQLdb

def list_states (username, password, database):
    """lists all states from the database hbtn_0e_0_usa.
    Ags:
        username: mysql username
        password: mysql password
        database: mysql database
    """

    db = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
    cursor = db.cursor()

    
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    
    rws = cursor.fetchall()


    for r in rws:
        print(r)

    
    db.close()


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
