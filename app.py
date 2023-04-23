from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager

login_manager = LoginManager()  # об'єкт що буде відповідати за login, object that is responsible for login


db = SQLAlchemy()   # create data base

app = Flask(__name__)   # create web-app Flask

app.config["SECRET_KEY"] = "5a315f3fc289c0070fa3923e8376be8970a62b83    "
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coffee_house.db"  # set data base url ( connect sqlalchemy to data base ( coffee_house.db ))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # app.config() - config parameter
db.init_app(app)    # initialize the the app with the extension (start the app)

login_manager.init_app(app)
login_manager.login_view = "signin" # if you enter website first time, you won'be be able to enter the main page, and you will be on login page
login_manager.login_message = "To order stuff log in"   # message on log in page, you will see it only one time
login_manager.login_message_category = "alert-warning"  # set log in message (login_manager.login_message)


from routes import *    # import all, from routes import routes - import only object routes

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

# python3.9 -m venv venv_name - create venv mac
# source .venv/bin/activate - activate venv

# pip install Flask-SQLAlchemy - install Flask-SQLAlchemy (ORM SQL)