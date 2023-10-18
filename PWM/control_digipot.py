## Credit to Group 12 for helping to discuss the algorithm of this implementation and troubleshoot hardware
## Author: Vinessa ALmanza

##comprises of all necesary methods to use to write data to digipots to control resistance values
import RPi.GPIO as GPIO
import pigpio ## library using for spi methods
import time

def controlPot0(resistance) :
    ## initializes connection to pigpio daemon 
    pi = pigpio.pi()

    ## opens a spi channel to send data to spi object
    handler = pi.spi_open(0, 97600)
    
    ## determines num of steps (wiper position) based off given resistance
    wiperPos = int((resistance*128)/10000)
    
    print("programmed value p0: " + str((wiperPos*int(10000/128))))
    
    ## writes to digipot 0
    pi.spi_write(handler, [0b0000_0000, wiperPos])
    
    ## close handler
    pi.spi_close(handler)

def controlPot1(resistance) :
    ## initializes connection to pigpio daemon 
    pi = pigpio.pi()

    ## opens a spi channel to send data to spi object
    handler = pi.spi_open(0, 97600)
    
    ## determines num of steps (wiper position) based off given resistance
    wiperPos = int((resistance*128)/10000)
    
    print("programmed value p1: " + str((wiperPos*int(10000/128))))
    
    ## writes to digipot 1
    pi.spi_write(handler, [0b0001_0000, wiperPos])
    
    ## close handler
    pi.spi_close(handler)

