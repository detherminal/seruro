import board
import microcontroller
import time
import digitalio

# Copyright (c) 2023 Seruro Project

def main():
    # This is the entry point of the application.
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    while True:
        time.sleep(0.5)
        led.value = not led.value

main()