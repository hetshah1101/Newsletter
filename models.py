import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def add_user(name, email):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into users (email, name) values(?, ?)', (email, name))
    con.commit()
    con.close()
