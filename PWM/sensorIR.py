# Import required libraries
import RPi.GPIO as GPIO
import time

# Encoder variables
clk_pin = 26  # GPIO pin connected to CLK (brown wire)
dt_pin = 19   # GPIO pin connected to DT (yellow wire)
sw_pin = 13   # GPIO pin connected to SW (orange wire)

# Debouncing variables
smallDelay = 0.02  # Delay for debouncing
debounce_threshold = 3

# Turns per second variables
rotation_counter = 0
start_time = time.time()

octoPin = 20

GPIO.setmode(GPIO.BCM)  # Set the naming method for GPIO
GPIO.setup(octoPin,  GPIO.OUT, initial=GPIO.LOW)  # Setup the Output pin 12

pwm=GPIO.PWM(octoPin, 0.1) # Create a PWM object with the given frequency on pin 12
pwm.ChangeFrequency(  0.1) # Change the Frequency of the PWM object

# GPIO board and pin setup for the rotary encoder and switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
clkState_last = GPIO.input(clk_pin)

''' Function to handle rotary encoder input and initialization of variables '''
# Authors: Sam, Daniel, and Isaac
def turnRotaryEncoder():
    # Initialize and Declare Numerous Variables for the Rotary Encoder
    clkState = 0
    dtState = 0
    clkLastState = 0
    startTimeTurnRE = 0
    timeSinceLast = 0
    timeTakenToSpin = 0
    startTimeTurnRE = 0
    start_time = 0
    stop_time = 0
    endTime = 0
    increment = 0
    none_time = 0
    speed = 10
    
    # Value of GPIO 24 is continuously stored in the clkLastState variable
    clkLastState = GPIO.input(clk_pin)
    pwm.start(50)

    # Main Loop
    while True:

        # Get the state for each input pin
        clkState = GPIO.input(clk_pin)
        dtState = GPIO.input(dt_pin)
        swState = GPIO.input(sw_pin)

        # Check for rotary encoder movement
        if (clkState != clkLastState and dtState == 1) :

            
            if (dtState != clkState) :
                
                    
                speed += .25
                
            else:
                
                speed -= .25
            
            time.sleep(0.001)

        # Update the rotary encoder
        clkLastState = clkState
        pwm.ChangeFrequency(speed)
        time.sleep(0.001)


# Main Loop 
try:
    while True:

        turnRotaryEncoder()

finally:
    
    pwm.stop() # Stops the PWM

