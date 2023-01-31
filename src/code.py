import board
import time
import digitalio
import os

def turnLedOnAndOff(turn):
    passedTurns = 0
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    while passedTurns < turn:
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)
        passedTurns += 1
    
def main():
    # This is the entry point of the application.
    try:
        with open("config.json", "r") as config:
            # If the config file exists, then the Pico is configured.
            turnLedOnAndOff(1)
    except:
        turnLedOnAndOff(2)
            
main()