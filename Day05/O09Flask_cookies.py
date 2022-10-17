
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index04.html", uname="Mohammed Ali")

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("Success")
    resp.set_cookie("Cookie1", "Its rainy day today....")
    resp.set_cookie("Cookie2", "its a sunny day today...")
    return resp

@app.route("/get_cookie")
def get_cookie():
    val1 = request.cookies.get("Cookie1")
    val2 = request.cookies.get("Cookie2")
    if val1 == None:
        val1 = "Cookie Deleted......"
    elif val2 == None:
        val2 = "Cookie Deleted......."
    return "<h2> First cookie :" + val1 + "<br> Second Cookie :" + val2 + "</h2>"

@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("Deleted cookie successfully... ")
    resp.delete_cookie("Cookie1")
    return resp

if __name__ == '__main__':
    app.run(debug=True)

