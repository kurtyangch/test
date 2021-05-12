from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # name = "Kurt"
    # li = list(name)
    # dict = {"Name":"Kurt"}
    user_logged_in = False
    return render_template("basic.html", user_logged_in=user_logged_in)

# @app.route("/world")
# def hello_world():
#     return "<h1>Hello world</h1>"
#

# dynamic route
# @app.route("/user/<name>")
# def user(name):
#     return "<h1> This is a page for {}</h1>".format(name)


if __name__ =="__main__":
    app.run(debug=True)

# debug=True 在本地端開發時debug用