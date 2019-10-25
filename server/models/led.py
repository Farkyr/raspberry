#import des utilistaires python
import RPi.GPIO as GPIO
import time
from threading import Thread

class Led:
    def __init__(self, numGPIO):
        self.numGPIO = numGPIO
        GPIO.setup(numGPIO, GPIO.OUT)

    def on(self):
        print('Led {} on'.format(self.numGPIO))
        GPIO.output(self.numGPIO, GPIO.HIGH)

    def off(self):
        print('Led {} off'.format(self.numGPIO))
        GPIO.output(self.numGPIO, GPIO.LOW)

    def blink(self, numBlink, sleepTime):
        i = 0
        while i < numBlink:
            self.on()
            time.sleep(sleepTime)
            self.off()
            time.sleep(sleepTime)
            i += 1

    def asyncBlink(self, numBlink, sleepTime):
        thread = Thread(target=self.blink, args=(numBlink, sleepTime, ))
        thread.start()
        return thread

    @classmethod
    def initialize(cls):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @classmethod
    def clean(cls):
        GPIO.cleanup()

Led.initialize()

# redLed = Led(18)
# blueLed = Led(24)
# redThread = redLed.asyncBlink(5, 0.25)
# blueThread = blueLed.asyncBlink(10, 0.5)
# redLed.blink(10, 0.25)
# blueLed.blink(50, 0.05)
# redLed.on()
# time.sleep(1)
# redLed.off()
# blueLed.on()
# time.sleep(1)
# blueLed.off()
# blueThread.join()
# redThread.join()
# Led.clean()