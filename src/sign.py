import utils
import time
import os
import machine
import main

def signTx(LCD):
    utils.clear(LCD)
    LCD.text("SERURO - SIGN TX MENU", 5, 5, LCD.black)
    LCD.text("--------------------", 5, 15, LCD.black)
    LCD.text("B", 220, 5, LCD.black)
    LCD.show()
    dir = os.listdir("tx")
    file_count = 0
    for file in dir:
        file_count += 1
        currency = file.removesuffix(".tx")
    if (file_count == 0):
        LCD.text("No Transaction Found", 5, 25, LCD.black)
        LCD.text("--------------------", 5, 35, LCD.black)
        LCD.text("Press A To Return Main Menu", 5, 45, LCD.black)
        LCD.text("Press B To Refresh", 5, 55, LCD.black)
    time.sleep(0.4)
    LCD.text("B", 220, 5, LCD.white)
    LCD.show()