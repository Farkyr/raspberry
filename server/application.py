from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

from blueprints.led_blueprint import bp_led
from blueprints.api_blueprint import bp_api
from models.light import lightSensor

app.register_blueprint(bp_led)
app.register_blueprint(bp_api)

@app.route('/')
def index():
    return render_template('index.html', lightSensor = lightSensor)
