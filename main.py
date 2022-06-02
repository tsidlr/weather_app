from flask import Flask, render_template, request
import weather_api
from datetime import date

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("shared/base.html")


@app.route("/weather", methods = ["GET", "POST"])
def weather():
    if request.method == "GET": 
        return render_template("weather.html")
    stadt = request.form["Stadt"]
    city,weather_description,temperature = weather_api.getLocation(stadt)
    today = date.today()
    
    return render_template("weather.html", city = city, weather_description = weather_description, temperature = temperature, today = today)

# Test Seite
@app.route("/test", methods = ["GET", "POST"])
def test():
    if request.method == "GET": 
        return render_template("test.html")

    return render_template("weather.html")


app.run(debug=True)






