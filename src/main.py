import time
import os
from machine import Pin,SPI,PWM
import framebuf
import lcd1_3inch
        
# Copyright (C) 2023 Seruro Project

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9

def clear():
    LCD.fill(LCD.black)
    LCD.fill(LCD.white)
    LCD.show()

def refreshUI():
    clear()
    LCD.text("SERURO", 5, 5, LCD.black)
    LCD.text("-------------", 5, 15, LCD.black)
    LCD.text("1 - Eth - 0.23 Ether", 5, 25, LCD.black)
    LCD.text("-------------", 5, 35, LCD.black)
    LCD.text("Press A To Refresh", 5, 45, LCD.black)
    LCD.show()
  
def ethSignTx():
    print("Signing Tx")

if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(65535) # Brightness - Max 65535
    LCD = lcd1_3inch.LCD_1point3inch()

    os.mkdir("wallets")

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
