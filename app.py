from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def home(name=None):
    car_list = [["Nissan GTR Skyline","2016","20 LAKH INR"],["Ford Mustang", "2015", "30 LAKH INR"],["BMW M3","2012","20 LAKH INR"]]
    return render_template('index.html', cars = car_list)
#def hello_world():
#    return "Welcome to AutoHub"
if __name__ == "__main__":
    app.run(port=5001, debug=True)
