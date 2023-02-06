import terminal
import setup
import json
import subprocess

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def connectToPico():
    isConnected = False
    terminal.clear()
    print("Connection")
    print("-" * 50)
    print("Connecting To Pico...")
    output = subprocess.check_output("sudo rshell --quiet ls -l /seruro/", shell=True).decode("utf-8").strip().split("\n")
    outputs = []
    for out in output:
        out = out.strip().split(" ")
        outputs.append(out)
    for out in outputs:
        if (out[5]) == "board.py":
            isConnected = True
            print("Pico Found")
    if (isConnected):
        try:
            output = subprocess.check_output("sudo rshell --quiet cat /seruro/config.json", shell=True).decode("utf-8").strip()
            config = json.loads(output)
            if (not config["isSetup"]):
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
    else:
        print("Pico Not Found")
        print("Please Connect Pico And Try Again")
    print("-" * 50)
    input("Press Enter To Return Main Menu...")
    return isConnected