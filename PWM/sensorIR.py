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
        
        if ((time.time() - startTime) > 1) :
            
            elapsedTime = (time.time() - startTime)
            
            startTime = time.time()
            
            RPM = rotations
            #RPM /= elapsedTime

            RPM *= 60
            RPM /= 3
            RPM *= dutyCycle
            RPM /= 10
            rotations = 0
            
            expectedRPM = dutyCycle * 20 * 5         
            
            print("Duty Cycle: ", dutyCycle, "expectedRPM: ", expectedRPM, "actualRPM: ", RPM)
            
        if (GPIO.input(irPin) == 0) :
            
            rotations += 1
        
        # Get the state for each input pin
        clkState = GPIO.input(clk_pin)
        dtState  = GPIO.input(dt_pin)
        swState  = GPIO.input(sw_pin)


        # Check for rotary encoder movement
        if (clkState != clkLastState and dtState == 1) :
            
            if (dtState != clkState) :
                    
                dutyCycle += .5
                
                if (dutyCycle >= 100) :
                    
                    dutyCycle = 100
                
            else:
                
                dutyCycle -= .5
                
                if (dutyCycle <= 0) :
                    
                    dutyCycle = 1
            
        clkLastState = clkState
        time.sleep(0.01)


        if (swState == GPIO.LOW) :
                
            time.sleep(.3)
            
            if (isOn == True) :
                
                pwm.start(0)
                pwm.stop
                isOn = False
                
            else :
                    
                isOn = True
                pwm.ChangeFrequency(frequency)
                pwm.start(dutyCycle)
            
            print(isOn)
                
        if (isOn == False) :
            
            pwm.stop
            
        else :
            
            pwm.start(dutyCycle)
          
            
# Main Loop 
try:
    while True:

        turnRotaryEncoder()
        #pwm.ChangeFrequency(1000)
        #pwm.start(10)
        #print(GPIO.input(irPin))
        
        

        
finally:
    
    pwm.stop() # Stops the PWM
