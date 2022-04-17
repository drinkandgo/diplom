import sqlite3 as sq

with sq.connect("storage.db") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE """)