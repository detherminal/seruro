import terminal
import os
import setup
import json

def connectToPico():
    isConnected = False
    terminal.clear()
    print("Connection")
    print("-" * 50)
    print("Connecting To Pico...")
    try:
        user = os.getlogin()
        with open("/run/media/" + user + "/CIRCUITPY/code.py", "r"):
            isConnected = True
            print("Pico Found")
    except:
        isConnected = False
        print("Pico Not Found")
    if (isConnected):
        try:
            with open("/run/media/" + user + "/CIRCUITPY/config.json", "r") as config:
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
    input("Press Enter To Return Main Menu...")
    return isConnected