from app import *

with app.app_context():
    db.create_all() # create all tables
    # db.drop_all() # delete all tables

    user = User(name = "Roman", username = "Roman99999", password = "43553535") # add user
    user2 = User(name = "John", username = "Johnpro2344", password = "daedwk122")
    user3 = User(name = "Karin", username = "sawdw232", password = "ddefdfe")
    user4 = User(name = "Dicky", username = "ddedf242", password  ="prosuper3434")

    db.session.add(user)    # add user to the data base     TypeError: add() takes from 2 to 3 positional arguments but 5 were given, if more than 3 arguments or less than 2
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    
    db.session.commit() # confirm changes - without this row nothing will be changed

# SHOULD BE LAUNCHED ONLY 1 TIME, next time will be error