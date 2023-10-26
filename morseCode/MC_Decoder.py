#Imports
import RPi.GPIO as GPIO
from time import sleep

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


#Function that monitors the GPIO pin connected to the telegraph key and returns the duration of the press


#Function that take lenght of key press as an input and returns its corresponding unit (dot, dash, or space)


#Function to determine the average dot and dash lenght by having the user sign attention
# This function determines the length of a unit because the user will input -.-.-, which will give us 
def determineLength () :
    
    # This function waits for the user to input -.-.- on the keyboard.
    # This will calculate the average length of a 'unit' by timing

#Function to pay a tone through the speaker anytime the telegraph key is pressed


#The interrupt that triggers the ey press length function anytime the GPIO connected t the telegraph is ky enters the high state.


#Parts 10, 11, and 12