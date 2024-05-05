from os import abort
from flask import Flask,render_template,request,session,redirect,url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "find-the-flag-my-man"

def getCurrentLogin():
    username=""
    login_auth = False
    if "username" in session:
        username = session["username"] 
        login_auth = True
    return username,login_auth


@app.route("/")
def Index():
    username,login_auth = getCurrentLogin()
    return render_template("index.html",username=username,login_auth=login_auth)

@app.route("/login",methods=["get","post"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                connection = sqlite3.connect("test.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE username='"+username+"' and password='"+password+"'")
                data = cursor.fetchone()
                if data != None:
                    session["username"] = username
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))
        abort(400)
    username,login_auth = getCurrentLogin()
    return render_template("login.html",username=username,login_auth=login_auth)



@app.route("/logout")
def Logout():
    if "username" in session:
        del session["username"]
    return redirect(url_for("Index"))


if __name__ == "__main__":
    app.run(debug=True)

