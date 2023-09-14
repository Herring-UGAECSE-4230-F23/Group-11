# Group 11's Keypad
#
# Created 6SEP2023
# Blessed with the mentorship of Dr. Herring
# Property of Samuel, Isaac, Austin, and Daniel

# Imports
import RPi.GPIO as GPIO
from time import sleep

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
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)

'''Initialize the Variables'''
# Choices of the Keypad
one   = [1, 2, 3, 'A']
two   = [4, 5, 6, 'B']
three = [7, 8, 9, 'C']
four  = ['*', '0', '#', 'D']

# Variable to stop loop
stop = 0

'''Function Called to Read a High GPIO Input from the Pi'''
def readKeyPad(rowNum, char):
    
    # The variable for the users Y Value
    curVal = 0
    
    # Sends a High to the Keypad to check for a High input in return
    GPIO.output(rowNum, GPIO.HIGH)
    
    # Deciphers what Y Input is received and returns value to user
    if GPIO.input(23) == 1:
        curVal = char[0]
    if GPIO.input(24) == 1:
        curVal = char[1]
    if GPIO.input(25) == 1:
        curVal = char[2]
    if GPIO.input(5) == 1:
        curVal = char[3]
    
    # Kills the High input
    GPIO.output(rowNum, GPIO.LOW)
    
    return curVal

'''Loop to Interact with the User'''
while stop == 0:
    
    # Continuously calls the function with differing X Values until something is returned
    stop = readKeyPad(4, one)
    if stop != 0:
        break
    stop = readKeyPad(17, two)
    if stop != 0:
        break
    stop = readKeyPad(27, three)
    if stop != 0:
        break
    stop = readKeyPad(22, four)
    if stop != 0:
        break
 
# Prints the chosen value
print("You want to print", stop)
GPIO.output(12, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)


GPIO.cleanup()
