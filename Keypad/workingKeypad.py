import RPi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# From Pi Pad 4, 17, 27, 22
# 23, 24, 25, 5

GPIO.setup(23, GPIO.IN)
state = GPIO.input(23)

GPIO.setup(24, GPIO.IN)
state = GPIO.input(24)

GPIO.setup(25, GPIO.IN)
state = GPIO.input(25)

GPIO.setup(5, GPIO.IN)
state = GPIO.input(5)

GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)

#pull up?
one = [1, 2, 3, 'A']
two = [4, 5, 6, 'B']
three = [7, 8, 9, 'C']
four = ['*', '0', '#', 'D']

stop = 0

def readKeyPad(rowNum, char):
    
    curVal = 0
    
    GPIO.output(rowNum, GPIO.HIGH)
    
    if GPIO.input(23) == 1:
        curVal = char[0]
    if GPIO.input(24) == 1:
        curVal = char[1]
    if GPIO.input(25) == 1:
        curVal = char[2]
    if GPIO.input(5) == 1:
        curVal = char[3]
        
    GPIO.output(rowNum, GPIO.LOW)
    
    return curVal

while stop == 0:
    
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
    
print("You want to print", stop)
GPIO.output(12, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)

#GPIO.cleanup()
