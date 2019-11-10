from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def info():
    return "<h1>We are store!</h1>"

@app.route("/product", methods=["GET","POST"])
def product():
    arr = {"type": "food"}, {"price": "10"}, {"name": "product"}
    return str(arr)

if __name__ == "__main__":
    app.run(debug=True)
