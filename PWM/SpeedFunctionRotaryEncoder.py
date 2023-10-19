    #code for setting up digipot  
def turnDigiPot(clk, dt, potNum):
    digiVal = 0
    #starts the time for to determine the speed of the rotary encoder's turning
    
    clkLastState = GPIO.input(18)
    counter = 0
    changeInValue = 5000
    oldValue = 5000
    newValue = 5000
    timeSinceLast = -1

    #gets the inputs of the clk and dt states

    while True:
        
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        
        #checks if there has been a change in state
        if (clkState != clkLastState and dtState == 1):
            
            startTimeTurnDigiPot = timeSinceLast
            timeSinceLast = time.time()
            
            #if so, calculates the speed of the turning
            timeTakenToSpin = (time.time() - startTimeTurnDigiPot)
            startTimeTurnDigiPot = time.time()
            #startTimeTurnDigiPlot = time.time() #resets the clock
                        
            #if the speed is fast, does below statement
            if (timeTakenToSpin < .1):
                if (dtState != clkState):
                    changeInValue += 100
                    if (changeInValue > 10000): #ensures that the value does not go above 10000
                        changeInValue = 10000     
                    print(changeInValue)
                else: #(dtState == clkState and clkState != 1):
                    changeInValue -= 100
                    if (changeInValue < 100): #ensures that the value does not go below 100
                        changeInValue = 100
                    print(changeInValue)
                newValue = changeInValue
        #if the speed is slow, does below statement
            else:
                if (dtState != clkState):
                    changeInValue += 10
                    if (changeInValue > 10000): #ensures that the value does not go above 10000
                        changeInValue = 10000
                    print(changeInValue)
                else:
                    changeInValue -= 10
                    if (changeInValue < 100): #ensures that the value does not go below 100
                        changeInValue = 100
                    print(changeInValue)
                newValue = changeInValue
                
        clkLastState = clkState # updates state for next loop

        time.sleep(.001)
        
        if (newValue != oldValue):
            lcd.setCursor(0,1)
            lcd.printout("      ")
            lcd.setCursor(0,1)
            lcd.printout(changeInValue)
            lcd.setCursor(6,1)
            lcd.printout("Ohms")
        
        oldValue = newValue
        
        #Checks if a button got pushed
        if (GPIO.input(27) == GPIO.LOW):
            if (holdButton(27) == True):
                #button held: return to main
                lcd.clear()
                lcd.printout("Returning to")
                lcd.setCursor(0,1)
                lcd.printout("Select Screen...")
                return #back to main
                
                ## release pigpio resources
                pi.stop()
            else:
                #button pressed: select value of digiPot
                print("Value Set")
                print(changeInValue)
                
                ## check which digipot was selected
                if (potNum == 1) :
                    ## invoke control digi
                    control_digipot.controlPot1(newValue)
                    
                elif (potNum == 0) :
                    ## invoke control digi
                    control_digipot.controlPot0(newValue)
                    
                ## sleep program to prevent immediately changing value after setting it   
                time.sleep(0.25)
                
