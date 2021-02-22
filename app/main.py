from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
