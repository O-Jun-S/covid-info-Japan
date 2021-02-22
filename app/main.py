from flask import Flask
from flask import render_template
from .covid_api.covid_api import CovidApi

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def index():
    api = CovidApi()
    api.get_json_data()
    positive = api.get_positive_data()
    return render_template("index.html", positive=positive)
