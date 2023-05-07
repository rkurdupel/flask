from app import app, db
from flask import render_template, request, url_for, redirect, flash # url_for - generate url
from models import User, Project
from flask_login import login_user, logout_user, current_user, login_required

import datetime


from settings import *
# main page /
@app.route("/") # за таким маршрутом http://127.0.0.1:5000/

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
            return redirect(url_for("index"))
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
                return redirect(url_for('index'))   # redirect to the main page (index) using flask method redirect
            login_user(user)
        else:
            flash("Ban", "alert alert-danger")
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
        image = request.files["image_file"]     # get name from our picture from html file   
        image.save(PATH_STATIC + "img" + os.sep + "upload" + os.sep + image.filename)     # save picture in img/upload/
        new_project = Project(title = request.form["title"], description = request.form["description"], link = request.form["link"], image = image.filename)
        db.session.add(new_project)
        db.session.commit()
        flash("Added")  # flash message - project is added
        # request.form["row"]   # get row from  the database
    return render_template("new_project.html")

@app.route("/projects/<project_id>")
@login_required
def project_page(project_id):
    project = Project.query.get(int(project_id))   # get project  by id
    return render_template("project_page.html", project = project)  # project = project - transfer variable





# якщо машрут route без "/" - буде помилка, if route without "/" error will occur:
#  ValueError: urls must start with a leading slash
