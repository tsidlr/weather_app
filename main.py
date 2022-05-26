from flask import Flask, render_template, request
import weather_api
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/weather", methods = ["GET", "POST"])
def weather():
    if request.method == "GET": 
        return render_template("weather.html")
    stadt = request.form["Stadt"]
    city,weather_description,temperature = weather_api.getLocation(stadt)
    print(city,weather_description,temperature)
    return render_template("weather.html", city = city, weather_description = weather_description, temperature = temperature)

app.run(debug=True)






