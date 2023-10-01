#Group 11's Code for Wiringpi

#imports library
import wiringpi

#Initializes GPIO pin 27
wiringpi.wiringPiSetupGpio()
wiringpi.softToneCreate(27)

#Outputs a frequency of 15000 to GPIO 27
wiringpi.softToneWrite(27,15000)

#Forever loop to let know its running
while True:
    
    print("running")

#Kills the output.
wiringpi.softToneWrite(27,0)
