import os
from flask import Flask

app = Flask(__name__)

port = int(os.environ.get('PORT', 3000))

@app.route("/200")
def route200():
    return "Result 200"
@app.route("/200", methods=["POST"])
def route200post():
    return "POST Result 200"

@app.route("/400")
def route400():
    return "Result 400", 400 
@app.route("/400", methods=["POST"])
def route400post():
    return "POST Result 400", 400 

@app.route("/500")
def route500():
    return "Result 500", 500
@app.route("/500", methods=["POST"])
def route500post():
    return "POST Result 500", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port)