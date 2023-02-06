import terminal
import json
import os
import subprocess
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
        output = subprocess.check_output("sudo rshell --quiet ls -l /seruro/wallets", shell=True).decode("utf-8").strip().split("\n")
        outputs = []
        wallets_array = []
        for out in output:
            out = out.strip().split(" ")
            outputs.append(out)
        try:
            count = 0
            for out in outputs:
                count += 1
                file_output = subprocess.check_output("sudo rshell --quiet cat /seruro/wallets/" + out[5], shell=True).decode("utf-8").strip()
                wallet = json.loads(file_output)
                name = str(wallet["name"])
                public_adress = wallet["public_adress"]
                module = importlib.import_module("coins." + name.lower())
                balance = module.getBalance(public_adress)
                currency = wallet["currency"]
                wallets_array.append([count, name, public_adress, balance, currency])
        except:
            terminal.clear()
            print("Show All Wallets And Balances")
            print("-" * 50)
            print("No Wallets Found")
            print("-" * 50)
            input("Press Enter To Return Main Menu...")
            return
        terminal.clear()
        print("Show All Wallets And Balances")
        print("-" * 50)
        for line in wallets_array:
            print(str(line[0]) + " - " + line[1] + " - " + line[2] + " - " + str(line[3]) + " " + line[4])
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
