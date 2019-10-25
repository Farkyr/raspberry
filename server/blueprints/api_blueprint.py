from flask import Blueprint, redirect, url_for, jsonify
from models.light import lightSensor

bp_api = Blueprint('api', __name__, url_prefix='/api')

@bp_api.route('/light')
def light_json():
    light = lightSensor.read_light()
    return jsonify({
        'light': light
    })