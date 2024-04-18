#!/usr/bin/python3

"""
function that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(sql_query, (state_name,))

    rws = cursor.fetchall()

    for r in rws:
        print(r)

    cursor.close()
    db.close()
