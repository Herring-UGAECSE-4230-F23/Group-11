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
def LEDSoundOn (time):
    
    GPIO.output(17,GPIO.HIGH)
    speaker.start(50)
 
    sleep(time)

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
  
# Author: Austin Iverson
morseCodeLibrary={
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G':'--.','H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N':'-.', 'O':'---', 'P': ' .--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U':'..-','V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
    
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
        cleaned_line = line.strip()
        Morse_Line=''.join([morseCodeLibrary.get(char.upper(),char)for char in line])
        Morse_Lines.append(Morse_Line)
        
    return Morse_Lines

''' '''
#Author: Sam Brewster
def makeMorseList(filePath):
    
    with open(filePath) as file:
        lines = file.readlines()
        
    Morse_Lines = []
    loops = 0
    
    while (loops < len(lines)) :
        Morse_Lines = lines[loops]
        print(Morse_Lines[loops])
        loops = loops + 1
        
    print(Morse_Lines)
    

''' Prints the Morse Code to The Output '''
# Author: Sam Brewster
def printMorseCode(Morse_Lines) :
    
    iteration = 0
    print(len(Morse_Lines))
    
    while (iteration < len(Morse_Lines)) :
        
        currentString = Morse_Lines[iteration]
        curStringLength = len(currentString)
        incrementor = 0
        currentMorseWord = ""
        doNothing = 0
        
        while (curStringLength > incrementor) :
            
            if (currentString[incrementor] == '.') :
                
                currentMorseWord += "."
                LEDSoundOn(2)
                
            elif (currentString[incrementor] == '-') :
                
                currentMorseWord += "-"
                LEDSoundOn(4)
            
            elif (currentString[incrementor] == ' ') :
                
                print(currentMorseWord + printMorseWord(iteration))
                currentMorseWord = ""
                
            elif (currentString[incrementor] == '\n') :
                
                print(currentMorseWord + printMorseWord(iteration))
                currentMorseWord = ""

            incrementor += 1
            LEDSoundOff()
            sleep(2)

        #print(currentMorseWord + printMorseWord(iteration))
        iteration = iteration + 1
        
    return
        

''' Prints the Word that the Morse Code Is '''
# Author: Sam Brewster
def printMorseWord(lineNumber) :
    
    with open('/home/group-11/Desktop/mcencode.txt') as file:
        lines = file.readlines()
        
        return(" | " + lines[lineNumber])
        

filePath = '/home/group-11/Desktop/mcencode.txt'
#print(Text_Morse('/home/group-11/Desktop/mcencode.txt'))
#OpenTextFile()
#printMorseWord(1)
printMorseCode(Text_Morse('/home/group-11/Desktop/mcencode.txt'))
makeMorseList(filePath)
#LEDSound()
