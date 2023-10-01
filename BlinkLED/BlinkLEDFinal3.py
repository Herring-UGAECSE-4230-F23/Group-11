#Group 11's Pigpio code

#import library
import pigpio

#initialize the pi
pi=pigpio.pi()

#sets frequency and duty cycle
pi.set_PWM_frequency(27, 100000)
pi.set_PWM_dutycycle(27, 15)

#Forever loop to keep wave running
while True:
    
    print("running")
