#!/usr/bin/python3
""" lists all states from hbtn_0e_0_usa database when name start with N"""
import MySQLdb
import sys

if __name__ == '__main__':
    ''' The follow code will not be exuceted when imported '''
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    input = str(sys.argv[4])
    cur.execute("""
    SELECT * FROM states
    WHERE name LIKE BINARY %s ORDER BY id ASC
    """, (input,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
