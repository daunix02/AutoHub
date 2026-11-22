from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/cars")
def home():

    cars = [
        ["Nissan GTR Skyline", "2016", "20 LAKH INR", "nissangtr.jpg"],
        ["Ford Mustang", "2015", "30 LAKH INR", "mustang.jpg"],
        ["BMW M3", "2012", "20 LAKH INR", "bmw.jpg"],
        ["Lamborghini Aventodor", "2012" , "1 Cr INR", "lamboav.jpg" ],
        ["Ferrari F40", "2003" , "1 Cr INR", "ff40.jpg" ],
        ["McLaren F1", "2010" , "1 Cr INR", "mcf1.jpg" ]

    ]

    return render_template("index.html", cars=cars)
#def hello_world():
#    return "Welcome to AutoHub"
if __name__ == "__main__":
    app.run(port=5001, debug=True)
