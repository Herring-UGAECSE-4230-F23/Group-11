#Imports
import RPi.GPIO as GPIO
from time import sleep
import time

morseInput = 12
ledAudioOutput = 21

# Set the Mode of the Input Pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(morseInput, GPIO.IN)

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

#List, dictionary, or class for convertng letters into their corresponding morse code.
lettertomorse_code_dict ={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

''' Function for converting '''
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in lettertomorse_code_dict:
            morse_code.append(lettertomorse_code_dict[char])
    return ' '.join(morse_code)


#List, dictionary, or class for converting morse code to their corresponding letter.
# Author: Daniel Covaci
orsetoletter_code_dict ={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                         '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                         '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                         '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                         '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                         '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                         '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                         '-----': '0', '-.-.- .-.': 'Over'}


''' Function for converting '''
# Author: Daniel Covaci
def transToMorse (message) :
             
    return (morsetoletter_code_dict.get(message, '?'))
            
''' Finds the Length of a Morse Code Unit By Having the User Sign Attention '''
def findMorseLength () :
    
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
            
            # Takes the first time that the user pushes a button
            if (increment == 1) : 
                
                timeStart = time.time()
                
            if ((increment % 2) == 0) :
                
                print('.', end="")
            
            else :
                
                print('-', end="")
                
                
            # Testing print
            #print(increment)
            
        elif (GPIO.input(morseInput) == 0 and noPress == False) :
            
            noPress = True     # Switch to look for positive
            
            # Exits when the user has pushed the button 5 times
            if (increment == 5) :
                
                timeStop = time.time()
                loop = False
                
            # Testing Print
            
        sleep(.1) # Debounce

    print("")
    
    # Calculate the Final Time
    finalTime = (timeStop - timeStart)
    finalTime = int(finalTime)
    finalTime = finalTime/15
    
    # Print for Testing
    print(finalTime)
    
    # Returns the Average Time
    return finalTime        


''' Function that monitors the GPIO pin connected to the telegraph key and returns the duration of the press '''
# Author: Sam Brewster
def findDuration() :
    
    noPress   = True
    loop      = True
    timeStart = 0
    timeStop  = 0
    
    while (loop == True) :
        
        if (GPIO.input(morseInput) == 1 and noPress == True) :
        
            noPress = False
            timeStart = time.time()
            #print(timeStart)
        elif (GPIO.input(morseInput) == 0 and noPress == False) :
            
            loop = False
            timeStop = time.time()
            
        sleep(.1)
    
    #print(timeStop - timeStart)
    
    return (timeStop - timeStart)


''' Converts User Input into Dots and Dashes '''
# Author: Daniel Corvaci
def printDotDashSpace(durationUserGave, oneUnitLength) :
    
    if (int(durationUserGave) <= int(oneUnitLength)) :
        
        print(".")
        
def playtone():
    GPIO.setup(morseInput, GPIO.OUT)
    
    try:
        while True:
           GPIO.wait_for_edge(morseInput, GPIO.RISING)
           GPIO.output(morseInput, GPIO.HIGH)
           time.sleep(.5)
           GPIO.output(morseInput, GPIO.LOW)


def runTime (userDuration, word) :
    
    noPress   = True
    loop      = True
    timeStart = 0
    timeStop  = 0
    
    timeStart = time.time()
    
    while (loop == True) :
        
        if (GPIO.input(morseInput) == 1 and noPress == True) :
            
            noPress = False
            
            #print(timeStart)
        while (GPIO.input(morseInput) == 1 and noPress == False) :
              
            timeStop = time.time()
            changeInTime = timeStop - timeStart
            durationPress = findDuration()
            
            #print(changeInTime)
            loop = False
            
            if (changeInTime <= 2* userDuration) :
                
                print(" ", end="")
                
            elif (changeInTime > 2 * userDuration) :
                
                print("   ", end="")
            
            
            if (durationPress <= 2 * userDuration) :
                
                print(".", end="")
                word += "."
                
            elif (durationPress > 2 * userDuration) :
                
                print("-", end="")
                word += "-"
         
        if (((time.time() - timeStart) > 7 * userDuration) and word != "") :
                
                print(" | ")
        
                return "done"
         
                
    
    return word

''' Prompts the User to Sign Attention '''    
def printToUser () :
    
    print("Please Enter Attention (-.-.-) via the Morse Code Tapper: ", end="")

''' Main Loop '''
def main () :
    
    endLine = False
    word = ""
    #unitLength = findMorseLength()
    unitLength = 1
    
    while True: 
    
        if (word == "") :
            
            result = runTime(unitLength, word)
            word = result
            
        else :
            
            result = runTime(unitLength, word)
            
            if (result == "done") :
            
                print("the user wants: ", end="")
                print(transToMorse(word))
                word = ""
            
            else :
                
                word = result
            
    #printToUser()
    
try:
    
    main()
    
finally:
    
    GPIO.cleanup()
