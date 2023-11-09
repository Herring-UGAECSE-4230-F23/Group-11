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
morsetoletter_code_dict ={'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
                         '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
                         '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
                         '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                         '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
                         '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                         '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                         '-----': '0', '-.-.- .-.': 'over'}


''' Function for converting '''
# Author: Daniel Covaci
def transToMorse (message) :
    
    x = 0
    size = 1
    output = ""
    
    while (x < len(message)) :
    
        if (message[x] == " ") :
            
            size += 1
            
        x += 1
        
    englishText = [""] * size
    size2 = 0
    x = 0
    
    while (x < len(message)) :
        
        if (message[x] != " ") :
            
            englishText[size2] += message[x]
            
        elif (message[x] == " ") :
            
            size2 += 1
            
        x += 1
    
    y = 0
    while (y < size) :
        
        if (y == 0) :
            output += morsetoletter_code_dict.get(englishText[y], '?')
        elif (y >= 1) :
            output += morsetoletter_code_dict.get(englishText[y], '?')
        y += 1
        
    return output
   
   
            
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
    
    return (timeStop - timeStart)


''' Converts User Input into Dots and Dashes '''
# Author: Daniel Corvaci
def printDotDashSpace(durationUserGave, oneUnitLength) :
    
    if (int(durationUserGave) <= int(oneUnitLength)) :
        
        print(".")
        
def playtone():
    GPIO.setup(morseInput, GPIO.OUT)
    
    while True:
        GPIO.wait_for_edge(morseInput, GPIO.RISING)
        GPIO.output(morseInput, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(morseInput, GPIO.LOW)

''' '''
def runTime (userDuration, letter) :
    
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
            
            if (changeInTime <= 2* userDuration and letter != "") :
                
                print(" ", end="")
                
            elif (changeInTime > 2 * userDuration and letter != "") :
                
                print("   ", end="")
                letter += " "
            
            if (durationPress <= 2 * userDuration) :
                
                print(".", end="")
                letter += "."
                return letter
                
            elif (durationPress > 2 * userDuration) :
                
                print("-", end="")
                letter += "-"
                return letter
         
                
        if (((time.time() - timeStart) > 7 * userDuration) and letter != "") :
                
            print(" | ", end="")
        
            return "word done"       
    
    return letter


''' Prompts the User to Sign Attention '''    
def printToUser () :
    
    print("Please Enter Attention (-.-.-) via the Morse Code Tapper: ", end="")

''' Main Loop '''
def main () :
    
    endLine = False
    letter = ""
    #unitLength = findMorseLength()
    unitLength = .3
    
    while True: 
    
        if (letter == "") :
            
            result = runTime(unitLength, letter)
            letter = result
            
        else :
            
            result = runTime(unitLength, letter)
            
            if (result == "word done") :
            
                print(transToMorse(letter))
                letter = ""
            
            else :
                
                letter = result
            
    #printToUser()
    
try:
    
    main()
    
finally:
    
    GPIO.cleanup()
