from flask import Flask,render_template,request,redirect,url_for,render_template_string
import sqlite3

app = Flask(__name__)       

@app.route("/",methods=["POST","GET"])
def xpathinjection():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username='"+username+"' and password='"+password+"'")
        data = str(cursor.fetchall())
        return data
    else:
        return render_template("index.html")
    


if __name__ == "__main__":
    app.run(debug=True)