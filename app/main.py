from flask import Flask
from flask import render_template
from .covid_data.get_positive_data import GetPositiveData
from .covid_data.data_control import DataControl

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

get_positive_data = GetPositiveData()

@app.route("/")
def index():
    get_positive_data.get_data()
    get_positive_data.write_data()
    data_control = DataControl()

    positive = data_control.get_positive_data()
    return render_template("index.html", date=data_control.yesterday_key, positive=positive, death=0)
