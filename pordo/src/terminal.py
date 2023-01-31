import os

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def clear():
    # WARNING: USED SO MUCH, BE CAREFUL WHEN CHANGING
    os.system('cls' if os.name == 'nt' else 'clear')

def getPicoPath():
    if (os.name != "nt"):
        return "/run/media/" + os.getlogin() + "/CIRCUITPY/"