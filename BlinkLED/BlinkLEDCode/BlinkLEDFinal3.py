import pigpio

pi=pigpio.pi()

pi.set_PWM_frequency(27, 100000)
pi.set_PWM_dutycycle(27, 15)

while True:
    
    print("running")