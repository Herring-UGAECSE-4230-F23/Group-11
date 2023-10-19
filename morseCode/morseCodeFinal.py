import RPi.GPIO as GPIO
from time import sleep
#import simpleaudio
import numpy

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

'''Setup the Output Pins and Start them at low'''
GPIO.setup(4,  GPIO.OUT)                    # Sets the Speaker pin to an output
GPIO.setup(17,  GPIO.OUT, initial=GPIO.LOW) # Sets the LED Pin to an output
speaker = GPIO.PWM(4, 1200) # Allows for the speaker output


''' Turns the LED and Sound On '''
# Author: Austin Iverson
def LEDSoundOn (time):

    # Ouputs a high to the LED Pin and starts the PWM to the speaker
    GPIO.output(17,GPIO.HIGH)
    speaker.start(50)
 
    sleep(time) # Sleeps whatever length the user gives for the morse length

    return


''' Turns the LED and Sound Off '''
# Author: Sam Brewster
def LEDSoundOff() :
    
    # Turns off the LED and Speaker
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

# Author: Austin Iverson
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

    # Opens a File and Reads the Lines into a List Called 'lines'
    with open(filePath) as file:
        lines = file.readlines()
        
    Morse_Lines = [] # Makes a List
    
    for line in lines:
        cleaned_line = line.strip() # Cleans the Whitespace out
        Morse_Line=''.join([morseCodeLibrary.get(char.upper(),char)for char in line]) # Gets the corresponding morse for each character
        Morse_Lines.append(Morse_Line) # Adds the morse code to the list

    # Returns a list of all Morse Code for the File
    return Morse_Lines


''' A Nonessential Function'''
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

    # Creates a file object and reads the lines from the file given
    file = open(filePath)
    lines = file.readlines()
    
    for line in lines:
        cleaned_line = line.strip('\n') #Takes the \n out of each line, unnecessary
     
    return lines # Returns the list of strings
          

''' Returns the Given Char as Morse Code'''
def convertChar (engChar) :

    # Returns the parameter char as morse code obtained from our library
    return(morseCodeLibraryNoSpace.get(engChar)) 


''' Writes the Morse Character to both the Output File and Terminal '''
def writeMorseChar (morseChar, morseLength) :

    #writes to the file
    #include spaces between characters
    incrementor = 0
    LEDSoundOff()

    # Increments for the length of the word given
    while (incrementor < len(morseChar)) :

        # Checks each morse character
        if (morseChar[incrementor] == '.') :
            
            # If its a dot, print, write, and beep accordingly.
            print('. ', end="")
            output = open('/home/group-11/Desktop/morseCode/output.txt', 'a') # Opens File
            output.write('. ') # Writes
            output.close() # Closes File
            LEDSoundOn(float(morseLength)) # Turns the LED and Sound on for 1 times the morse length
            
        elif (morseChar[incrementor] == '-') :

            # If its a dash, print, write, and beep accordingly.
            print('- ', end="")
            output = open('/home/group-11/Desktop/morseCode/output.txt', 'a') # Opens Files
            output.write('- ') # Writes
            output.close() # Closes File
            LEDSoundOn(3 * float(morseLength)) # Turns the LED and sound on for 3 times the morse length
           
        
        incrementor += 1
        LEDSoundOff() # Turns the LED and sound off
        sleep(morseLength) # Ensures the period of off lasts for the morse length
    
    return 1

''' Prints the Morse Code to The Output '''
# Author: Sam Brewster
def printMorseCode(lines, morseLength) :
    
    iteration = 0
    lastWordLocation = 0

    # Iterates for the amount of lines in the input file
    while (iteration < len(lines)) :

        # Initialize a bunch of variables used
        currentString = lines[iteration]
        curStringLength = len(currentString)
        incrementor = 0
        currentMorseWord = ""
        tracking = 0
        lastLetter = True

        # Main Logic Loop
        while (curStringLength > incrementor) :
            
            if (currentString[incrementor] == ' ') :
                # If the character is a space, end the line
                
                i = lastWordLocation
                # Print and write so we can follow it with the english translation
                print("| ", end="")
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('| ')
                output.close()
                
                while (i < incrementor) :
                    # Prints the word in english
                    
                    print(currentString[i], end="")
                    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                    output.write(currentString[i])
                    output.close()
                    i += 1 # increments to show where in word we are
                    
                print() # prints a new line
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('\n')
                output.close()             

                # Set variables to keep track of location in file
                lastWordLocation = incrementor
                tracking = lastWordLocation
                lastLetter = True
                    
            elif (currentString[incrementor] == '\n') :
                # Means that there is a new message
                
                i = lastWordLocation
                #new word in message
                print("| ", end="")

                
                while (i < incrementor) :
                    # Prints the word in english
                    
                    print(currentString[i], end="")
                    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                    output.write(currentString[i])
                    output.close()
                    i += 1
                    
                print() # Prints new line
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('\n')
                output.close()

                # Logic to keep track of location in file
                lastWordLocation = 0
                tracking = lastWordLocation
                printSeven = True
                lastLetter = True
                printOver(morseLength) # Calls a function to print over to signify that the message is over
                
            else :
                if (lastLetter == False) :
                    # If its not the last letter, this gives it the three long spacing
                    
                    print("  ", end="")
                    output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                    output.write('  ')
                    output.close()

                # Calls our function to write the morse 
                writeMorseChar(convertChar(currentString[incrementor]), morseLength)
                lastLetter = False
                

            # Increments the loop and resets the beeping of the LED and speaker
            incrementor += 1
            LEDSoundOff()      
            sleep(float(morseLength))

            # Logic for having seven spaces on continuing messages
            if (tracking != 0) :
                
                print("       ", end="")
                output = open('/home/group-11/Desktop/morseCode/output.txt', 'a')
                output.write('       ')
                output.close()
                tracking = 0
                
        #print(currentMorseWord + printMorseWord(iteration))
        iteration = iteration + 1
        
    return
        

''' Useless function '''
# Author: Sam Brewster
def printMorseWord(lineNumber) :
    
    with open('/home/group-11/Desktop/mcencode.txt') as file:
        lines = file.readlines()
        
        return(" | " + lines[lineNumber])
       
       
''' Prints Attention When Called '''
# Author: Sam Brewster
def printAttention(morseLength) :
    # Hard coded to print and write : '-.-.-'

    # Writes accordingly and beeps the LED and Sound
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
    
 
''' Prints Out When Called '''
# Author: Sam Brewster
def printOut(morseLength) :
    # Hard coded to print and write : '.-.-.'

    # Writes accordingly and beeps the LED and Sound
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
    # Hard coded to print and write : '-.-'

    # Writes accordingly and beeps the LED and Sound
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
    # Prompts the user for input and returns it
    
    print("How long would you like a Morse Code Input to be (In Seconds): ", end="")
    return input()

''' Main '''
def main() :
    # The Main Function for the Morse Code Running
    
    morseLength = float(askForMorseCodeLength()) # Grabs the length of each Morse Code pause
    LEDSoundOff() # Sets the Morse Code to be Off immediately
    filePath = '/home/group-11/Desktop/morseCode/mcencode.txt' # Initialize
    
    printAttention(morseLength) # Prints Attention
    
    printMorseCode(OpenTextFile(filePath), morseLength) # Prints the Content
    
    printOut(morseLength) # Prints Out

    #Call print out
    #writeMorseChar(convertChar('a'), morseLength)
    

#print(Text_Morse('/home/group-11/Desktop/mcencode.txt'))
#OpenTextFile()
#printMorseWord(1)
main()
#makeMorseList(filePath)
#LEDSound()
