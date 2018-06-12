import sqlite3

with sqlite3.connect('genealogy.db') as conn:
    try:
        with open('genealogy-schema.sql') as f:
            conn.executescript(f.read())
        with open('genealogy-data.sql') as f:
            conn.executescript(f.read())
    except sqlite3.OperationalError as e:
        print(e)

    cursor = conn.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute('select * from family')

    for row in cursor:
        for key in row.keys():
            print(key, row[key], sep=':', end=' ')
        print()
