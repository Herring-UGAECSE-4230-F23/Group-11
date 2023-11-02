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


''' Finds the Length of a Morse Code Unit '''
# Author: Sam Brewster
def findLength () :
    
    loop = True
    fallingEdge = 0
    
    while (loop == True) :
        
        if (GPIO.input(morseInput) == 1 and fallingEdge == 0) :
            
            startTime = time.time()
            
            while (GPIO.input(morseInput) == 1 and fallingEdge == 0) :
            
                if (GPIO.input(morseInput) == 0) :
                    
                    print(fallingEdge)
                    fallingEdge += 1
                    
                    sleep(.1)
                
        while (GPIO.input(morseInput) == 0) :
            
            while (GPIO.input(morseInput) == 1 and fallingEdge != 0) :
            
                if (GPIO.input(morseInput) == 0) :
                    
                    print(fallingEdge)
                    fallingEdge += 1
                    sleep(.1)
            
        if (fallingEdge >= 5) :
            
            loop = False
            endTime = time.time()
    
    return (endTime - startTime)/9


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
def monitorkey(lengthOfKeyPress):
    if lengthOfKeyPress >= attention and lengthOfKeyPress < (3 * attention):
        return 'dot'
    elif lengthOfKeyPress >= (3 * attention):
        return 'dash'

#Function to determine the average dot and dash lenght by having the user sign attention
# This function determines the length of a unit because the user will input -.-.-, which will give us 
    
    # This function waits for the user to input -.-.- on the keyboard.
    # This will calculate the average length of a 'unit' by timing

#Function to pay a tone through the speaker anytime the telegraph key is pressed
def playtone():
    GPIO.setup(morseInput, GPIO.OUT)
    
    try:
        while True:
           GPIO.wait_for_edge(morseInput, GPIO.RISING)
           GPIO.output(morseInput, GPIO.HIGH)
           time.sleep(.5)
           GPIO.output(morseInput, GPIO.LOW)

    finally:
        GPIO.cleanup()

#The interrupt that triggers the ey press length function anytime the GPIO connected t the telegraph is ky enters the high state.


#Parts 10, 11, and 12
    
while True:
    #danielFunc()
    #findDuration()
    print(findLength())
    #print(GPIO.input(morseInput))
    #sleep(.01)
