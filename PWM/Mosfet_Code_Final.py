# Mosfet_Code_Final.py
# Author: Sam Brewster, Daniel Covaci, Austin Iverson, Isaac Ramirez
# Written 02NOV2023
# For ECSE 4230: Embedded Systems 1
#
# Purpose: To Output a PWM Frequency to a MOSFET.

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 				# Set the naming method for GPIO
GPIO.setup(12,  GPIO.OUT, initial=GPIO.LOW) 	# Setup the Output pin 12


pwm=GPIO.PWM(12,    10000)	# Create a PWM object with the given frequency on pin 12
pwm.ChangeFrequency(10000)	# Change the Frequency of the PWM object
pwm.start(50)			# Starts the PWM output at a 50% duty cycle
#pwm.stop()			# Stops the PWM when we're done

# Main Loop 
try:
    while True:

        print("Empty Loop") 	# Fill the Empty Loop

finally:
    
    pwm.stop()			# Stops the PWM
