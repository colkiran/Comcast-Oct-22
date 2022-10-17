
from flask import Flask, render_template

app  = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index03.html", username= name, contents="Fruits available in all seasons", fruits = ['Apple', 'Ornge', 'Grapes', 'Pineapple','Gauva', 'Watermelon', 'Banana', 'Strawberry'])

if __name__ == '__main__':
    app.run(debug=True)