from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/flask' #key-value pair for setting up db
db = SQLAlchemy(app)

class Data(db.Model):
    
    # This is to automatically generate a table with columns in the database...like @Entity
    __tablename__ = "height_collector"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self,email,height): # Constructor
        self.email = email
        self.height = height


@app.route("/") # This is like Spring @RequestMapping
def index():
    return render_template("index.html")


@app.route("/success",methods=['POST']) # This is like Spring @RequestMapping
def success():
    if request.method == 'POST':
        useremail = request.form["useremail"] # "email" is the name attribute in the form
        userheight = request.form["userheight"] # "height" is the name attribute in the form
        
        if db.session.query(Data).filter(Data.email==useremail).count() == 0: # Before inserting we check if the email is already there or not

            data = Data(useremail,userheight)
            db.session.add(data) # Insert
            db.session.commit()
            return render_template("success.html")
    return render_template("index.html",text="Email already exists!")

if __name__=="__main__":
    app.run(debug=True)