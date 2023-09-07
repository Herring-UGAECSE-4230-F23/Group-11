#Group 11's RPIO Code

#imports the library
import RPi.GPIO as GPIO

#imports sleep function
from time import sleep

#Sets up the GPIO pin 27 to start at a low output.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)

#Forever loops to turn on and off the LED
while True:
    GPIO.output(27, GPIO.HIGH)
    sleep(.01)
    GPIO.output(27, GPIO.LOW)
    sleep(.02)

#Resets all GPIOs
GPIO.cleanup()
