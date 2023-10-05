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
    delayPersonal()                   # Waits
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
    
    # Calls each number to be output then calls its corresponding clock to update it
    
    wantToPrint(hOne)
    clkCycle(1)
    wantToPrint(hTwo)
    clkCycle(2)
    wantToPrint(mOne)
    clkCycle(3)
    wantToPrint(mTwo)
    clkCycle(4)
 
''' Gets the Current Time and Returns it as a String '''
def getTime() :
    
    now = datetime.now()
    
    currentTime = now.strftime("%H: %M: %S")
    
    return currentTime
    
''' Does the automatic Clock '''    
def automaticClock() :

    # Variable Declaration
    PM = False
    isOn = True
    threeBs = 0
    iterations = 0
    buttonReset = 0
    desiredKey = -1
    
    # Initialize
    currentFirst = '0'
    currentSecond = '0'
    currentThird = '0'
    currentFourth = '0'
    
    # Gets the current time on the pi
    currentTimeArray = list(getTime())
    
    # Deciphers the Hours, Minutes, and Seconds from the currentTime String
    autoHours = int(currentTimeArray[0])*10 + int(currentTimeArray[1])
    autoMinutes = int(currentTimeArray[4])*10 + int(currentTimeArray[5])
    autoSeconds = int(currentTimeArray[8])*10 + int(currentTimeArray[9])
    
    # Makes the current time into an int for each place
    hOne = int(autoHours/10)
    hTwo = int(autoHours%10)
    mOne = int(autoMinutes/10)
    mTwo = int(autoMinutes%10)
    
    # Checks if it is AM or PM
    PM = adjustToCivilian(str(hOne), str(hTwo))
    # Calls to output the civilian version of the given military time
    displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)

    # Main While Loop, Checks if B has been hit three times
    while (threeBs < 3) :
        
        # Makes the current time into an int for each place
        hOne = int(autoHours/10)
        hTwo = int(autoHours%10)
        mOne = int(autoMinutes/10)
        mTwo = int(autoMinutes%10)
        
        # Checks if the button is ready for the next input
        if (desiredKey == -1) :
            
            # Looks for the next user button input
            desiredKey = lookForInput()
        
            # Turns the SSD on or off
            if (desiredKey == '#') :
                
                threeBs = 0 # resets the counter to see if three bs have been input
                
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
                    
                    # Makes the current time into an int for each place
                    hOne = int(autoHours/10)
                    hTwo = int(autoHours%10)
                    mOne = int(autoMinutes/10)
                    mTwo = int(autoMinutes%10)
                    
                    # Checks if it is AM or PM
                    PM = adjustToCivilian(str(hOne), str(hTwo))
                    # Calls to output the civilian version of the given military time
                    displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)
             
            # Increments the counter if three bs are pressed
            elif (desiredKey == 'B') :
                
                threeBs += 1
                print(threeBs)
          
        # How our delay loop works
        iterations += 1 # Increases the counter for each time the loop runs
        buttonReset += 1
        
        # Delay for One Second
        if (iterations >= 60000) :
            iterations = 0 # Resets the Counter
            autoSeconds += 1 # Increments the second counter
            print(autoSeconds, " seconds")
            
        # Logic so there is no bouncing
        if (buttonReset >= (3*60000)) :
            desiredKey = -1 # Allows for another button input
            buttonReset = 0 # Resets the button counter
        
        # Logic for incrementing a minute
        if (autoSeconds >= 60) :
            autoMinutes += 1 # increments time
            autoSeconds = 00 # resets seconds
            
            # Prepares to print by checking AM vs PM and printing if on
            PM = adjustToCivilian(str(hOne), str(hTwo))
            if (isOn == True) :
                displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)
                
        # Logic for incrementing an hour
        if (autoMinutes >= 60) :   
            autoHours += 1 # increments time
            autoMinutes = 00 # resets minutes
            
            # prepares for printing
            hOne = int(autoHours/10)
            hTwo = int(autoHours%10)
            mOne = int(autoMinutes/10)
            mTwo = int(autoMinutes%10)
            PM = adjustToCivilian(str(hOne), str(hTwo))
            if (isOn == True) :
                displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)
        
        # Logic for resetting
        if (autoHours >= 24) :   
            autoHours = 00 # resets time
            # Prepares for print
            hOne = int(autoHours/10)
            hTwo = int(autoHours%10)
            mOne = int(autoMinutes/10)
            mTwo = int(autoMinutes%10)
            PM = adjustToCivilian(str(hOne), str(hTwo))
            if (isOn == True) :
                displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)

''' Checks that the First Hour is a Legal Input '''
def checkhOne(hOne) :
    
    if (isALetter(hOne) == True) :
        
        return False # Returns False if not a number
    
    else :
        
        hOne = int(hOne) # Typecasts to an int
    
        if (hOne != 0 and hOne != 1 and hOne != 2) :
            
            return False # returns False if too big a number
        
    return True # returns True if a legal input


''' Checks that the Second Hour is a Legal Input '''
def checkhTwo(hOne, hTwo) :
    
    if (isALetter(hTwo) == True) :
        
        return False # Returns False if not a number
    
    else :
            
        if (hOne == '2' and (hTwo != '0' and hTwo != '1' and hTwo != '2' and hTwo != '3')) :
                
            return False # returns False if it is above 23 hours
                
    return True # returns True if a legal input

''' Checks that the First Minute is a Legal Input '''
def checkmOne(mOne) :
    
    if (isALetter(mOne) == True) :
        
        return False # Returns false if it is a letter
    
    else :
        
        mOne = int(mOne) # typecasts to an int
        
        if (mOne < 0 or mOne > 5) :
            
            return False # Returns false if it is not a number 0-5
    
    return True # Returns true if it is a legal input


''' Checks that the Second Minute is a Legal Input '''
def checkmTwo(mTwo) :
     
    if (isALetter(mTwo) == True) :
        
        return False # Returns false if it is a letter
    
    else :
        
        mTwo = int(mTwo) # typecasts to an int
        
        if (mTwo < 0 or mTwo > 9) :
            
            return False # Returns false if it is not a number 0-5
    
    return True # Returns true if it is a legal input


''' Checks if the Input is a Letter '''
def isALetter(stop) :
    
    # Checks if the input is a letter, returns false if it is not
    
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

''' Gets the input of the first manual digit '''
def getFirstInput() :
    
    # Declare and Initialize
    desiredKey = '-1'
    iterations = 0
    blink = True
    
    # Loops until something is returned
    while True :
        
        desiredKey = lookForInput() # Asks for user input

        # Checks if the user has input a button
        if (desiredKey != -1) :
            
            # If the button is legal, delay for a second and go to the next digit
            if (checkhOne(desiredKey) == True) :
        
                delayPersonal()
                return desiredKey
            
            else :
                GPIO.output(18, GPIO.HIGH) # LED ON for illegal inputs
                return -1
            
        # Counts the loops in order to time it
        iterations += 1
        
        # The loop count for a blink
        if (iterations >= 10000) :
            iterations = 0
            
            # Toggles the blinking LED
            if (blink == True) :
                blink = False
                sevenSegFunc.displayOFF()
                    
                # Calls each clock to update to the Off Call
                clkCycle(1)

            else :
                blink = True
                sevenSegFunc.display0()
                
                # Calls a clokc to update to the On Call
                clkCycle(1)
    
    # Ensures the digit goes back to 0
    sevenSegFunc.display0()
                
    clkCycle(1)

''' Gets the User's Second Input '''
def getSecondInput(currentFirst) :
    
    # Declare and Initialize
    desiredKey = '-1'
    iterations = 0
    blink = True
    
    # Main Loop
    while True :
        
        # Ask for user input
        desiredKey = lookForInput()

        # Looks for a user press
        if (desiredKey != -1) :

            # Checks if it is a legal button
            if (checkhTwo(currentFirst, desiredKey) == True) :
        
                # Sleep 1 second and return the press
                delayPersonal()
                return desiredKey
            
            else :
                GPIO.output(18, GPIO.HIGH) # LED on, illegal press
                return -1
            
        # counter for our blink method
        iterations += 1
        
        # Checks how many times the loop iterates to time it
        if (iterations >= 10000) :
            iterations = 0
            
            # toglles the blink on and off
            if (blink == True) :
                blink = False
                sevenSegFunc.displayOFF()
                    
                # Calls each clock to update to the Off Call
                clkCycle(2)

            else :
                blink = True
                sevenSegFunc.display0()
                
                # Calls each clock to update to the On Call
                clkCycle(2)
                
    # Ensures the screen has a 0
    sevenSegFunc.display0()
                
    clkCycle(2)
 
''' Gets the User's Third Input '''
def getThirdInput() :
    
    # Declare and Intialize
    desiredKey = '-1'
    iterations = 0
    blink = True
    
    # Main Loop
    while True :
        
        # Checks for user input
        desiredKey = lookForInput()

        # if it is a new press, enter loop
        if (desiredKey != -1) :

            # if it is a legal press
            if (checkmOne(desiredKey) == True) :
        
                # sleep and return the legal input
                delayPersonal()
                return desiredKey
            
            else :
                GPIO.output(18, GPIO.HIGH) # led on for illegal input
                return -1
            
        # counter for the iterations of our sleep method
        iterations += 1
        
        # counter for the blinking to toggle
        if (iterations >= 10000) :
            iterations = 0
            
            # toggles the blink on and off
            if (blink == True) :
                blink = False
                sevenSegFunc.displayOFF()
                    
                # Calls each clock to update to the Off Call
                clkCycle(3)

            else :
                blink = True
                sevenSegFunc.display0()
                
                # Calls each clock to update to the On Call
                clkCycle(3)
        
    # Ensures the screen has a 0
    sevenSegFunc.display0()
                
    clkCycle(3)
    
''' Gets the User's Third Input '''
def getFourthInput() :
    
    # Declare and Initialize
    desiredKey = '-1'
    iterations = 0
    blink = True
    
    # main loop
    while True :
        
        # checks for user input
        desiredKey = lookForInput()

        # if the user input is different, enter loop
        if (desiredKey != -1) :

            # checks if the user input is legal
            if (checkmTwo(desiredKey) == True) :
        
                # uses our delay method and returns the legal press
                delayPersonal() # prevents bouncing
                return desiredKey
            
            else :
                GPIO.output(18, GPIO.HIGH) # led for the illegal input
                return -1
            
        # counts for our loop iterations
        iterations += 1
        
        # logic for the blink to toggle
        if (iterations >= 10000) :
            iterations = 0
            
            # toggles the blink on and off
            if (blink == True) :
                blink = False
                sevenSegFunc.displayOFF()
                    
                # Calls each clock to update to the Off Call
                clkCycle(4)

            else :
                blink = True
                sevenSegFunc.display0()
                
                # Calls each clock to update to the Off Call
                clkCycle(4)
    
    # Ensures the screen has a 0
    sevenSegFunc.display0()
                
    clkCycle(4)

''' Checks if the Time needs to be Converted '''
def adjustToCivilian(one, two) :
        
    # Logical cases to see if the time is a PM number and needs to be converted to civilian time
        
    if (one == '0') :
        
        return False
    
    elif (one == '1' or one == '2') :
        
        if (one == '1' and (two != '1' and two != '2' and two != '0')) :
            
            return True
        
        elif (one == '2') :
            
            return True
        
    return False

''' Displays the time in civilian time when given military time '''
def displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM) :
    
    # Outputs the time if it is 1300 or later
    if (PM == True) :

        # converts hOne to civilian time
        if (hOne == 2) : 
            hOne = 0
            if (hTwo == 2 or hTwo == 3) : 
                hOne = 1
                print(hOne)
        else :
            
            hOne = 0
        # Converst hTwo to civilian time
        if (hTwo == 0) :
            hTwo = int(8)
        elif (hTwo == 1) :
            hTwo = int(9)
        else :
            hTwo = int(hTwo) - 2
        
        wantToPrint(hOne)
        clkCycle(1)
        wantToPrint(hTwo)
        sevenSegFunc.displayDP(True)
        clkCycle(2)
        wantToPrint(mOne)
        clkCycle(3)
        wantToPrint(mTwo)
        clkCycle(4)
        
    else :
        # outputs the normal time from 0000 - 1259
        wantToPrint(hOne)
        clkCycle(1)
        wantToPrint(hTwo)
        GPIO.output(16, GPIO.LOW) # LED
        clkCycle(2)
        wantToPrint(mOne)
        clkCycle(3)
        wantToPrint(mTwo)
        clkCycle(4)
        
''' The Main Function for the manual clock'''
def manualClock():
    
    # Declare and Intialize
    isOn = True
    PM = False
    threeBs = 0
    iterations = 0
    desiredKey = -1
    buttonReset = 0
    
    militaryFirst = -1
    militarySecond = -1
    currentFirst = -1
    currentSecond = -1
    currentThird = -1
    currentFourth = -1
    
    delayPersonal() # Prevents bouncing

    # Logic for a legal first input
    while (currentFirst == -1) : 
    
        currentFirst = getFirstInput() # Gets input from the user
        
    # Updates the screen
    wantToPrint(currentFirst)
    clkCycle(1)
    GPIO.output(18, GPIO.LOW) # LED off for legal input

    # Logic for a legal second input
    while (currentSecond == -1) : 
    
        currentSecond = getSecondInput(currentFirst) # Gets input from the user
        
    GPIO.output(18, GPIO.LOW) # LED off for legal input
    
    # Checks AM or PM
    if (adjustToCivilian(currentFirst, currentSecond) == True) :
        
        PM = True
        
    else :
        
        PM = False
     
    # Finds the military time and outputs the correct SSD
    if (PM == True) :
        if (currentFirst == '2') :
            
            militaryFirst = 0
            
            if (currentSecond == '2' or currentSecond == '3') :
                
                militaryFirst = 1
                
        else :
            
            militaryFirst = 0
        
        if (currentSecond == '0') :
            militarySecond = int(8)
        elif (currentSecond == '1') :
            militarySecond = int(9)
        else :
            militarySecond = int(currentSecond) - 2
        
        wantToPrint(militaryFirst)
        clkCycle(1)
        wantToPrint(militarySecond)
        sevenSegFunc.displayDP(True)
        clkCycle(2)
    else :
        wantToPrint(currentFirst)
        clkCycle(1)
        wantToPrint(currentSecond)
        clkCycle(2)
      
    GPIO.output(18, GPIO.LOW) # LED off for legal input
      
    # Logic for third legal input
    while (currentThird == -1) : 
    
        currentThird = getThirdInput() # loops until legal input
    
    # updates ssd
    GPIO.output(18, GPIO.LOW) # LED off for legal input
    wantToPrint(currentThird)
    clkCycle(3)
    
    # Logic for fourth legal input
    while (currentFourth == -1) : 
    
        currentFourth = getFourthInput() # loops until legal input
        
    # updates ssd
    wantToPrint(currentFourth)
    clkCycle(4)
    GPIO.output(18, GPIO.LOW) # LED off for legal input
          
    # initializes the counter time
    manualHours = int(currentFirst)*10 + int(currentSecond)
    manualMinutes = int(currentThird)*10 + int(currentFourth)
    manualSeconds = 00

    # main while loop, checks for the b button to be pressed three times
    while (threeBs < 3) :
        
        # converts the time into integers
        hOne = int(manualHours/10)
        hTwo = int(manualHours%10)
        mOne = int(manualMinutes/10)
        mTwo = int(manualMinutes%10)
        
        # checks for a user input if the button is ready for another press
        if (desiredKey == -1) :
            
            desiredKey = lookForInput() # asks for user input
        
            # Logic for iff the screen turns off
            if (desiredKey == '#') :
                
                # resets the three b presses
                threeBs = 0
                manualSeconds -= 8 # calibration
                
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
                    
                    # gets the int values of the current time
                    hOne = int(manualHours/10)
                    hTwo = int(manualHours%10)
                    mOne = int(manualMinutes/10)
                    mTwo = int(manualMinutes%10)
                    
                    # checks if AM or PM then outputs
                    PM = adjustToCivilian(str(hOne), str(hTwo))
                    displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)
                                        
            elif (desiredKey == 'B') :
                
                # increments by a b press
                threeBs += 1
                manualSeconds -= 8
                print(threeBs)
        
        # increments for our delay
        buttonReset += 1
        iterations += 1
        
        # enters the loop every one second
        if (iterations >= 60000) :
            iterations = 0 # resets
            manualSeconds += 1 # increments by a second
            print(manualSeconds, " seconds")

        # prevents bouncing by the button
        if (buttonReset >= (3*200000)) :
            desiredKey = -1 # resets, ready to read another button press
            buttonReset = 0
        
        # logic for a minute incrementing
        if (manualSeconds >= 60) :
            manualMinutes += 1
            manualSeconds = 00
            # updates the screen with usual code
            hOne = int(manualHours/10)
            hTwo = int(manualHours%10)
            mOne = int(manualMinutes/10)
            mTwo = int(manualMinutes%10)
            PM = adjustToCivilian(str(hOne), str(hTwo))
            if (isOn == True) :
                displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)
        elif (manualMinutes >= 60) :
            # increments for every hour
            manualHours += 1
            manualMinutes = 00 # resets
            # updates the screen with the usual code
            hOne = int(manualHours/10)
            hTwo = int(manualHours%10)
            mOne = int(manualMinutes/10)
            mTwo = int(manualMinutes%10)
            PM = adjustToCivilian(str(hOne), str(hTwo))
            if (isOn == True) :
                displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)
        elif (manualHours >= 24) :
            # resets when midnight is reached
            manualHours = 00
            # updates the screen with the usual code
            hOne = int(manualHours/10)
            hTwo = int(manualHours%10)
            mOne = int(manualMinutes/10)
            mTwo = int(manualMinutes%10)
            PM = adjustToCivilian(str(hOne), str(hTwo))
            if (isOn == True) :
                displayMilitaryTime(hOne, hTwo, mOne, mTwo, PM)
        
''' Our Version of Sleep '''
def delayPersonal () :
    
    counter = 0
    
    # Prints to slow the computer down about one second when operating
    while (counter < 600) :
        
        counter += 1
        print("Im waiting...")
        
    print("im done") # just to help see visually

''' Starts the Clock '''
def start() :
    
    # Erases the screen and asks for an input
    blankClock()
    desiredKey = lookForInput()
    
    # Logic for Automatic
    if (desiredKey == 'A') :
            
        automaticClock()
        delayPersonal() # prevents bouncing
     
    # Logic for Manual
    elif (desiredKey == 'B') :
            
        manualClock()
        delayPersonal() # prevents bouncing
    
''' Starts the Program '''
while True:
    start()
    
GPIO.cleanup()

 