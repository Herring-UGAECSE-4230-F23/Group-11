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

irPin   = 21    #IR sensor GPIO pin number 

GPIO.setmode(GPIO.BCM)  # Set the naming method for GPIO
GPIO.setup(octoPin,  GPIO.OUT, initial=GPIO.LOW)  # Setup the Output pin 12

pwm=GPIO.PWM(octoPin,1000) # Create a PWM object with the given frequency on pin 12
pwm.ChangeFrequency(20) # Change the Frequency of the PWM object

# GPIO board and pin setup for the rotary encoder and switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(irPin, GPIO.IN)
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
    dutyCycle = 50
    rotations = 0
    startTime = 0
    theoSpeed = 0
    RPM = 0
    debounce_threshold = 1
    frequency = 1000
    expectedRPM = 0

    # Value of GPIO 24 is continuously stored in the clkLastState variable
    clkLastState = GPIO.input(clk_pin)
    pwm.start(dutyCycle)
    pwm.ChangeFrequency(frequency)
    isOn = True
    topOfTheHour = True
    startTime = time.time()

    # Main Loop
    while True:
        
        # Checks to see if a second has elapsed
        if ((time.time() - startTime) > 1) :
            
            
            #elapsedTime = (time.time() - startTime)
            
            startTime = time.time()    # Restart the timer
            
            RPM = rotations            # Set the RPM = Rotations
            #RPM /= elapsedTime        # Commented out for experimeting
            RPM *= 60                  # Make RPM = Rotations Per Minute
            RPM /= 3                   # Divide By 3 because there are 3 fan blades
            RPM *= dutyCycle           # Mutiply by the duty cycle to account for discharge rate
            RPM /= 10                  # Divide by 10 to account for the duty cycle
            
            rotations = 0              # Reset Rotations
            
            expectedRPM = dutyCycle    # Make the expectedRPM equal to the duty cycle
            expectedRPM *= 60          # Multipy by 60 to make it per minute
            expectedRPM /= 3           # Divide by 3 to account for 3 fan blades
            expectedRPM *= 3           # Muliply by 3 to account for error (Found by counting RPM in Slo Mo)
            
            print("Duty Cycle: ", dutyCycle, "expectedRPM: ", expectedRPM, "actualRPM: ", RPM)
            
        # Counts when the IR Sensor is Obstructed
        if (GPIO.input(irPin) == 0) :
            
            rotations += 1             # Increments the Rotations Per Second
        
        # Get the state for each input pin
        clkState = GPIO.input(clk_pin)
        dtState  = GPIO.input(dt_pin)
        swState  = GPIO.input(sw_pin)


        # Check for rotary encoder movement
        if (clkState != clkLastState and dtState == 1) :
            
            if (dtState != clkState) :
                    
                dutyCycle += 2.5
                
                # Check if within boundaries
                if (dutyCycle >= 100) :
                    
                    dutyCycle = 100
                
            else:
                
                dutyCycle -= 2.5
                
                # Check if within boundaries
                if (dutyCycle <= 0) :
                    
                    dutyCycle = 1
            
        clkLastState = clkState
        time.sleep(0.01) # Debounce

        # In our slow motion video, we found 22 spins per second on 12 duty cycle

        # Logic For Button Press
        if (swState == GPIO.LOW) :
                
            # Debounce
            time.sleep(.3)
            
            # Switch On to Off and Off to On Logic
            if (isOn == True) :
                
                # Kill the Output
                pwm.start(0)
                pwm.stop
                isOn = False
                
            else :
                   
                # Restart the Output
                isOn = True
                pwm.ChangeFrequency(frequency)
                pwm.start(dutyCycle)
          
            
# Main Loop 
try:
    while True:

        turnRotaryEncoder()       

        
finally:
    
    pwm.stop() # Stops the PWM
