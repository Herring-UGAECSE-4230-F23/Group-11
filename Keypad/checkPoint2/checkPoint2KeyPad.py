# Group 11's Keypad
#
# Created 14SEP2023
# Blessed with the mentorship of Dr. Herring
# Property of Samuel, Isaac, Austin, and Daniel

# Imports
import RPi.GPIO as GPIO
from time import sleep\
     
import sevenSegFuncCP2

#Allows for cleaner runtime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Outputs are pins 4,  17, 27, 22
# Inputs are pins  23, 24, 25, 5

'''Setup in the Input Pins'''
GPIO.setup(23, GPIO.IN)
state = GPIO.input(23)

GPIO.setup(24, GPIO.IN)
state = GPIO.input(24)

GPIO.setup(25, GPIO.IN)
state = GPIO.input(25)

GPIO.setup(5, GPIO.IN)
state = GPIO.input(5)

'''Setup the Output Pins and Start them at low'''
GPIO.setup(4,  GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)


'''Initialize the Variables'''
# Choices of the Keypad
one   = ['1', '2', '3', 'A']
two   = ['4', '5', '6', 'B']
three = ['7', '8', '9', 'C']
four  = ['*', '0', '#', 'D']

# Variable to stop loop
stop = 0
global currentState
currentState = 0

'''Function Called to Read a High GPIO Input from the Pi'''
def readKeyPad(rowNum, char):
    
    # The variable for the users Y Value
    curVal = -1
    
    # Sends a High to the Keypad to check for a High input in return
    GPIO.output(rowNum, GPIO.HIGH)
    
    # Deciphers what Y Input is received and returns value to user
    if GPIO.input(23) == 1:
        currentState = stop
        curVal = char[0]
    if GPIO.input(24) == 1:
        currentState = stop
        curVal = char[1]
    if GPIO.input(25) == 1:
        currentState = stop
        curVal = char[2]
    if GPIO.input(5) == 1:
        currentState = stop
        curVal = char[3]
    
    # Kills the High input
    GPIO.output(rowNum, GPIO.LOW)
    
    return curVal

'''Loop to Interact with the User'''
def lookForInput():
    
    stop = -1
 
 # Continuously calls the function with differing X Values until something is returned
    stop = readKeyPad(4, one)
    if stop != -1:
        return stop
    stop = readKeyPad(17, two)
    if stop != -1:
        return stop
    stop = readKeyPad(27, three)
    if stop != -1:
        return stop
    stop = readKeyPad(22, four)
    if stop != -1:
        return stop
    
    return stop 
    
def wantToPrint(stop, decimalPoint) :
    # Prints the chosen value
    print("You want to print ", stop)

    if (stop == '1') :
        sevenSegFunc.display1(decimalPoint)
    elif (stop == '2'):
        sevenSegFunc.display2(decimalPoint)
    elif (stop == '3'):
        sevenSegFunc.display3(decimalPoint)
    elif (stop == '4'):
        sevenSegFunc.display4(decimalPoint)
    elif (stop == '5'):
        sevenSegFunc.display5(decimalPoint)
    elif (stop == '6'):
        sevenSegFunc.display6(decimalPoint)
    elif (stop == '7'):
        sevenSegFunc.display7(decimalPoint)
    elif (stop == '8'):
        sevenSegFunc.display8(decimalPoint)
    elif (stop == '9'):
        sevenSegFunc.display9(decimalPoint)
    elif (stop == '0'):
        sevenSegFunc.display0(decimalPoint)
    elif (stop == 'A'):
        sevenSegFunc.displayA(decimalPoint)
    elif (stop == 'B'):
        sevenSegFunc.displayb(decimalPoint)
    elif (stop == 'C'):
        sevenSegFunc.displayC(decimalPoint)
    elif (stop == 'D'):
        sevenSegFunc.displayd(decimalPoint)
         
    sevenSegFunc.displayDP(decimalPoint)    
    
    clkCycle()
    return stop
    
def checkOnOff(currentState, isOn) :
    
    #wantToPrint(currentState)
    if (isOn == True) :
        isOn = False
    else :
        isOn = True
        
    print("isOn is now")
 
def clkCycle():

    GPIO.output(11, GPIO.HIGH)
    #sleep(.25)
    GPIO.output(11, GPIO.LOW)

def main() :
    
    isOn = True
    desiredKey = -1
    currentKey = '0'
    decimalPoint = False
    
    while True :
        
        desiredKey = -1
    
        while (desiredKey == -1) :
            desiredKey = lookForInput()
        
        if (desiredKey == '#') :
            if (isOn == True) :
                print("turn off")
                isOn = False
                sevenSegFunc.displayOFF()
                clkCycle()
            else :
                isOn = True
                print("turn on")
                wantToPrint(currentKey, decimalPoint)
        else :
            if (isOn == True):
            
                if(desiredKey == '*') :
                    print("decimal point")
                    decimalPoint = sevenSegFunc.displayDP(decimalPoint)
                    print(decimalPoint)
                    #wantToPrint(currentKey, decimalPoint)
                    sevenSegFunc.displayDP(decimalPoint)
                    clkCycle()
                else :
                    sevenSegFunc.displayDP(decimalPoint)
                    currentKey = wantToPrint(desiredKey, decimalPoint)
        
        sleep(1)
    
while True:
    main()

#GPIO.cleanup()

 
