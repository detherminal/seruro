import terminal
import importlib
import os
import json
import subprocess

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def addOrRemoveWalletMenu():
    isInvalid = False
    terminal.clear()
    while True:
        print("Wallets")
        print("-" * 50)
        print("1 - Add Wallet")
        print("2 - Remove Wallet")
        print("0 - Exit")
        if (isInvalid):
            print("Invalid Option")
        answer = input("> ")
        if (answer == "1"):
            addWallet()
            break
        elif (answer == "2"):
            removeWallet()
            break
        elif (answer == "0"):
            break
        else:
            isInvalid = True
            terminal.clear()
            continue

def addWallet():
    isInvalid = False
    isAdded = False
    terminal.clear()
    while True:
        print("Wallet Setup")
        print("-" * 50)
        print("Choose A Blockchain (Enter The Number Of Option): ")
        with open("coins.json", "r") as blockchains:
            blockchains = json.load(blockchains)
            coins = blockchains["coins"]
            for coin in coins:
                print(str(coins[coin]["number"]) + " - " + coins[coin]["name"])
            print("0 - Exit")
        if (isInvalid):
            print("Invalid Option")
        answer = input("> ")
        if (answer == "0"):
            break
        else:
            try:
                answer = int(answer)
                with open("coins.json", "r") as coins:
                    blockchains = json.load(coins)
                    coins = blockchains["coins"]
                    for coin in coins:
                        if (answer == coins[coin]["number"]):
                            module = importlib.import_module("coins." + coins[coin]["symbol"])
                            module.setup()
                            isAdded = True
                            break
                        else:
                            continue
            except(KeyError):
                isInvalid = True
        if (isAdded):
            break
        else:
            terminal.clear()
            continue


def removeWallet():
    isInvalid = False
    terminal.clear()
    while True:
        terminal.clear()
        print("Remove Wallet")
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
                            print("Removing Wallet...")
                            command = "sudo rshell --quiet rm -r /seruro/wallets/" + str(wallet[5])
                            os.system(command)
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