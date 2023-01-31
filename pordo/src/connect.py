import terminal
import setup
import json

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def connectToPico():
    isConnected = False
    terminal.clear()
    print("Connection")
    print("-" * 50)
    print("Connecting To Pico...")
    try:
        with open(terminal.getPicoPath() + "code.py", "r"):
            isConnected = True
            print("Pico Found")
    except:
        isConnected = False
        print("Pico Not Found")
    if (isConnected):
        try:
            with open(terminal.getPicoPath() + "config.json", "r") as config:
                print("Config File Found")
                config = json.load(config)
                if (config["isSetup"] == False):
                    print("Pico Not Setup")
                    print("Starting Setup...")
                    input("Press Enter To Continue...")
                    setup.setup()
                else:
                    print("Successfully Connected To Pico")
        except:
            print("Config File Not Found")
            print("Starting Setup...")
            input("Press Enter To Continue...")
            setup.setup()
    print("-" * 50)
    input("Press Enter To Return Main Menu...")
    return isConnected