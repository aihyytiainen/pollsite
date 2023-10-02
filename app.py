from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/sign_up")
def sign_up():
	return render_template("sign_up.html")

@app.route("/new_user", methods=["POST"])
def new_user():
	username = request.form["username"]
	password = request.form["password"]
	groupA = False
	groupB = False
	groupC = False
	groupD = False
	if username and password:
		hash_value = generate_password_hash(password)
		sql = "INSERT INTO users (username, password, groupA, groupB, groupC, groupD) VALUES (:username, :password, :groupA, :groupB, :groupC, :groupD)"
		db.session.execute(text(sql), {"username":username, "password":hash_value, "groupA":groupA, "groupB":groupB, "groupC":groupC, "groupD":groupD})
		db.session.commit()
		session["username"] = username
		return redirect("/")
	return redirect("/sign_up")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/loginuser",methods=["POST"])
def login_user():
	username = request.form["username"]
	password = request.form["password"]
	sql = text("SELECT id, password FROM users WHERE username=:username")
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if not user:
		return render_template("login_fail.html")
	else:
		hash_value = user.password
		if check_password_hash(hash_value, password):
			session["username"] = username
			return redirect("/")
		else:
			return render_template("login_fail.html")

#@app.route("/loign_fail")
#def login_fail():
#	render_template("login_fail.html")


@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")
