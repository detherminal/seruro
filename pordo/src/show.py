import terminal
import json
import os
import importlib

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def showAllWalletsAndBalances():
    isInvalid = False
    terminal.clear()
    while True:
        terminal.clear()
        print("Show All Wallets And Balances")
        print("-" * 50)
        print("Loading...")
        dir = os.listdir(terminal.getPicoPath() + "wallets")
        output = []
        if (len(dir) == 0):
            terminal.clear()
            print("Show All Wallets And Balances")
            print("-" * 50)
            print("No Wallets Found")
        else:
            count = 0
            for file in dir:
                count += 1
                with open(terminal.getPicoPath() + "wallets/" + file, "r") as file:
                    wallet = json.loads(file.read())
                    name = str(wallet["name"])
                    public_adress = wallet["public_adress"]
                    module = importlib.import_module("coins." + name.lower())
                    balance = module.getBalance(public_adress)
                    currency = wallet["currency"]
                    output.append(str(count) + " - " + name + " - " + public_adress + " - " + str(balance) + " " + currency)
            terminal.clear()
            print("Show All Wallets And Balances")
            print("-" * 50)
            for line in output:
                print(line)
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
