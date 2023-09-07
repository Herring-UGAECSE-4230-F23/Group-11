import wiringpi

wiringpi.wiringPiSetupGpio()

wiringpi.softToneCreate(27)
wiringpi.softToneWrite(27,15000)

while True:
    
    print("running")
        
wiringpi.softToneWrite(27,0)