from flask import Blueprint, redirect, url_for
from models.led import Led
import time

bp_led = Blueprint('led', __name__, url_prefix='/led')

Led.initialize()
leds = {
    'red': Led(18),
    'blue': Led(24)
}

redLed = Led(18)
blueLed = Led(24)

@bp_led.route('/on/<led_name>')
def led_on(led_name):
    leds[led_name].on()
    return redirect(url_for('index'))

@bp_led.route('/off/<led_name>')
def led_off(led_name):
    leds[led_name].off()
    return redirect(url_for('index'))

@bp_led.route('/blink/<led_name>')
def led_blink(led_name):
    leds[led_name].asyncBlink(10, 0.07)
    return redirect(url_for('index'))

@bp_led.route('/schema')
def schema():
    redLed.on(),
    time.sleep(0.5)
    blueLed.asyncBlink(10, 0.07),
    time.sleep(0.8)
    redLed.asyncBlink(10, 0.07)
    return redirect(url_for('index'))


@bp_led.route('/schema2')
def schema2():
    blueLed.asyncBlink(10, 0.07),
    time.sleep(1)
    redLed.asyncBlink(10, 0.07),
    time.sleep(1.5)
    redLed.on(),
    time.sleep(0.5)
    blueLed.on(),
    time.sleep(0.5)
    redLed.off(),
    time.sleep(0.5)
    blueLed.off(),

    return redirect(url_for('index'))