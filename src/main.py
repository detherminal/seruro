import time
import os
import machine
import framebuf
import screen
import json
import utils
import sign

# Copyright (C) 2023 Seruro Project

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

def refreshUI(LCD):
    utils.clear(LCD)
    LCD.text("SERURO - MAIN MENU", 5, 5, LCD.black)
    LCD.text("--------------------", 5, 15, LCD.black)
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
        LCD.text("--------------------", 5, 35 + (file_count * 10), LCD.black)
        LCD.text("Press A To Refresh", 5, 45 + (file_count * 10), LCD.black)
        LCD.text("Press B To Sign Tx", 5, 55 + (file_count * 10), LCD.black)
    else:
        LCD.text("--------------------", 5, 25 + (file_count * 10), LCD.black)
        LCD.text("Press A To Refresh", 5, 35 + (file_count * 10), LCD.black)
        LCD.text("Press B To Sign Tx", 5, 45 + (file_count * 10), LCD.black)
    LCD.text("A", 220, 5, LCD.black)
    LCD.show()
    time.sleep(0.4)
    LCD.text("A", 220, 5, LCD.white)
    LCD.show()
  
def ethSignTx():
    print("Signing Tx")

def mainMenu():
    pwm = machine.PWM(machine.Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(65535) # Brightness - Max 65535
    LCD = screen.LCD_1point3inch()

    try:
        os.mkdir("./wallets")
    except:
        pass
    try:
        os.mkdir("./tx")
    except:
        pass

    button_a = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_UP)
    button_b = machine.Pin(17,machine.Pin.IN,machine.Pin.PULL_UP)
    button_x = machine.Pin(19,machine.Pin.IN,machine.Pin.PULL_UP)
    button_y = machine.Pin(21,machine.Pin.IN,machine.Pin.PULL_UP)

    joystick_up = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP)
    joystick_down = machine.Pin(18,machine.Pin.IN,machine.Pin.PULL_UP)
    joystick_left = machine.Pin(16,machine.Pin.IN,machine.Pin.PULL_UP)
    joystick_right = machine.Pin(20,machine.Pin.IN,machine.Pin.PULL_UP)
    joystick_press = machine.Pin(3,machine.Pin.IN,machine.Pin.PULL_UP)

    refreshUI(LCD)

    while True:
        if (button_a.value() == 0):
            refreshUI(LCD)
        if (button_b.value() == 0):
            sign.signTx(LCD)
        time.sleep(0.1)

if __name__ == "__main__":
    mainMenu()