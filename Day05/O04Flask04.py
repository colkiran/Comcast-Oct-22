

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index01.html", adj="This is my first web page using Flask", x = 100)
if __name__ == '__main__':
    app.run(debug =True)
