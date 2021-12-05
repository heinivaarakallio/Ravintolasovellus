from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("test.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    sql = "SELECT id, password FROM users WHERE username_:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        # TODO: invalid username
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            # TODO: correct username and password
        else:
            # TODO: invalid password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

