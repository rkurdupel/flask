from flask import Flask

app = Flask(__name__)   # create web-app Flask

# @app.route - декоратор, задати маршрут
@app.route("/") # за таким маршрутом http://127.0.0.1:5000/ 
def index():
    return "<h1>Hello World!</h1>"   # результат, що повертається у браузер
    #return "text"

@app.route("/about")    # @app.route("/about") - http://127.0.0.1:5000/about
def about():
    return "<b>About page</b>"

if __name__== "__main__":   # при запуску app.py
    app.run(debug = True)   # launch local web-server from this file
    # debug = True - запустити в режимі debug


