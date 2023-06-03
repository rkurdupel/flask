from app import db, login_manager  # connect database, login manager from app.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model,  UserMixin):   # create db # filter by priority 1)db.Model 2) UserMixin, if there are same functions first function will be taken from db.Model then from UserMixin
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)    # nullable = False - value can not be empty (0)
    # db.String(50) - amount of letters db.String(size)
    password = db.Column(db.String, nullable = False) 
    name = db.Column(db.String(200))    # String - VARCHAR
    country = db.Column(db.String(50), default = 'USA')  # default = 'USA' - default value is USA

    #projects = db.relationship("Project", backref = "author")    # задавти відношення з Project, set relation with data base Project, backref = "author" - Project is an author to User database


    def __repr__(self): # як виглядає об'єкт при друці
        return f"User: {self.username}" # відобразити користувача (name)
    # self.username - name of the user

    def set_password_hash(self, original_password):
        self.password = generate_password_hash(original_password)   # generate encrypted password from original_password
    def check_password(self, original_password):   

        return check_password_hash(self.password, original_password)    # check if passwords match, both passwords are encrypted
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Item(db.Model):
    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer)
    

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    product_name = db.Column(db.String)
    product_price = db.Column(db.Integer)
    product_picture = db.Column(db.String)
    
    
    
#  ↨
# class OrderItem(db.Model):  # cart
#     id = db.Column(db.Integer, primary_key = True)
#     product_id = db.Column(db.Integer)
#     order_id = db.Column(db.Integer)
#     user_id = db.Column(db.Integer)
#     amount_products = db.Column(db.Integer)

class ReceiveOrder(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String)
    user_email = db.Column(db.String)
    user_address = db.Column(db.String)
    user_city = db.Column(db.String)
    user_zip_code = db.Column(db.String)
    user_country = db.Column(db.String)
    order_price = db.Column(db.Integer)
    products = db.Column(db.String)



