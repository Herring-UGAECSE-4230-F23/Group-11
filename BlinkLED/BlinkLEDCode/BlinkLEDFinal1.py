import RPi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(27, GPIO.HIGH)
    sleep(.01)
    GPIO.output(27, GPIO.LOW)
    sleep(.02)
    
GPIO.cleanup()