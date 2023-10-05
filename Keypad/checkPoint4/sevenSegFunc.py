# Imports
import RPi.GPIO as GPIO
from time import sleep

#Allows for cleaner runtime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


'''Setup the Output Pins and Start them at low'''
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW) # a - red wire
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # b - yellow
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # c - white wire
GPIO.setup(6,  GPIO.OUT, initial=GPIO.LOW) # d - purple wire
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # e - blue wire
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW) # f - brown wire
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # g - green wire
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)  # dp - purple wire
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # clock
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)  # dp - purple wire


'''
'    a
'    _
'  f|_|b
'  e|_|c.DP
'    d
' inside is g
'''

'''
def clkCycle():
    
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
'''

''' Function to Display 1 on 7SD'''
def display1() :
    # Needs to display b and c as High
    
    GPIO.output(15, GPIO.LOW)  # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH) # c
    GPIO.output(6,  GPIO.LOW)  # d
    GPIO.output(12, GPIO.LOW)  # e
    GPIO.output(14, GPIO.LOW)  # f
    GPIO.output(26, GPIO.LOW)  # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 2 on 7SD'''
def display2():
    # Needs to display a, b, g, e, and d as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.LOW)  # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.LOW)  # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 3 on 7SD'''
def display3():
    # Needs to display a, b, g, c, and d as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH)  # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.LOW) # e
    GPIO.output(14, GPIO.LOW)  # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 4 on 7SD'''
def display4():
    # Needs to display a, b, g, c, and d as High
    
    GPIO.output(15, GPIO.LOW) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH)  # c
    GPIO.output(6,  GPIO.LOW) # d
    GPIO.output(12, GPIO.LOW) # e
    GPIO.output(14, GPIO.HIGH)  # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 5 on 7SD'''
def display5():
    # Needs to display a, b, g, c, and d as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.LOW) # b
    GPIO.output(13, GPIO.HIGH)  # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.LOW) # e
    GPIO.output(14, GPIO.HIGH)  # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 6 on 7SD'''
def display6():
    # Needs to display a, b, g, c, and d as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.LOW) # b
    GPIO.output(13, GPIO.HIGH)  # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.HIGH)  # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 7 on 7SD'''
def display7():
    # Needs to display a, b, g, c, and d as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH)  # c
    GPIO.output(6,  GPIO.LOW) # d
    GPIO.output(12, GPIO.LOW) # e
    GPIO.output(14, GPIO.LOW)  # f
    GPIO.output(26, GPIO.LOW) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 8 on 7SD'''
def display8():
    # Needs to display a, b, g, c, and d as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH)  # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.HIGH)  # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 9 on 7SD'''
def display9():
    # Needs to display a, b, g, c, and d as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH)  # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.LOW) # e
    GPIO.output(14, GPIO.HIGH)  # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 0 on 7SD'''
def display0():
    # Needs to display a, b, c, d, e, and f as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH) # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.HIGH) # f
    GPIO.output(26, GPIO.LOW)  # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
# EOF

''' Function to Display 0 on 7SD'''
def displayA():
    # Needs to display a, b, c, d, e, and f as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH) # c
    GPIO.output(6,  GPIO.LOW) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.HIGH) # f
    GPIO.output(26, GPIO.HIGH)  # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
''' Function to Display 0 on 7SD'''
def displayb():
    # Needs to display a, b, c, d, e, and f as High
    
    GPIO.output(15, GPIO.LOW)  # a
    GPIO.output(10, GPIO.LOW)  # b
    GPIO.output(13, GPIO.HIGH) # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.HIGH) # f
    GPIO.output(26, GPIO.HIGH) # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
''' Function to Display 0 on 7SD'''
def displayC():
    # Needs to display a, b, c, d, e, and f as High
    
    GPIO.output(15, GPIO.HIGH) # a
    GPIO.output(10, GPIO.LOW) # b
    GPIO.output(13, GPIO.LOW) # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.HIGH) # f
    GPIO.output(26, GPIO.LOW)  # g
    #GPIO.output(16, GPIO.HIGH)  # DP
    
''' Function to Display 0 on 7SD'''
def displayd():
    # Needs to display a, b, c, d, e, and f as High
    
    GPIO.output(15, GPIO.LOW) # a
    GPIO.output(10, GPIO.HIGH) # b
    GPIO.output(13, GPIO.HIGH) # c
    GPIO.output(6,  GPIO.HIGH) # d
    GPIO.output(12, GPIO.HIGH) # e
    GPIO.output(14, GPIO.LOW) # f
    GPIO.output(26, GPIO.HIGH)  # g
    #GPIO.output(16, GPIO.HIGH)  # DP

''' Function to Display 0 on 7SD'''
def displayDP(decimalState):
    # Needs to display a, b, c, d, e, and f as High
    
    if (decimalState == True) :
        GPIO.output(16, GPIO.HIGH)  # DP
        print("dp off")
        return True
    
    return False

''' Function to Display 0 on 7SD'''
def displayOFF():
    # Needs to display a, b, c, d, e, and f as High
    
    GPIO.output(15, GPIO.LOW) # a
    GPIO.output(10, GPIO.LOW) # b
    GPIO.output(13, GPIO.LOW) # c
    GPIO.output(6,  GPIO.LOW) # d
    GPIO.output(12, GPIO.LOW) # e
    GPIO.output(14, GPIO.LOW) # f
    GPIO.output(26, GPIO.LOW)  # g
    GPIO.output(16,  GPIO.LOW)  # DP
    
#EOF
''' Blink The Screen '''
def blinkScreen() :
    
    display0()
    clkCycle(1)
    clkCycle(2)
    clkCycle(3)
    clkCycle(4)
    
    sleep(.5)
    
    displayOFF()
    clkCycle(1)
    clkCycle(2)
    clkCycle(3)
    clkCycle(4)

''' Calls the Clock Cycle '''
def clkCycle(cycleNum):
    
    if (cycleNum == 1) :   # Clock pulses for first digit
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
    elif (cycleNum == 2) : #Clock pulses for second digit
        GPIO.output(9, GPIO.HIGH)
        GPIO.output(9, GPIO.LOW)
    elif (cycleNum == 3) : # Clock pulses for third digit
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
    elif (cycleNum == 4) : # Clock pulses for fourth digit
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)