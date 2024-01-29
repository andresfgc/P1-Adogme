from flask import render_template
from dogmanager import app, db


# @app.route("/")
# def home():
#     return render_template("base.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/test")
def test():
    return render_template("test.html")