from app import app, db
from flask import render_template, request, url_for, redirect, flash, session # url_for - generate url
from models import User, Item, Order, ReceiveOrder
from flask_login import login_user, logout_user, current_user, login_required

import datetime
from telebot import types


from settings import *






@app.route("/")

def hall_page():
    return render_template("hall.html")

# main page /
@app.route("/main") # за таким маршрутом http://127.0.0.1:5000/

@login_required # you should be logged in, otherwise you won't enter the page (mainpage)
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
    if request.method == "POST":
        is_username = User.query.filter_by(username=request.form["username"]).first()
        if is_username:
            flash("Such username already exists", "alert alert-warning")   # send alert warning to webpage, alert warning - catergory bootstrap docs
        
        elif len(request.form["password"]) < 6 or len(request.form["username"]) < 6: # if password or username less than 6 chars then
            flash("password or username should contain more than 6 chars !", "alert alert-danger")
        elif request.form["password"] == request.form["passwordCheck"]: # if password = repeat password

            user = User(name=request.form["name"], 
                    username=request.form["username"], 
                    )
            user.set_password_hash(request.form["password"])
            db.session.add(user)    # add user to database
            db.session.commit()     # commit changes
            flash("Profile created successfully", "alert alert-success")
            #return redirect(url_for('hall_page'))
            return redirect(url_for('signin'))
        else:
            flash("Passwords does not match", "alert alert-danger ")
    
    return render_template("signup.html")

@app.route("/signin", methods = ["POST", "GET"])
def signin():
    if current_user.is_authenticated:   # if user is already logged in and is trying to enter the log in page he will be redirected to the main page(index)
        return redirect(url_for("index"))
    if request.method == "POST":
        user = User.query.filter_by(username = request.form["username"]).first() # get username from database
        if user and user.check_password(request.form["password"]):  # if user exists and password match
            if login_user(user, remember = "True", duration = datetime.timedelta(days = 7)):    # if log in is successful, remember log in to cookie files, duration - time that session is saved (default value - 30 days) can change using datetime.timedelta(days = 5) 5 - amount of days
                return redirect(url_for('hall_page'))   # redirect to the main page (index) using flask method redirect
            login_user(user)
        else:
            flash("Username or Password is uncorrect", "alert alert-danger")
    return render_template("login.html")

@login_required # you should be logged in @login_required, @ - decorator
@app.route("/logout")
def logout():
    logout_user()   # logout the user
    flash("You logged out of the page", "alert alert-success")
    return redirect(url_for("signin"))

@login_required
@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/projects")
@login_required

def projects():
    print(1)
    return render_template("projects.html")

@app.route("/projects/new", methods = ["POST", "GET"])
@login_required
def new_project():
    if request.method == "POST":
        try:    # try to add a new project
            image = request.files["image_file"]     # get name for our picture from html file   
            image.save(PATH_STATIC + "img" + os.sep + "upload" + os.sep + image.filename)     # save picture in img/upload/
            new_project = Project(title = request.form["title"], 
                                description = request.form["description"], 
                                link = request.form["link"], 
                                status = request.form["status"],
                                image = image.filename,
                                user_id = current_user.get_id()
                                )
            db.session.add(new_project)
            db.session.commit()
            flash("Project is added")  # flash message - project is added
            # request.form["row"]   # get row from  the database
        except: # if error occurs
            db.session.rollback()   # cancel all changes if the problem occurred
            flash("Problem with adding a new project", category = "alert alert-danger")   # flash message with category danger
            # alert alert-danger - red color message
    return render_template("new_project.html")

@app.route("/projects/<project_id>")
@login_required
def project_page(project_id):
    project = Project.query.get(int(project_id))   # get project  by id
    return render_template("project_page.html", project = project)  # project = project - transfer variable




@app.route("/menu")
def menu_page():
    # item = request.form.get('cappuccino')
    # print(item) 
    return render_template("menu.html")


@app.route("/add_to_cart", methods = ["POST"])
def add_to_cart():
    print(1555)

    # data gets from input value = "data", value finds by name, name = "item"
    chosen_item = request.form.get('item')  # request.form.get('item') get from menu html item
    # returns name of the item that the usee has chosen
    print(chosen_item)

    dbItem = Item.query.filter_by(product_name = chosen_item).first()   # get product which user chose from database, first() - to get the first product
    #order = Order(user_id = current_user.id, product_name = dbItem.product_name, product_price = dbItem.price, product_picture)
    print(dbItem.price) # get the price of the product
    order = Order(
        user_id = current_user.id,
        product_name = dbItem.product_name,
        product_price = dbItem.price
        
    )
    db.session.add(order)   # add order to the Order table
    db.session.commit() # commit changes, otherwise anything will not save

    return redirect(url_for('cart_page', user_id = current_user.id))



def calculate_total_amount(user_id):
    total_amount = 0
    #orders = Order.query.all()

    orders = Order.query.filter_by(user_id = user_id).all()  # get all users orders

    for item in orders:
        total_amount += item.product_price  # calculate the total sum
        print(total_amount)
    return total_amount

@app.route('/cart/<user_id>')
@login_required # @login_required must be after the route ( /cart ) so the user could not enter the page if he is not logged in
def cart_page(user_id):
    orders = Order.query.filter_by(user_id = user_id).all() # get all user orders ( products that user sent to cart ) all() - all
    print(orders)
    print(len(orders), "len")
    order_length = len(orders)
    #orders = Order.query.all()
    #print(orders.product_name)
    total_amount = calculate_total_amount(user_id = user_id)
    print(total_amount)
   
    # for item in orders:
    #      image = f"static/images/{item.product_name}.png"   # make through separator os library !!!
    
    image = PATH_STATIC + 'images' + os.sep + "Cappuccino" + ".png"
    print(image)
    return render_template("cart.html", orders = orders, total_amount = total_amount, image = image, order_len = order_length)

@app.route("/check", methods = ["GET", "POST"])
@login_required
def checkout_page():
    current_user_id = current_user.id
    print(current_user_id)    
    return render_template("checkout.html")

@app.route("/process_checkout", methods = ["POST"])
@login_required
def process_checkout():
    name = request.form["full-name"]
    email = request.form["email"]
    address = request.form["user_address"]
    city = request.form["city"]
    zip_code = request.form["zip-code"]
    country = request.form["country"]
    total_amount = calculate_total_amount(user_id = current_user.id)    # current_user.id - id of the user that is currently logged in

    print(name, email, address, city, zip_code, country, total_amount)
    orders = Order.query.filter_by(user_id = current_user.id).all() # get all user orders ( products that user sent to cart ) all() - all
    print(orders)
    list_of_products = ""
    for order in orders:
        #print(order.product_name)
        list_of_products += order.product_name + '\n' # \n = new row
    print(list_of_products)

    new_order_receive = ReceiveOrder(
        user_name = name,
        user_email = email,
        user_address = address,
        user_city = city,
        user_zip_code = zip_code,
        user_country = country,
        order_price = total_amount,
        products = list_of_products
    )

    db.session.add(new_order_receive)
    db.session.commit()


    return redirect(url_for("order_info"))

@app.route('/order_status')
@login_required
def order_info():
     return render_template("order_status.html")

# якщо машрут route без "/" - буде помилка, if route without "/" error will occur:
#  ValueError: urls must start with a leading slash
