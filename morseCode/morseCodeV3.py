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
    #speaker.start(50)
 
    sleep(time)

    return


''' Turns the LED and Sound Off '''
# Author: Sam Brewster
def LEDSoundOff() :
    
    GPIO.output(17, GPIO.LOW)
    speaker.stop()

  
# Author: Austin Iverson
morseCodeLibrary={
    'A': '. -', 'B': '- . . .', 'C': '- . - .', 'D': '- . .', 'E': '.', 'F': '. . - .', 'G':'- - .','H': '. . . .',
    'I': '. .', 'J': '.- - -', 'K': '- . -', 'L': '. - . .', 'M': '- -', 'N':'- .', 'O':'- - -', 'P': ' . - - .',
    'Q': '- - . -', 'R': '. - .', 'S': '. . .', 'T': '-', 'U':'. . - ','V': '. . . -', 'W': '. - -', 'X': '- . . -',
    'Y': '- . - -', 'Z': '- - . .'
    
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
 

''' Opens a Text File '''
# Author: Sam Brewster
def OpenTextFile(filePath) :
    
    file = open(filePath)
    lines = file.readlines()
    
    for line in lines:
        cleaned_line = line.strip('\n')
        print(cleaned_line)
     
    return lines
          
      
''' Prints the Morse Code to The Output '''
# Author: Sam Brewster
def printMorseCode2(Morse_Lines, morseLength) :
    
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
                print(". ", end="")
                LEDSoundOn(float(morseLength))
                
            elif (currentString[incrementor] == '-') :
                
                currentMorseWord += "-"
                print("- ", end="")
                LEDSoundOn(2 * float(morseLength))
            
            elif (currentString[incrementor] == ' ') :
                
                print(currentMorseWord + printMorseWord(iteration))
                currentMorseWord = ""
                
            elif (currentString[incrementor] == '\n') :
                
                print(currentMorseWord + printMorseWord(iteration))
                currentMorseWord = ""

            incrementor += 1
            LEDSoundOff()
            sleep(float(morseLength))

        #print(currentMorseWord + printMorseWord(iteration))
        iteration = iteration + 1
        
    return        

''' Returns the Given Char as Morse Code'''
def convertChar (char) :
    
    print(morseCodeLibrary.get(char))
    return(morseCodeLibrary.get(char))

def writeMorseChar (char) :

    #writes to the file
    #include spaces between characters, 
    
    return 1

''' Prints the Morse Code to The Output '''
# Author: Sam Brewster
def printMorseCode(lines, morseLength) :
    
    iteration = 0
    print(len(lines))
    print(lines)
    
    while (iteration < len(lines)) :
        
        currentString = lines[iteration]
        curStringLength = len(currentString)
        incrementor = 0
        currentMorseWord = ""
        doNothing = 0
        
        while (curStringLength > incrementor) :
            
            if (currentString[incrementor] == '.') :
                
                currentMorseWord += "."
                print(". ", end="")
                LEDSoundOn(float(morseLength))
                
            elif (currentString[incrementor] == '-') :
                
                currentMorseWord += "-"
                print("- ", end="")
                LEDSoundOn(2 * float(morseLength))
            
            elif (currentString[incrementor] == ' ') :
                
                #print("  ")
                currentMorseWord = "  "
                
            elif (currentString[incrementor] == '\n') :
                
                print(printMorseWord(iteration))
                currentMorseWord = ""

            incrementor += 1
            LEDSoundOff()
            print("  ", end="")
            sleep(float(morseLength))

        #print(currentMorseWord + printMorseWord(iteration))
        iteration = iteration + 1
        
    return
        

''' Prints the Word that the Morse Code Is '''
# Author: Sam Brewster
def printMorseWord(lineNumber) :
    
    with open('/home/group-11/Desktop/mcencode.txt') as file:
        lines = file.readlines()
        
        return(" | " + lines[lineNumber])
       
''' Prints Attention '''
def printAttention() :
    
    print("- . - . - . | attention", end="")
    #write attention to file
   
''' Asks For The Length of the Morse Code Beeps '''
def askForMorseCodeLength() :
    
    print("How long would you like a Morse Code Input to be (In Seconds): ", end="")
    return input()

''' Main '''
def main() :
    
    #morseLength = askForMorseCodeLength()
    morseLength = .25
    filePath = '/home/group-11/Desktop/mcencode.txt'
    
    #printMorseCode(OpenTextFile(filePath), morseLength)

    convertChar(filePath[1])

#print(Text_Morse('/home/group-11/Desktop/mcencode.txt'))
#OpenTextFile()
#printMorseWord(1)
main()
#makeMorseList(filePath)
#LEDSound()
