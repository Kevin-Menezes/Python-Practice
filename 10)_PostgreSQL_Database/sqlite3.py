# Here we use sqlite3 which is an inbuilt database

import sqlite3

# Create
def create_table():
    conn = sqlite3.connect("lite.db") # connection
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    conn.commit() # we use commit only when we make changes to the db
    conn.close()

# Insert
def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

# Read
def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

# Delete
def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE * FROM store WHERE item=?",(item))
    conn.commit()
    conn.close()
    return rows

# Update
def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()
    return rows



create_table()

insert('Green Tea', 250, 90)
insert('Coffee', 200, 100)

print(view())

delete('Coffee')

update(250, 90, 'Green Tea')