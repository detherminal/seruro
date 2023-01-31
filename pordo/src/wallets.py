import terminal
import importlib
import os
import json

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
                    coins = json.load(coins)
                    coins = blockchains["coins"]
                    for coin in coins:
                        if (answer == coins[coin]["number"]):
                            module = importlib.import_module("coins." + coins[coin]["symbol"])
                            module.setup()
                            isAdded = True
                            break
                        else:
                            continue
            except:
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
        print("Remove Wallet")
        print("-" * 50)
        dir = os.listdir(terminal.getPicoPath() + "wallets")
        if (len(dir) == 0):
            print("No Wallets Found")
        else:
            count = 0
            output = []
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
            for line in output:
                print(line)
        print("-" * 50)
        print("Choose An Option (Enter The Number Of Wallet):")
        print("0 - Back")
        if (isInvalid):
            print("Invalid Option")
        option = input("> ")
        if (option == "0"):
            break
        else:
            try:
                option = int(option)
                if (option > len(dir)):
                    isInvalid = True
                    terminal.clear()
                    continue
                else:
                    count = 0
                    for file in dir:
                        count += 1
                        if (count == option):
                            print("-" * 50)
                            print("Are You Sure You Want To Remove This Wallet? (Y/N):")
                            with open(terminal.getPicoPath() + "wallets/" + file, "r") as file:
                                wallet = json.loads(file.read())
                                name = str(wallet["name"])
                                public_adress = wallet["public_adress"]
                                module = importlib.import_module("coins." + name.lower())
                                balance = module.getBalance(public_adress)
                                currency = wallet["currency"]
                            print("Wallet: " + name + " - " + public_adress + " - " + str(balance) + " " + currency)
                            answer = input("> ")
                            answer = answer.lower()
                            if (answer == "y" or answer == "yes"):
                                os.remove(terminal.getPicoPath() + "wallets/" + name + ".keys")
                                print("-" * 50)
                                print("Wallet Removed")
                                print("-" * 50)
                                input("Press Enter To Continue")
                                terminal.clear()
                                break
                            elif (answer == "n" or answer == "no"):
                                print("Wallet Not Removed")
                                continue
                            else:
                                isInvalid = True
                                terminal.clear()
                                continue
                        else:
                            continue
            except:
                isInvalid = True
                terminal.clear()
                continue