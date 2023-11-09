# Imports
import RPi.GPIO as GPIO
from time import sleep
import time

# Declare the Pinout
morseInput     = 12
ledAudioOutput = 21
audioPin       = 17
ledPin         = 4

# Set the Mode of the Input Pin
GPIO.setmode(GPIO.BCM)

# Setup the Pins
GPIO.setup(morseInput, GPIO.IN)
GPIO.setup(ledAudioOutput, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(audioPin, GPIO.OUT, initial=GPIO.LOW)

'''Setup the Output Pins and Start them at low'''
GPIO.setup(audioPin,  GPIO.OUT)
GPIO.setup(ledPin,  GPIO.OUT, initial=GPIO.LOW)
speaker = GPIO.PWM(audioPin, 1200) # Set the Speaker as a PWM

''' Letter to Morse Dictionary '''
# Author: Daniel Covaci
lettertomorse_code_dict ={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                          'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                          'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                          'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                          'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                          'Z': '--..'}

''' Turns the LED and Sound On '''
# Author: Austin Iversen
def LEDSoundOn ():
    
    GPIO.output(ledPin, GPIO.HIGH)
    speaker.start(50)

    return


''' Turns the LED and Sound Off '''
# Author: Austin Iversen
def LEDSoundOff() :
    
    GPIO.output(ledPin, GPIO.LOW)
    speaker.stop()
    

''' Function for converting '''
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in lettertomorse_code_dict:
            morse_code.append(lettertomorse_code_dict[char])
    return ' '.join(morse_code)


''' Morse to Letter Dictionary '''
# Author: Daniel Covaci
morsetoletter_code_dict ={'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
                         '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
                         '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
                         '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                         '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
                         '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                         '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                         '-----': '0', '-.-.- .-.': 'over'}


''' Function for Converting '''
# Authors: Samuel Brewster and Daniel Covaci
def transToMorse (message) :
    
    # Declare Variables
    x = 0
    size = 1
    output = ""
    
    # Checks for over
    if (message == ".-.-. -.-") :
        
        writeOver() # Calls the Write Over Function
        return 10
    
    # Finds the Number of Letters in the Word
    while (x < len(message)) :
    
        if (message[x] == " ") :
            
            size += 1
            
        x += 1
        
    # Creates an Array for the Number of Letters
    englishText = [""] * size
    size2 = 0
    x = 0
    
    # Makes a String of Each Morse Letter
    while (x < len(message)) :
        
        # If it isn't a space, then it adds it to the array index
        if (message[x] != " ") :
            
            englishText[size2] += message[x]
            
        elif (message[x] == " ") :
            
            size2 += 1 # increments the array index
            
        x += 1
    
    y = 0
    
    # Reads through the array and adds it to an output string
    while (y < size) :
        
        # Redundant Code
        if (y == 0) :
            output += morsetoletter_code_dict.get(englishText[y], '?')
        elif (y >= 1) :
            output += morsetoletter_code_dict.get(englishText[y], '?')
        y += 1
        
    # Writes to the output file
    writeToFile(output)
    writeToFile('\n')
        
    return output
   
   
            
''' Finds the Length of a Morse Code Unit By Having the User Sign Attention '''
# Author: Samuel Brewster
def callAttention () :
    
    # Initialize Variables
    loop      = True
    timeStart = 0
    timeStop  = 0
    increment = 0
    noPress   = True
    
    # Main Loop
    while (loop == True) :
        
        # Switches between searching for a high and low edge
        if (GPIO.input(morseInput) == 1 and noPress == True) :
        
            noPress = False     # Switch to look for negative
            increment += 1      # Increment Edge Counter
            
            LEDSoundOn()
            
            # Takes the first time that the user pushes a button
            if (increment == 1) : 
                
                timeStart = time.time()
                
            # Finds out if its a Dot or Dash
            if ((increment % 2) == 0) :
                
                print('.', end="")
            
            else :
                
                print('-', end="")
            
        elif (GPIO.input(morseInput) == 0 and noPress == False) :
            
            noPress = True     # Switch to look for positive
            LEDSoundOff()
            
            # Exits when the user has pushed the button 5 times
            if (increment == 5) :
                
                timeStop = time.time()
                loop = False
            
        sleep(.1) # Debounce

    print("") # Prints a new line character
    
    # Calculate the Final Time
    finalTime = (timeStop - timeStart)
    finalTime = int(finalTime)
    finalTime = finalTime/15
    
    # Prints to tell the User the Time
    print(finalTime)
    
    # Returns the Average Time
    return finalTime        


''' Writes Attention to the File '''
# Author: Isaac Ramirez :)
def writeAttention () :

    print("- . - . - | attention ")
    
    output = open('/home/group-11/morseDecoder/mcdecode.txt', 'a')
    output.write("-.-.- | attention")
    output.close()


''' Function that monitors the GPIO pin connected to the telegraph key and returns the duration of the press '''
# Author: Samuel Brewster
def findDuration() :
    
    # Declare and Initialize
    noPress   = True
    loop      = True
    timeStart = 0
    timeStop  = 0
    
    # Loops until a high is found
    while (loop == True) :
        
        # Enters the loop when a high is found, then once it is gone it finds the time
        if (GPIO.input(morseInput) == 1 and noPress == True) :
        
            noPress = False         # Helps enter the exit part of the loop
            timeStart = time.time() # Starts timing
            LEDSoundOn()            # Turns the Speaker and LED on
            
        elif (GPIO.input(morseInput) == 0 and noPress == False) :
            
            loop = False            # Helps break the main loop
            timeStop = time.time()  # Stops timing so it can return the time held down
            LEDSoundOff()           # Turns the Speaker and LED off
            
        sleep(.1)
    
    return (timeStop - timeStart)


''' Converts User Input into Dots and Dashes '''
# Author: Daniel Corvaci
def printDotDashSpace(durationUserGave, oneUnitLength) :
    
    if (int(durationUserGave) <= int(oneUnitLength)) :
        
        print(".")


''' The Main Loop Used for Runtime '''
# Authors: Samuel Brewster and Daniel Corvaci
def runTime (userDuration, letter) :
    
    # Declare and Initialize
    noPress   = True
    loop      = True
    timeStart = 0
    timeStop  = 0
    
    timeStart = time.time() # Starts the timer
    
    # Loop while waiting for user input
    while (loop == True) :
        
        if (GPIO.input(morseInput) == 1 and noPress == True) :
            
            noPress = False # Helps break into while loop
            
        # Used to find the time of the user input
        while (GPIO.input(morseInput) == 1 and noPress == False) :
              
            # Stops the time and finds the duration of the user press
            timeStop = time.time()
            changeInTime = timeStop - timeStart
            durationPress = findDuration()
            
            loop = False
            
            # elifs to find the duration of the change in time
            if (changeInTime <= 1.5* userDuration and letter != "") :
                
                print(" ", end="")
                
            elif (changeInTime > 1.5 * userDuration and letter != "") :
                
                # Returns a space to the file and the output
                print("   ", end="")
                letter += " "
                writeToFile(" ")
            
            # elifs to find what to print for the user duration
            if (durationPress <= 1.5 * userDuration) :
                
                # Returns a . to the file and the output
                print(".", end="")
                letter += "."
                writeToFile(".")
                return letter
                
            elif (durationPress > 1.5 * userDuration) :
                
                # Returns a - to the file and the output
                print("-", end="")
                letter += "-"
                writeToFile("-")
                return letter
         
        # Knows if it is the end time for a line if it isnt empty        
        if (((time.time() - timeStart) > 7 * userDuration) and letter != "") :
                
            # Returns word done to let the program to know the word is over
            print(" | ", end="")
            writeToFile(" | ")
            return "word done"       
    
    return letter


''' Prompts the User to Sign Attention '''
# Author: Samuel Brewster
def printToUser () :
    
    print("Please Enter Attention (-.-.-) via the Morse Code Tapper: ", end="")
    
    
''' Function to Write to a File '''
# Author: Austin Iversen :)
def writeToFile (thing) :

    # Opens a File and Outputs the Argmument
    output = open('/home/group-11/morseDecoder/mcdecode.txt', 'a')
    output.write(thing)
    output.close()
    
    
''' Writes Over to the Output and a File '''
# Author: Isaac Ramirez :)
def writeOver () :

    print(".-.-. -.- | over ")
    
    # Opens a File and Outputs "over"
    output = open('/home/group-11/morseDecoder/mcdecode.txt', 'a')
    output.write("over")
    output.close()
            

''' Main Loop '''
# Author: Samuel Brewster
def main () :
    
    # Declare and Intialize
    endLine = False
    letter = ""
    unitLength = callAttention() # Calls the User to Sign Attention
    #unitLength = .3
    
    writeAttention()             # Writes attention to the screen
    writeToFile('\n')
    
    # Loops To Continually Get User Input
    while True: 
    
        # Checks if there has been an input, if so runs until line end
        if (letter == "") :
            
            result = runTime(unitLength, letter)
            letter = result
            
        else :
            
            result = runTime(unitLength, letter)
            
            # Checks if the line has ended, else, add to the word
            if (result == "word done") :
            
                print(transToMorse(letter))
                letter = ""
            
            else :
                
                letter = result
            
    
try:
    
    main()
    GPIO.cleanup()
    
finally:
    
    GPIO.cleanup()
