from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def home(name=None):
    return render_template('index.html', person=name)
#def hello_world():
#    return "Welcome to AutoHub"
app.run(port=5001)
