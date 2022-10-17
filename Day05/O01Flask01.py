
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route("/<username>")
def user(username):
    return f"<h2> Hello {username} </h2>"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(port=8000)
