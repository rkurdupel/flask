from app import app, db
from flask import render_template, request, url_for, redirect, flash # url_for - generate url
from models import User, Project



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
        else:
            flash("Passwords does not match", "alert alert-danger ")
        

    return render_template("signup.html")

@app.route("/signin", methods = ["POST", "GET"])
def signin():
    return render_template("login.html")

# якщо машрут route без "/" - буде помилка, if route without "/" error will occur:
#  ValueError: urls must start with a leading slash