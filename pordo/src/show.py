import terminal
import json
import os

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def showAllWalletsAndBalances():
    isInvalid = False
    terminal.clear()
    user = os.getlogin()
    while True:
        terminal.clear()
        print("Show All Wallets And Balances")
        print("-" * 50)
        dir = os.listdir("/run/media/" + user + "/CIRCUITPY/wallets")
        if (len(dir) == 0):
            print("No Wallets Found")
        else:
            count = 0
            for file in dir:
                count += 1
                with open("/run/media/" + user + "/CIRCUITPY/wallets/" + file, "r") as file:
                    wallet = json.loads(file.read())
                    name = str(wallet["name"])
                    public_adress = wallet["public_adress"]
                    balance = 0
                    print(str(count) + " - " + name + " - " + public_adress + " - " + str(balance) + "$")
                    print("-" * 50)
        print("Choose An Option (Enter The Number Of Option):")
        print("0 - Back")
        if (isInvalid):
            print("Invalid Option")
        option = input("> ")
        if (option == "0"):
            break
        else:
            isInvalid = True
            continue
