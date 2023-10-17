import RPi.GPIO as GPIO
from time import sleep
#import simpleaudio
import numpy

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

'''Setup the Output Pins and Start them at low'''
GPIO.setup(4,  GPIO.OUT)
GPIO.setup(17,  GPIO.OUT, initial=GPIO.LOW)
speaker = GPIO.PWM(4, 1200)


''' Turns the LED and Sound On '''
# Author: Austin Iverson
def LEDSound ():
    
    GPIO.output(17,GPIO.HIGH)
    speaker.start(50)

    return


''' Turns the LED and Sound Off '''
# Author: Sam Brewster
def LEDSoundOff() :
    
    GPIO.output(17, GPIO.LOW)
    speaker.stop()

''' Opens a Text File '''
# Author: Sam Brewster
def OpenTextFile() :
    
    file = open('/home/group-11/Desktop/mcencode.txt')
    lines = file.readlines()
    
    for line in lines:
        cleaned_line = line.strip('\n')
        print(cleaned_line)
  
morseCodeLibrary={
    'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G':'--. ','H': '.... ',
    'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N':'-. ', 'O':'--- ', 'P': ' .--. ',
    'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ', 'U':'..- ','V': '...- ', 'W': '.-- ', 'X': '-..- ',
    'Y': '-.-- ', 'Z': '--.. '
    
    'a' '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g':'--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--','n':'-.', 'o':'--- ', 'p': ' .--.',
    'q': '--.-', 'r': '.-.', 's': '... ', 't': '-', 'u':'..-','v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
}

''' Takes the Letters Out of a File and Outputs '''
# Author: Austin Iverson
def Text_Morse(filePath):
    with open(filePath) as file:
        lines = file.readlines()
    
    Morse_Lines = []
    for line in lines:
        cleaned_line = line.strip('\n')
        Morse_Line=''.join([morseCodeLibrary.get(char.upper(),char)for char in line])
        Morse_Lines.append(Morse_Line)
        
    return Morse_Lines


        
print(Text_Morse('/home/group-11/Desktop/mcencode.txt'))
OpenTextFile()
#LEDSound()
