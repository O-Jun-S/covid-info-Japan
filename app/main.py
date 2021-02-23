from flask import Flask
from flask import render_template
from .covid_data.get_positive_data import GetPositiveData
from .covid_data.get_death_data import GetDeathData
from .covid_data.get_pcr_data import GetPcrData
from .covid_data.get_patient_data import GetPatientData
from .covid_data.data_control import DataControl

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

get_positive_data = GetPositiveData()
get_death_data = GetDeathData()
get_pcr_data = GetPcrData()
get_patient_data = GetPatientData()

@app.route("/")
def index():
    get_positive_data.get_data()
    get_positive_data.write_data()

    get_death_data.get_data()
    get_death_data.write_data()

    get_pcr_data.get_data()
    get_pcr_data.write_data()

    get_patient_data.get_data()
    get_patient_data.write_data()

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
