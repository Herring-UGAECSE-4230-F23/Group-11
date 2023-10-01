# Group 11's Keypad
#
# Created 28SEP2023
# Blessed with the mentorship of Dr. Herring
# Property of Samuel, Isaac, Austin, and Daniel

# Imports
import RPi.GPIO as GPIO
from time import sleep\
     
import sevenSegFunc

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

GPIO.setup(18,  GPIO.OUT, initial=GPIO.LOW) 


''' Clock Pins '''
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # clock cycle 1
GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW) # clock cycle 2
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # clock cycle 3
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # clock cycle 4


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
def lookForInput(blink):
    
    stop = -1
 
    if (blink == True) :
         
        sevenSegFunc.blinkScreen()
 
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
    
    
    
''' Prints the Value That Was Selected '''
def wantToPrint(stop, decimalPoint) :

    # Logic that sends calls the corresponding display to the user input
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
        sevenSegFunc.display0()
    
    return stop



''' Function to Make the LED Blink '''
def blinkLED() :
    
    GPIO.output(18, GPIO.HIGH) # Turns LED On
    sleep(1)                   # Waits
    GPIO.output(18, GPIO.LOW)  # Turns LED Off



''' Calls the Clock Cycle '''
def clkCycle(cycleNum):
    
    if (cycleNum == 1) :   # Clock pulses for first digit
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
    elif (cycleNum == 2) : #Clock pulses for second digit
        GPIO.output(9, GPIO.HIGH)
        GPIO.output(9, GPIO.LOW)
    elif (cycleNum == 3) : # Clock pulses for third digit
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
    elif (cycleNum == 4) : # Clock pulses for fourth digit
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)



''' Invalid Entries Not Important Yet'''
def checkInvalid(currentFirst, currentSecond, currentThird, currentFourth) :
    
    if (currentFirst == '2' and (currentSecond != '0' or currentSecond != '1' or currentSecond != '2' or currentSecond != '3')) :
        print("WRONG")
        return True
    elif (currentFirst != '0' and currentFirst != '1' and currentFirst != '2'):
        print("WRONG")
        return True
    elif (currentSecond == 'A' or currentSecond == 'B' or currentSecond == 'C' or currentSecond == 'D'):
        return True
    elif (currentThird == 'A' or currentThird == 'B' or currentThird == 'C' or currentThird == 'D'):
        return True
    elif (currentFourth == 'A' or currentFourth == 'B' or currentFourth == 'C' or currentFourth == 'D'):
        return True

''' Checks if the Input is a Letter '''
def isALetter(stop) :
    
    if (stop == 'A'):
        blinkLED()
    elif (stop == 'B'):
        blinkLED()
    elif (stop == 'C'):
        blinkLED()
    elif (stop == 'D'):
        blinkLED()

''' Initialize Clock '''
def blankClock () :
    
    #Output the Number 0
    sevenSegFunc.display0()
    GPIO.output(16, GPIO.LOW)
    
    sevenSegFunc.clkCycle(1)    # Call Clock One
    sevenSegFunc.clkCycle(2)    # Call Clock Two
    sevenSegFunc.clkCycle(3)    # Call Clock Three
    sevenSegFunc.clkCycle(4)    # Call Clock Four

''' Main Function '''
def main() :
    
    isOn = True
    desiredKey = -1
    currentFirst = '0'
    currentSecond = '0'
    currentThird = '0'
    currentFourth = '0'
    decimalPoint = False
    cycleNum = 1
    checkClock = False
    blink = False
    
    blankClock()
    
    while True :
        
        desiredKey = -1
        
        if(checkClock == True) :
                        
            if (checkInvalid(currentFirst, currentSecond, currentThird, currentFourth) == True) :
                            
                currentFirst  = '0'
                currentSecond = '0'
                currentThird  = '0'
                currentFourth = '0'
                            
                blankClock()
                blink = True
                            
            #Output a high to the LED
            checkClock = False
            cycleNum = 1
    
        while (desiredKey == -1) :
            desiredKey = lookForInput(blink)
        
        if (desiredKey == '#') :
            if (isOn == True) :
                print("turn off")
                isOn = False
                sevenSegFunc.displayOFF()
                clkCycle(1)
                clkCycle(2)
                clkCycle(3)
                clkCycle(4)
            else :
                isOn = True
                print("turn on")
                print(currentFirst)
                print(currentSecond)
                print(currentThird)
                print(currentFourth)
                wantToPrint(currentFirst, decimalPoint)
                clkCycle(1)
                wantToPrint(currentSecond, decimalPoint)
                clkCycle(2)
                wantToPrint(currentThird, decimalPoint)
                clkCycle(3)
                wantToPrint(currentFourth, decimalPoint)
                clkCycle(4)
            
        elif (desiredKey == 'A' or desiredKey == 'B' or desiredKey == 'C' or desiredKey == 'D') :
            
            isALetter(desiredKey)
            
        elif (desiredKey == '*') :
                decimalPoint = True
                sevenSegFunc.displayDP(decimalPoint)
                wantToPrint(currentSecond, decimalPoint) # Prints the Desired Character and stores it in the currentKey spot
                sevenSegFunc.clkCycle(2)
            
        else :
            if (isOn == True):
            
                if(desiredKey == '*') :
                    #print("decimal point")
                    #decimalPoint = sevenSegFunc.displayDP(decimalPoint)
                    #print(decimalPoint)
                    #wantToPrint(currentKey, decimalPoint)
                    #sevenSegFunc.displayDP(decimalPoint)
                    #wantToPrint(desiredKey, decimalPoint) # Prints the Desired Character and stores it in the currentKey spot
                    #sevenSegFunc.clkCycle(2)
                    print("hi mom")
                else :
                    blink = False
                    sevenSegFunc.displayDP(decimalPoint) # Displays the decimal point if it is supposed to be on screen, will need a clock call here so that it updates
                                
                    if (cycleNum == 1) :
                        currentFirst = wantToPrint(desiredKey, decimalPoint) # Prints the Desired Character and stores it in the currentKey spot
                    elif (cycleNum == 2) :
                        currentSecond = wantToPrint(desiredKey, decimalPoint) # Prints the Desired Character and stores it in the currentKey spot
                    elif (cycleNum == 3) :
                        currentThird = wantToPrint(desiredKey, decimalPoint) # Prints the Desired Character and stores it in the currentKey spot
                    elif (cycleNum == 4) :
                        currentFourth = wantToPrint(desiredKey, decimalPoint) # Prints the Desired Character and stores it in the currentKey spot
                    
                    
                    sevenSegFunc.clkCycle(cycleNum)
                    
                    if (cycleNum == 4) :
                        cycleNum = 1
                        checkClock = True
                    else :
                        cycleNum += 1
        sleep(.5)
    
while True:
    main()

#GPIO.cleanup()

 