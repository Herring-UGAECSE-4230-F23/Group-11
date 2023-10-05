# Group 11's Keypad
#
# Created 28SEP2023
# Blessed with the mentorship of Dr. Herring
# Property of Samuel, Isaac, Austin, and Daniel

# Imports
import RPi.GPIO as GPIO
from datetime import datetime
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

now = datetime.now()

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
    
    
    
''' Prints the Value That Was Selected '''
def wantToPrint(stop) :

    # Logic that sends calls the corresponding display to the user input
    if (stop == '1') :
        sevenSegFunc.display1()
    elif (stop == '2'):
        sevenSegFunc.display2()
    elif (stop == '3'):
        sevenSegFunc.display3()
    elif (stop == '4'):
        sevenSegFunc.display4()
    elif (stop == '5'):
        sevenSegFunc.display5()
    elif (stop == '6'):
        sevenSegFunc.display6()
    elif (stop == '7'):
        sevenSegFunc.display7()
    elif (stop == '8'):
        sevenSegFunc.display8()
    elif (stop == '9'):
        sevenSegFunc.display9()
    elif (stop == '0'):
        sevenSegFunc.display0()
    elif (stop == 1) :
        sevenSegFunc.display1()
    elif (stop == 2):
        sevenSegFunc.display2()
    elif (stop == 3):
        sevenSegFunc.display3()
    elif (stop == 4):
        sevenSegFunc.display4()
    elif (stop == 5):
        sevenSegFunc.display5()
    elif (stop == 6):
        sevenSegFunc.display6()
    elif (stop == 7):
        sevenSegFunc.display7()
    elif (stop == 8):
        sevenSegFunc.display8()
    elif (stop == 9):
        sevenSegFunc.display9()
    elif (stop == 0):
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


''' Initialize Clock '''
def blankClock () :
    
    #Output the Number 0
    sevenSegFunc.display0()
    GPIO.output(16, GPIO.LOW)
    
    sevenSegFunc.clkCycle(1)    # Call Clock One
    sevenSegFunc.clkCycle(2)    # Call Clock Two
    sevenSegFunc.clkCycle(3)    # Call Clock Three
    sevenSegFunc.clkCycle(4)    # Call Clock Four


''' Displays the Parsed Numbers to the Pi '''
def displayTime(hOne, hTwo, mOne, mTwo) :
    
    #print(hOne, hTwo, mOne, mTwo)
    
    wantToPrint(hOne)
    clkCycle(1)
    wantToPrint(hTwo)
    clkCycle(2)
    wantToPrint(mOne)
    clkCycle(3)
    wantToPrint(mTwo)
    clkCycle(4)
 
def getTime() :
    
    now = datetime.now()
    
    currentTime = now.strftime("%H: %M: %S")
    
    return currentTime
    
''' Does the automatic Clock '''    
def automaticClock() :

    isOn = True
    threeBs = 0
    iterations = 0
    desiredKey = -1
    
    currentFirst = '0'
    currentSecond = '0'
    currentThird = '0'
    currentFourth = '0'
    
    currentTimeArray = list(getTime())
    
    autoHours = int(currentTimeArray[0])*10 + int(currentTimeArray[1])
    autoMinutes = int(currentTimeArray[4])*10 + int(currentTimeArray[5])
    autoSeconds = int(currentTimeArray[8])*10 + int(currentTimeArray[9])
    
    hOne = int(autoHours/10)
    hTwo = int(autoHours%10)
    mOne = int(autoMinutes/10)
    mTwo = int(autoMinutes%10)
    displayTime(hOne, hTwo, mOne, mTwo)

    while (threeBs < 3) :
        
        hOne = int(autoHours/10)
        hTwo = int(autoHours%10)
        mOne = int(autoMinutes/10)
        mTwo = int(autoMinutes%10)
        
        if (desiredKey == -1) :
            
            desiredKey = lookForInput()
        
            if (desiredKey == '#') :
                
                threeBs = 0
                
                ''' Turns the Keypad completely off/back on '''
                if (isOn == True) :
                    # Sets the Display State to Off
                    isOn = False
                    
                    # Calls the Display to turn every segment Off
                    sevenSegFunc.displayOFF()
                    
                    # Calls each clock to update to the Off Call
                    clkCycle(1)
                    clkCycle(2)
                    clkCycle(3)
                    clkCycle(4)
                    
                else :
                    # Sets the Display State to Back On
                    isOn = True
                    
                    hOne = int(autoHours/10)
                    hTwo = int(autoHours%10)
                    mOne = int(autoMinutes/10)
                    mTwo = int(autoMinutes%10)
                    
                    displayTime(hOne, hTwo, mOne, mTwo)
                                        
            elif (desiredKey == 'B') :
                
                threeBs += 1
                print(threeBs)
                        
        iterations += 1
        
        if (iterations >= 250000) :
            iterations = 0
            autoSeconds += 1
            desiredKey = -1
        
        if (autoSeconds >= 60) :
            autoMinutes += 1
            autoSeconds = 00
            displayTime(hOne, hTwo, mOne, mTwo)
        elif (autoMinutes >= 60) :   
            autoHours += 1
            autoMinutes = 00   
        elif (autoHours >= 24) :   
            autoHours = 00
        
        #print("The Seconds are... ", autoSeconds)

''' '''
def checkhOne(hOne) :
    
    if (isALetter(hOne) == True) :
        
        return False
    
    else :
        
        hOne = int(hOne)
    
        if (hOne != 0 and hOne != 1 and hOne != 2) :
            
            return False
        
    return True


''' '''
def checkhTwo(hOne, hTwo) :
    
    if (hOne != 0 or hOne != 1 or hOne != 2) :
        
        if (hOne == 2 and hTwo >= 4) :
            
            return -1
            
    else :
    
        return -1

''' '''
def checkmOne(mOne) :
    
    if (mOne > 0 or mOne < 5) :
        
        return False
    
    return True


''' '''
def checkmTwo(mTwo) :
    
    if (mTwo > 0 or mTwo < 9) :
        
        return False
    
    return True


''' Checks if the Input is a Letter '''
def isALetter(stop) :
    
    # Calls the LED function to blink if an incorrect input was pressed
    
    if (stop == 'A'):
        return True
    elif (stop == 'B'):
        return True
    elif (stop == 'C'):
        return True
    elif (stop == 'D'):
        return True
    elif (stop == '*'):
        return True
    elif (stop == '#'):
        return True
    
    return False

def getFirstInput() :
    
    desiredKey = '-1'
    iterations = 0
    blink = True
    
    while True :
        
        desiredKey = lookForInput()

        if (desiredKey != -1) :

            if (checkhOne(desiredKey) == True) :
        
                return desiredKey
            
            else :
                
                return -1
            
        
        iterations += 1
        
        if (iterations >= 10000) :
            iterations = 0
            
            if (blink == True) :
                blink = False
                sevenSegFunc.displayOFF()
                    
                # Calls each clock to update to the Off Call
                clkCycle(1)

            else :
                blink = True
                sevenSegFunc.display0()
                
                clkCycle(1)
                
    sevenSegFunc.display0()
                
    clkCycle(1)

 
''' '''
def manualClock():
    
    isOn = True
    threeBs = 0
    iterations = 0
    desiredKey = -1
    
    currentFirst = -1
    currentSecond = '0'
    currentThird = '0'
    currentFourth = '0'
    
    sleep(1)
    
    while (currentFirst == -1) : 
    
        currentFirst = getFirstInput()
        print(currentFirst)
        
    wantToPrint(currentFirst)
    clkCycle(1)
    
    while True:
        
        iterations += 1
          
'''    
    manualHours = int(currentTimeArray[0])*10 + int(currentTimeArray[1])
    manualMinutes = int(currentTimeArray[4])*10 + int(currentTimeArray[5])
    manualSeconds = int(currentTimeArray[8])*10 + int(currentTimeArray[9])
    
    hOne = int(manualHours/10)
    hTwo = int(manualHours%10)
    mOne = int(manualMinutes/10)
    mTwo = int(manualMinutes%10)
    displayTime(hOne, hTwo, mOne, mTwo)

    while (threeBs < 3) :
        
        hOne = int(manualHours/10)
        hTwo = int(manualHours%10)
        mOne = int(manualMinutes/10)
        mTwo = int(manualMinutes%10)
        
        if (desiredKey == -1) :
            
            desiredKey = lookForInput()
        
            if (desiredKey == '#') :
                
                threeBs = 0
                
                if (isOn == True) :
                    # Sets the Display State to Off
                    isOn = False
                    
                    # Calls the Display to turn every segment Off
                    sevenSegFunc.displayOFF()
                    
                    # Calls each clock to update to the Off Call
                    clkCycle(1)
                    clkCycle(2)
                    clkCycle(3)
                    clkCycle(4)
                    
                else :
                    # Sets the Display State to Back On
                    isOn = True
                    
                    hOne = int(manualHours/10)
                    hTwo = int(manualHours%10)
                    mOne = int(manualMinutes/10)
                    mTwo = int(manualMinutes%10)
                    
                    displayTime(hOne, hTwo, mOne, mTwo)
                                        
            elif (desiredKey == 'B') :
                
                threeBs += 1
                print(threeBs)
                        
        iterations += 1
        
        if (iterations >= 250000) :
            iterations = 0
            manualSeconds += 1
            desiredKey = -1
        
        if (manualSeconds >= 60) :
            manualMinutes += 1
            manualSeconds = 00
            displayTime(hOne, hTwo, mOne, mTwo)
        elif (manualMinutes >= 60) :   
            manualHours += 1
            manualMinutes = 00   
        elif (manualHours >= 24) :   
            manualHours = 00
        
        #print("The Seconds are... ", autoSeconds)
'''        
        
''' Main Function '''
def main() :
    
    # Initialize Variables for Ease of Use
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
    acON = True
    manON = False
    
    # Wipe the Clock Clean, Set to All 0's and No DP
    blankClock()
    
    
    
    currentTimeArray = list(getTime())
    
    autoHours = int(currentTimeArray[0])*10 + int(currentTimeArray[1])
    autoMinutes = int(currentTimeArray[4])*10 + int(currentTimeArray[5])
    autoSeconds = int(currentTimeArray[8])*10 + int(currentTimeArray[9])

    manualHours = 12
    manualMinutes = 34
    manualSeconds = 00
    
    #displayTime(currentTimeArray[0], currentTimeArray[1], currentTimeArray[4], currentTimeArray[5])
    
    ''' Main Loop for the Function '''
    while True :
                
        desiredKey = -1   
        sleep(.5)
        
        ''' Reads Input for the Keypad '''
        #while (desiredKey == -1) :
        desiredKey = lookForInput()
        
        ''' Controls the Automatic Clock '''
        if (acON == True and isOn == True) :
            
            print("The automatic clock is ticking!")
            hOne = int(autoHours/10)
            hTwo = int(autoHours%10)
            mOne = int(autoMinutes/10)
            mTwo = int(autoMinutes%10)
            
            displayTime(hOne, hTwo, mOne, mTwo)
            
        if (manON == True and isOn == True) :
            
            print("The manual clock is ticking!")
            hOne = int(manualHours/10)
            hTwo = int(manualHours%10)
            mOne = int(manualMinutes/10)
            mTwo = int(manualMinutes%10)
        
        ''' Deciphers the Returned Value '''
        if (desiredKey == '#') :
            
            ''' Turns the Keypad completely off/back on '''
            if (isOn == True) :
                # Sets the Display State to Off
                isOn = False
                
                # Calls the Display to turn every segment Off
                sevenSegFunc.displayOFF()
                
                # Calls each clock to update to the Off Call
                clkCycle(1)
                clkCycle(2)
                clkCycle(3)
                clkCycle(4)
            else :
                # Sets the Display State to Back On
                isOn = True
                
                if(acON == True) :
                    hOne = int(autoHours/10)
                    hTwo = int(autoHours%10)
                    mOne = int(autoMinutes/10)
                    mTwo = int(autoMinutes%10)
                    displayTime(hOne, hTwo, mOne, mTwo)
                elif(manON == True) :
                    # Returns the Display to what it had before being turned off
                    wantToPrint(currentFirst)
                    clkCycle(1)
                    wantToPrint(currentSecond)
                    clkCycle(2)
                    wantToPrint(currentThird)
                    clkCycle(3)
                    wantToPrint(currentFourth)
                    clkCycle(4)
            
            
        elif (desiredKey == '*') :
                # Turns on the decimal point indefinitely
                decimalPoint = True
                
                # Updates the Second Seven Segment Display
                sevenSegFunc.displayDP(decimalPoint)
                wantToPrint(currentSecond) # Prints the Desired Character and stores it in the currentKey spot
                sevenSegFunc.clkCycle(2)
                
        elif (manON == True) :
            ''' Updates the LED Display Based on the User Input '''
            if (isOn == True):
            
                blink = False
                sevenSegFunc.displayDP(decimalPoint) # Displays the decimal point if it is supposed to be on screen, will need a clock call here so that it updates
                                
                if (cycleNum == 1) :
                    currentFirst = wantToPrint(desiredKey) # Prints the Desired Character and stores it in the currentKey spot
                elif (cycleNum == 2) :
                    currentSecond = wantToPrint(desiredKey) # Prints the Desired Character and stores it in the currentKey spot
                elif (cycleNum == 3) :
                    currentThird = wantToPrint(desiredKey) # Prints the Desired Character and stores it in the currentKey spot
                elif (cycleNum == 4) :
                    currentFourth = wantToPrint(desiredKey) # Prints the Desired Character and stores it in the currentKey spot
                               
                sevenSegFunc.clkCycle(cycleNum) # Calls the Clock Cycle for the Corresponding LED Display
                    
                # Changes the clock cycle
                if (cycleNum == 4) :
                    cycleNum = 1
                    checkClock = True
                else :
                    cycleNum += 1
        sleep(.5)
        
        autoSeconds += 1
        manualSeconds += 1
        iterations += 1
        
        if (autoSeconds >= 60) :
            autoMinutes += 1
            autoSeconds = 00
        elif (autoMinutes >= 60) :   
            autoHours += 1
            autoMinutes = 00   
        elif (autoHours >= 24) :   
            autoHours = 00
            
        if (manualSeconds >= 60) :   
            manualMinutes += 1
            manualSeconds = 00   
        elif (manualMinutes >= 60) :      
            manualHours += 1
            manualMinutes = 00       
        elif (manualHours >= 24) :  
            manualHours = 00

        print("The Seconds are... ", autoSeconds)
        print("The current Iteration is... ", iterations)
    
def start() :
    
    blankClock()
    desiredKey = lookForInput()
    
    if (desiredKey == 'A') :
            
        automaticClock()
        sleep(1)
            
    elif (desiredKey == 'B') :
            
        manualClock()
    
# Calls the Function
while True:
    start()
    #runManualClock('1', '1', '3', '4')
    #autoClock()
    

GPIO.cleanup()

 