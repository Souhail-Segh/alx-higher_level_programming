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
    input = sys.argv[4]

    cur.execute("""
    SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC
    """, (input,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
