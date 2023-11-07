#Imports
import RPi.GPIO as GPIO
from time import sleep
import time

morseInput = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(morseInput, GPIO.IN)

#List, dictionary, or class for convertng letters into their corresponding morse code.
lettertomorse_code_dict ={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

#Function for converting
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in lettertomorse_code_dict:
            morse_code.append(lettertomorse_code_dict[char])
    return ' '.join(morse_code)


#List, dictionary, or class for converting morse code to their corresponding letter.
morsetoletter_code_dict ={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

#Function for converting
def morse_to_text(text):
    morse_code = []
    for char in text.upper():
        if char in morsetoletter_code_dict:
            morse_code.append(morsetoletter_code_dict[char])
    return ' '.join(morse_code)


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
                
            # Testing print
            print(increment)
            
        elif (GPIO.input(morseInput) == 0 and noPress == False) :
            
            noPress = True     # Switch to look for positive
            
            # Exits when the user has pushed the button 5 times
            if (increment == 5) :
                
                timeStop = time.time()
                loop = False
                
            # Testing Print
            print(increment)
            
        sleep(.1) # Debounce

    # Calculate the Final Time
    finalTime = (timeStop - timeStart)
    finalTime = int(finalTime)
    finalTime = finalTime/5
    
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
    
    print(timeStop - timeStart)
    
    return timeStop


''' Converts User Input into Dots and Dashes '''
# Author: Daniel Corvaci
def printDotDashSpace(durationUserGave, oneUnitLength) :
    
    if (int(durationUserGave) == int(oneUnitLength)) :
        
        print(".")

'''
def danielFunc() :
    
    start_time = 0
    end_time = 0
    duration = 0
    
    while True:
        
        GPIO.WAIT(morseInput, GPIO.FALLING)
        start_time = time.time()
        GPIO.WAIT(morseInput, GPIO.RISING)
        end_time = time.time()
        duration = end_time - start_time
        print(duration)
'''     
#Function that take lenght of key press as an input and returns its corresponding unit (dot, dash, or space)


#Function to determine the average dot and dash lenght by having the user sign attention
# This function determines the length of a unit because the user will input -.-.-, which will give us 
    
    # This function waits for the user to input -.-.- on the keyboard.
    # This will calculate the average length of a 'unit' by timing

#Function to pay a tone through the speaker anytime the telegraph key is pressed


#The interrupt that triggers the ey press length function anytime the GPIO connected t the telegraph is ky enters the high state.


#Parts 10, 11, and 12
    
while True:
    #danielFunc()
    #findDuration()
    print(findLength())
    #print(GPIO.input(morseInput))
    #sleep(.01)
