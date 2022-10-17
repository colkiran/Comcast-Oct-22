
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
flag = False
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template("index04.html", uname="Mike Tyson")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    global flag
    flag = False

    if request.method == 'POST':
        user = request.form['nm']
        flag = True
        return redirect(url_for("user", usr=user))
    else:
        flag=False
        if flag == False:
            flash("You have used GET method")
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    global flag
    if flag:
        flash("You have used POST method.....")
    return render_template("result.html", usr=usr)

if __name__ == '__main__':
    app.run(debug=True)

