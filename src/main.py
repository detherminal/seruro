import time
import os
from machine import Pin,SPI,PWM
import framebuf
import lcd1_3inch
import json
import sys

# Copyright (C) 2023 Seruro Project

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

def clear():
    LCD.fill(LCD.white)
    LCD.show()

def refreshUI():
    clear()
    LCD.text("SERURO", 5, 5, LCD.black)
    LCD.text("-------------", 5, 15, LCD.black)
    LCD.show()
    dir = os.listdir("wallets")
    file_count = 0
    for file in dir:
        file_count += 1
        with open("./wallets/" + file) as file:
            json_file = json.loads(file.read())
            balance = json_file["balance"]
            name = json_file["name"]
            currency = json_file["currency"]
            LCD.text(str(file_count) + " - " + name + " - " + str(balance) + " " + currency, 5, 15 + (file_count * 10), LCD.black)
    if (file_count == 0):
        LCD.text("No Wallets Found", 5, 25 + (file_count * 10), LCD.black)
        LCD.text("-------------", 5, 35 + (file_count * 10), LCD.black)
        LCD.text("Press A To Refresh", 5, 45 + (file_count * 10), LCD.black)
    else:
        LCD.text("-------------", 5, 25 + (file_count * 10), LCD.black)
        LCD.text("Press A To Refresh", 5, 35 + (file_count * 10), LCD.black)
    LCD.text("A", 220, 5, LCD.black)
    LCD.show()
    time.sleep(0.4)
    LCD.text("A", 220, 5, LCD.white)
    LCD.show()
  
def ethSignTx():
    print("Signing Tx")

if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(65535) # Brightness - Max 65535
    LCD = lcd1_3inch.LCD_1point3inch()

    try:
        os.mkdir("./wallets")
    except:
        pass

    button_a = Pin(15,Pin.IN,Pin.PULL_UP)
    button_b = Pin(17,Pin.IN,Pin.PULL_UP)
    button_x = Pin(19 ,Pin.IN,Pin.PULL_UP)
    button_y = Pin(21 ,Pin.IN,Pin.PULL_UP)
    
    joystick_up = Pin(2,Pin.IN,Pin.PULL_UP)
    joystick_down = Pin(18,Pin.IN,Pin.PULL_UP)
    joystick_left = Pin(16,Pin.IN,Pin.PULL_UP)
    joystick_right = Pin(20,Pin.IN,Pin.PULL_UP)
    joystick_ctrl = Pin(3,Pin.IN,Pin.PULL_UP)

    refreshUI()

    while True:
        if (button_a.value() == 0):
            refreshUI()
        time.sleep(0.1)