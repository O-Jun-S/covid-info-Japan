from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler

import sys

sys.path.append("./covid_data/")

from .covid_data.get_positive_data import GetPositiveData
from .covid_data.get_death_data import GetDeathData
from .covid_data.get_pcr_data import GetPcrData
from .covid_data.get_patient_data import GetPatientData
from .covid_data.data_control import DataControl


# set configuration values
class Config(object):
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

get_positive_data = GetPositiveData()
get_death_data = GetDeathData()
get_pcr_data = GetPcrData()
get_patient_data = GetPatientData()

@scheduler.task('interval', id='write_data', hours=2)
def write_data():
    get_positive_data.get_data()
    get_positive_data.write_data()
    get_death_data.get_data()
    get_death_data.write_data()
    get_pcr_data.get_data()
    get_pcr_data.write_data()
    get_patient_data.get_data()
    get_patient_data.write_data()


@app.route("/")
def index():
    data_control = DataControl()

    positive = data_control.get_positive_data()
    death = data_control.get_death_data()
    pcr = data_control.get_pcr_data()
    patient = data_control.get_patient_data()
    return render_template(
        "index.html",
        date=data_control.the_day_key,
        positive=positive,
        death=death,
        pcr=pcr,
        patient=patient,
        )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
