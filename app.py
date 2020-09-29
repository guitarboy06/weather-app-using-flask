from flask import Flask, render_template, request
from search import data

app = Flask(__name__)
api_key = "9c8e7b21a572ffc5f7ae3222bfc333ca"


@app.route('/', methods=["POST", "GET"])
def weather():
    if request.method == "POST":
        city = request.form["city"]
        country = request.form["country"]
        res = data(city, country, api_key)
        #icon = f"http://openweather.org/img/w/{res[4]}.png"
        return render_template("weather.html", temp=res[0], humidity=res[1], sky=res[2], wind_speed=res[3], icon=res[4], city=city)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
