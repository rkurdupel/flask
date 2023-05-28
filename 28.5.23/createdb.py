from app import *

with app.app_context():
    db.drop_all()   # delete database
    db.create_all() # create database

    #user = User(name = "Roman", username = "r12345", password = "123456")
    #db.session.add(user)
    #db.session.commit()