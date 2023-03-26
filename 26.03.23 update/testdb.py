from app import *

with app.app_context():
    db.create_all() # create all tables
    # db.drop_all() # delete all tables

user = User(name = "Romam", username = "Roman99999", password = "43553535") # add user
db.session.add(user)    # add user to the data base
db.session.commit() # confirm changes - without this row nothing will be changed