from flask import Flask

app = Flask(__name__)

@app.route("/200")
def route200():
    return "Result 200"
@app.route("/400")
def route400():
    return "Result 400", 400 
@app.route("/500")
def route500():
    return "Result 500", 500

if __name__ == "__main__":
    app.run()