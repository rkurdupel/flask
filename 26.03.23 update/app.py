from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # create data base

app = Flask(__name__)   # create web-app Flask

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coffee_house.db"  # set data base url ( connect sqlalchemy to data base ( coffee_house.db ))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # app.config() - config parameter
db.init_app(app)    # initialize the the app with the extension (start the app)

class User(db.Model):   # create db
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)    # nullable = False - value can not be empty (0)
    # db.String(50) - amount of letters db.String(size)
    password = db.Column(db.String, nullable = False)
    name = db.Column(db.String(200))
    country = db.Column(db.String(50), default = 'USA')  # default = 'USA' - default value is USA

    project = db.relationship("Project", backref = "author")    # задавти відношення з Project, set relation with data base Project, backref = "author" - Project is an author to User database


    def __repr__(self): # як виглядає об'єкт при друці
        return f"User: {self.name}" # відобразити користувача (name)
    # self.username - name of the user


class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    descriptiom = db.Column(db.Text)    # db.Text - text ( without limits )
    link = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))   # db.ForeignKey("user.id")  - get from data base user id, and connect to the row user_id (in Project class)

    def __repr__(self):
        return f"User: {self.username}"    


# main page /
@app.route("/") # за таким маршрутом http://127.0.0.1:5000/ 
def index():
    #return "<h1>Hello World!</h1>"   # результат, що повертається у браузер
    #return "text"  # works - output: text
    users = User.query.all()    # отримати всі об'єкти user
    print(users)    # [User: Roman99999, User: Johnpro2344, User: sawdw232, User: ddedf242]
    return render_template("index.html", users = users)    # load html page index.html
    # user = users - transfer data 

@app.route("/about")    # @app.route("/about") - http://127.0.0.1:5000/about
def about():
    return "<b>About page</b>"


# ALL TEMPLATES SHOULD BE IN THE templates folder, otherwise flask will not be able to find them
@app.route("/html_template")
def main_page():
    return render_template("index.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")
@app.route("/my_contact")
def contract_details():
    return render_template("my_contact.html")

# app.route - decorator
@app.route("/signup", methods = ["POST", "GET"])    # methods - methods, post - send data, get - get data
def signup():
    return render_template("signup.html")

@app.route("/signin", methods = ["POST", "GET"])
def signin():
    return render_template("login.html")


# якщо машрут route без "/" - буде помилка, if route without "/" error will occur:
#  ValueError: urls must start with a leading slash


if __name__== "__main__":   # при запуску app.py, після цієї умови більше нічого окрім функцій в класах не буде виконуватись
    app.config["TEMPLATES_AUTO_RELOAD"] = True  # що б сайт постійно перезгружвася ( що б відображались нові зміни )
    app.run(debug = True, port = 5001)   # launch local web-server from this file
    # debug = True - запустити в режимі debug

# ЩОБ ПОКАЗУВАЛОСЬ ФОТО З .html файлу потрібно створити папку static/images і туди закинути файл, 
# і в .html файлі вказати шлях  path static/images/image_name.png


# INSTALL Flask
# python -m pip install flask 

# SAVE Requirements
# python -m pip freeze > requirements.txt

# LOAD (install) requirements
# python -m pip install -r requirements.txt


# python -m venv venv - create venv
# venv\Scripts\activate - activate venv   ( need cmd, with bash does not work )

# pip install Flask-SQLAlchemy - install Flask-SQLAlchemy (ORM SQL)