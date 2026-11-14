from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to AutoHub"
app.run(port=5001)
