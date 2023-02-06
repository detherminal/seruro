import terminal
import show
import json
import os
import importlib
import subprocess

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def sendCoins():
    isInvalid = False
    terminal.clear()
    while True:
        terminal.clear()
        print("Send Coins")
        print("-" * 50)
        print("Choose A Wallet (Enter The Number Of Option): ")
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
                wallets_array.append([count, name, public_adress, balance, currency, out[5]])
            for wallet in wallets_array:
                print(str(wallet[0]) + " - " + wallet[1] + " - " + wallet[2] + " - " + str(wallet[3]) + " " + wallet[4])
            print("-"  * 50)
            print("0 - Exit")
            if (isInvalid):
                print("Invalid Option")
            answer = input("> ")
            if (answer == "0"):
                break
            else:
                try:
                    answer = int(answer)
                    for wallet in wallets_array:
                        if (answer == int(wallet[0])):
                            output = subprocess.check_output("sudo rshell --quiet cat /seruro/wallets/" + wallet[1].lower() + ".keys", shell=True)
                            wallet = json.loads(output)
                            public_adress = wallet["public_adress"]
                            password = input("Enter Password: ")
                            recipient = input("Enter Recipient Adress: ")
                            amount = input("Enter Amount (e.g. 0.1): ")
                            module = importlib.import_module("coins." + wallet[1].lower())
                            module.sendCoins(public_adress, recipient, amount, password)
                            break
                        else:
                            continue
                except:
                    isInvalid = True
                    input("Press Enter To Continue...")
        except:
            print("No Wallets Found")
            print("-" * 50)
            input("Press Enter To Continue...")
            break


def receiveCoins():
    terminal.clear()
    print("You can receive coins from the user by giving them the adress in the wallets page.")
    input("Press Enter To Continue...")
    terminal.clear()
    show.showAllWalletsAndBalances()
