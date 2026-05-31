from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import geocoder
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    location = None

    if request.method == "POST":
        number = request.form["number"]

        parsed = phonenumbers.parse(number)
        country = geocoder.description_for_number(parsed, "en")

        location = country

    return render_template("index.html", location=location)

if __name__ == "__main__":
    app.run()
