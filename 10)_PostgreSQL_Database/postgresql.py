# Here we use postgreSQL which is not inbuilt

import psycopg2

# Create
def create_table():
    conn = psycopg2.connect("dbname='tkinter' user='postgres' password='postgres123' host='localhost' port='5432'") # connection
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    conn.commit() # we use commit only when we make changes to the db
    conn.close()

# Insert
def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='tkinter' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

# Read
def view():
    conn = psycopg2.connect("dbname='tkinter' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

# Delete
def delete(item):
    conn = psycopg2.connect("dbname='tkinter' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE * FROM store WHERE item=%s",(item))
    conn.commit()
    conn.close()
    return rows

# Update
def update(quantity,price,item):
    conn = psycopg2.connect("dbname='tkinter' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()
    return rows



create_table()

insert('Green Tea', 250, 90)
insert('Coffee', 200, 100)

print(view())

# delete('Coffee')

# update(250, 90, 'Green Tea')