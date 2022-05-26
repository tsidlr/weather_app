import requests
from geopy.geocoders import Nominatim

# Key für die Wetter API
API_KEY = "2bc2a65563d90c431627a08a6de9ef1f"

# GeoPy API um Längengrad und Breitengrad der eingegeben Städte zu erhalten
def getLocation (eingabe):
    locator = Nominatim(user_agent="fintu-blog-geocoding-python")
    location = locator.geocode(eingabe)

    breitenGrad = location.latitude
    längenGrad = location.longitude
    return getWeather(breitenGrad,längenGrad)

def getWeather (breitenGrad, längenGrad):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={breitenGrad}&lon={längenGrad}&appid={API_KEY}"

    response = requests.get(request_url)

    # Check ob die Abfrage funktioniert
    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        weather_description = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] -273.15)
    

        print("Name: " + city)
        print("Wetterbeschreibung: " + weather_description)
        print("Temperatur: " + str(temperature))
    
        return city,weather_description,temperature
    else:
        print("Fehler")

