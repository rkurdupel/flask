from flask import Flask, render_template

app = Flask(__name__)   # create web-app Flask

# @app.route - декоратор, задати маршрут
@app.route("/") # за таким маршрутом http://127.0.0.1:5000/ 
def index():
    return "<h1>Hello World!</h1>"   # результат, що повертається у браузер
    #return "text"


@app.route("/about")    # @app.route("/about") - http://127.0.0.1:5000/about
def about():
    return "<b>About page</b>"


# ALL TEMPLATES SHOULD BE IN THE templates folder, otherwise flask will not be able to find them
@app.route("/html_template")
def template():
    return render_template("index.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")
@app.route("/my_contact")
def contract_details():
    return render_template("my_contact.html")

# якщо машрут route без "/" - буде помилка, if route without "/" error will occur:
#  ValueError: urls must start with a leading slash


if __name__== "__main__":   # при запуску app.py, після цієї умови більше нічого окрім функцій в класах не буде виконуватись
    app.run(debug = True)   # launch local web-server from this file
    # debug = True - запустити в режимі debug

# ЩОБ ПОКАЗУВАЛОСЬ ФОТО З html файлу потрібно створити папку static/images і туди закинути файл, 
# і в html файлі вказати шлях  path static/images/image_name.png