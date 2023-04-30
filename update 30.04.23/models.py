from app import db, login_manager  # connect database, login manager from app.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(db.Model,  UserMixin):   # create db # filter by priority 1)db.Model 2) UserMixin, if there are same functions first function will be taken from db.Model then from UserMixin
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

    def set_password_hash(self, original_password):
        self.password = generate_password_hash(original_password)   # generate encrypted password from original_password
    def check_password(self, original_password):   
        return check_password_hash(self.password, original_password)    # check if passwords match, both passwords are encrypted
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.Text)    # db.Text - text ( without limits )
    link = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))   # db.ForeignKey("user.id")  - get from data base user id, and connect to the row user_id (in Project class)

    def __repr__(self):
        return f"User: {self.username}"    
