# Import required libraries
import RPi.GPIO as GPIO
import time

# Encoder variables
clk_pin = 24  # GPIO pin connected to CLK (brown wire)
dt_pin = 23   # GPIO pin connected to DT (yellow wire)
sw_pin = 22   # GPIO pin connected to SW (orange wire)

# Debouncing variables
smallDelay = 0.02  # Delay for debouncing
debounce_threshold = 3

# Turns per second variables
rotation_counter = 0
start_time = time.time()

# GPIO board and pin setup for the rotary encoder and switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
clkState_last = GPIO.input(clk_pin)

# Function to handle rotary encoder input and initialization of variables
def turnRotaryEncoder():
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
    # Value of GPIO 24 is continuously stored in the clkLastState variable
    clkLastState = GPIO.input(24)

    while True:
        clkState = GPIO.input(clk_pin)
        dtState = GPIO.input(dt_pin)
        swState = GPIO.input(sw_pin)
        start_time = time.time()

        # Check for rotary encoder movement
        if clkState != clkLastState and dtState == 1:
            startTimeTurnRE = timeSinceLast
            timeSinceLast = time.time()
            timeTakenToSpin = (time.time() - startTimeTurnRE)
            startTimeTurnRE = time.time()
            stop_time = time.time()
            endTime = (1 / 20) * (stop_time - start_time) * 10000000

            # Determine the direction of rotation and print the result
            if dtState != clkState:
                print("Clockwise            Turns Per Second: " + str(endTime))
            else:
                print("CounterClockwise     Turns Per Second: " + str(endTime))

            none_time = time.time()
            time.sleep(0.001)

        # Check for button press and output button is pressed
        elif swState == GPIO.LOW:
            buttonDebouncing_counter = 0
            while swState == GPIO.LOW and buttonDebouncing_counter < debounce_threshold:
                time.sleep(smallDelay)
                swState = GPIO.input(sw_pin)
                buttonDebouncing_counter += 1

            if swState == GPIO.LOW and buttonDebouncing_counter >= debounce_threshold:
                print("SWITCH PRESSED")

            none_time = time.time()
            time.sleep(1)

        # Check for no input and output None
        if (start_time - none_time) > 0.35:
            print("None")

        clkLastState = clkState
        time.sleep(0.001)

# Main loop to handle the rotary encoder input
while True:
    turnRotaryEncoder()
