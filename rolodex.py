import sqlite3

with sqlite3.connect('rolodex.db') as conn:
    with open('rolodex-schema.sql') as f:
        conn.executescript(f.read())
    with open('rolodex-data.sql') as f:
        conn.executescript(f.read())

    cursor = conn.cursor()
    cursor.execute('select * from rolodex')

    for row in cursor:
        print(row)
