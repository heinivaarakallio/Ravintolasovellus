from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    return redirect("/frontpage")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        errormessage = ""

        username = request.form["username"]
        if len(username) == 0:
            errormessage = "Käyttäjätunnuksen luominen ei onnistunut. Käyttäjätunnus ei saa olla tyhjä."

        password = request.form.getlist("password")
        if len(password[0]) == 0:
            errormessage = "Käyttäjätunnuksen luominen ei onnistunut. Salasana ei saa olla tyhjä."
        if password[0] != password[1]:
            errormessage = "Käyttäjätunnuksen luominen ei onnistunut. Salasanat eivät täsmää."

        role = request.form["role"]
        if role != "1" and role != "2":
            errormessage = "Käyttäjätunnuksen luominen ei onnistunut. Valitse joko peruskäyttäjän tai ylläpitäjän rooli."

        if len(errormessage) > 0:
            return render_template("signup.html", errormessage=errormessage)

        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        return redirect("/frontpage")

@app.route("/frontpage")
def frontpage():
    result = db.session.execute("SELECT content FROM restaurants")
    restaurants = result.fetchall()
    return render_template("frontpage.html", restaurants=restaurants)

@app.route("/new")
def new():
    return render_template("new.html")
