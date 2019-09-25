import RPi.GPIO as GPIO # Use GPIO Library
import time
GPIO.setwarnings(False)

ledPin = 11
GPIO.setMode(GPIO.BOARD)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.output(ledPin,GPIO.HIGH)

while True:
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(1)

GPIO.cleanup();