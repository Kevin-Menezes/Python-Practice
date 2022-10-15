import sqlite3

class Database:

    # Constructor....this is like a default contructor that needs 1 default parameter "self".....self is like a default parameter for every function
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    # Insert
    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    # Display
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    # Search
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    # Delete
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    # Update
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    # Destructor.....this is called just before the program ends
    def __del__(self):
        self.conn.close()

    # create()
    # insert("Socerer Stone", "HP", 1980, 93285737)
    # insert("Water life", "Jayden", 2000, 93469020)
    # print(view())