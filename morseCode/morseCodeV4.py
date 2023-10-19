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

  
# Author: Austin Iverson
morseCodeLibrary={
    'A': '. -', 'B': '- . . .', 'C': '- . - .', 'D': '- . .', 'E': '.', 'F': '. . - .', 'G':'- - .','H': '. . . .',
    'I': '. .', 'J': '.- - -', 'K': '- . -', 'L': '. - . .', 'M': '- -', 'N':'- .', 'O':'- - -', 'P': ' . - - .',
    'Q': '- - . -', 'R': '. - .', 'S': '. . .', 'T': '-', 'U':'. . - ','V': '. . . -', 'W': '. - -', 'X': '- . . -',
    'Y': '- . - -', 'Z': '- - . .'
    
    'a' '. -', 'b': '- . . .', 'c': '- . - .', 'd': '- . .', 'e': '.', 'f': '. . - .', 'g':'- - .', 'h': '. . . .',
    'i': '. .', 'j': '. - - -', 'k': '- . -', 'l': '. - . .', 'm': '- -','n':'- .', 'o':'- - - ', 'p': ' . - - .',
    'q': '- - . -', 'r': '. - .', 's': '. . . ', 't': '-', 'u':'. . -','v': '. . . -', 'w': '. - -', 'x': '- . . -',
    'y': '- . - -', 'z': '- - . .'
}

morseCodeLibraryNoSpace={
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g':'--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--','n':'-.', 'o':'---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '... ', 't': '-', 'u':'..-','v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.---', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
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
        loops = loops + 1
        
 

''' Opens a Text File '''
# Author: Sam Brewster
def OpenTextFile(filePath) :
    
    file = open(filePath)
    lines = file.readlines()
    
    for line in lines:
        cleaned_line = line.strip('\n')
     
    return lines
          


''' Returns the Given Char as Morse Code'''
def convertChar (engChar) :
    
    return(morseCodeLibraryNoSpace.get(engChar))


''' Writes the Morse Character to both the Output File and Terminal '''
def writeMorseChar (morseChar, morseLength) :

    #writes to the file
    #include spaces between characters
    incrementor = 0
    LEDSoundOff()
    entry = True
    
    while (incrementor < len(morseChar)) :
        
        entry = False
        
        if (morseChar[incrementor] == '.') :
            
            #its a dot
            print('. ', end="")
            output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
            output.write('. ')
            output.close()
            LEDSoundOn(float(morseLength))
            
        elif (morseChar[incrementor] == '-') :
    
            print('- ', end="")
            output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
            output.write('- ')
            output.close()
            LEDSoundOn(3 * float(morseLength))
            #its a dash
        
        incrementor += 1
        LEDSoundOff()
        sleep(morseLength)
    
    return 1

''' Prints the Morse Code to The Output '''
# Author: Sam Brewster
def printMorseCode(lines, morseLength) :
    
    iteration = 0
    lastWordLocation = 0
    
    while (iteration < len(lines)) :
        
        currentString = lines[iteration]
        curStringLength = len(currentString)
        incrementor = 0
        currentMorseWord = ""
        tracking = 0
        lastLetter = True
        
        while (curStringLength > incrementor) :
            
            if (currentString[incrementor] == ' ') :
                
                i = lastWordLocation
                #new word in message
                print("| ", end="")
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('| ')
                output.close()
                
                while (i < incrementor) :
                    
                    print(currentString[i], end="")
                    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                    output.write(currentString[i])
                    output.close()
                    i += 1
                    
                print()
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('\n')
                output.close()                
                lastWordLocation = incrementor
                tracking = lastWordLocation
                lastLetter = True
                    
            elif (currentString[incrementor] == '\n') :
                
                #new message
                i = lastWordLocation
                #new word in message
                print("| ", end="")
                
                while (i < incrementor) :
                    
                    print(currentString[i], end="")
                    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                    output.write(currentString[i])
                    output.close()
                    i += 1
                    
                print()
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('\n')
                output.close()
                lastWordLocation = 0
                tracking = lastWordLocation
                printSeven = True
                lastLetter = True
                printOver(morseLength)
                
            else :
                if (lastLetter == False) :
                    print("  ", end="")
                    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                    output.write('  ')
                    output.close()
                
                writeMorseChar(convertChar(currentString[incrementor]), morseLength)
                lastLetter = False
                

            incrementor += 1
            LEDSoundOff()      
            sleep(float(morseLength))

            if (tracking != 0) :
                
                print("       ", end="")
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('       ')
                output.close()
                tracking = 0
                
        #print(currentMorseWord + printMorseWord(iteration))
        iteration = iteration + 1
        
    return
        

''' Prints the Word that the Morse Code Is '''
# Author: Sam Brewster
def printMorseWord(lineNumber) :
    
    with open('/home/group-11/Desktop/mcencode.txt') as file:
        lines = file.readlines()
        
        return(" | " + lines[lineNumber])
       
       
''' Prints Attention When Called '''
def printAttention(morseLength) :
    #-.-.-
    
    print('- ', end="")
    LEDSoundOn(3 * float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('. ', end="")
    LEDSoundOn(float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('- ', end="")
    LEDSoundOn(3 * float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('. ', end="")
    LEDSoundOn(float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('- ', end="")
    LEDSoundOn(3 * float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print("| attention")
    output = open('/home/group-11/Desktop/morseCode/output.txt', 'w')
    output.write("- . - . - | attention\n")
    output.close()
    #write attention to file
 
 
''' Prints Out When Called '''
def printOut(morseLength) :
    #.-.-.
        
    print('. ', end="")
    LEDSoundOn(float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('- ', end="")
    LEDSoundOn(3 * float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('. ', end="")
    LEDSoundOn(float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('- ', end="")
    LEDSoundOn(3 * float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('. ', end="")
    LEDSoundOn(float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print("| out")
    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
    output.write('. - . - . | out\n')
    output.close()
    

''' Prints Over When Called'''
def printOver(morseLength) :
    #-.-
    print('- ', end="")
    LEDSoundOn(3 * float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('. ', end="")
    LEDSoundOn(float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print('- ', end="")
    LEDSoundOn(3 * float(morseLength))
    LEDSoundOff()      
    sleep(float(morseLength))
    
    print("| over")
    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
    output.write('- . - | over\n')
    output.close()
    
    
''' Asks For The Length of the Morse Code Beeps '''
def askForMorseCodeLength() :
    
    print("How long would you like a Morse Code Input to be (In Seconds): ", end="")
    return input()

''' Main '''
def main() :
    
    morseLength = float(askForMorseCodeLength())
    LEDSoundOff()
    filePath = '/home/group-11/Desktop/morseCode/mcencode.txt'
    
    printAttention(morseLength)
    
    printMorseCode(OpenTextFile(filePath), morseLength)
    
    printOut(morseLength)

    #Call print out
    #writeMorseChar(convertChar('a'), morseLength)
    

#print(Text_Morse('/home/group-11/Desktop/mcencode.txt'))
#OpenTextFile()
#printMorseWord(1)
main()
#makeMorseList(filePath)
#LEDSound()
