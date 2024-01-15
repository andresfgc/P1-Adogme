from flask import Flask, render_template
# if os.path.exists("env.py"):
#     import env


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dogs")
def dogs():
    return render_template("dogs.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)