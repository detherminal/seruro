import terminal
import show
import json
import os
import importlib

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def sendCoins():
    isInvalid = False
    while True:
        terminal.clear()
        print("Send Coins")
        print("-" * 50)
        print("Please Choose A Wallet To Send Coins From:")
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
                            with open(terminal.getPicoPath() + "wallets/" + file, "r") as file:
                                wallet = json.loads(file.read())
                                name = str(wallet["name"])
                                public_adress = wallet["public_adress"]
                                module = importlib.import_module("coins." + name.lower())
                                balance = module.getBalance(public_adress)
                                currency = wallet["currency"]
                                terminal.clear()
                                print("Send Coins")
                                print("-" * 50)
                                print("Wallet: " + name)
                                print("Public Adress: " + public_adress)
                                print("Balance: " + str(balance) + " " + currency)
                                print("-" * 50)
                                print("Please Enter The Public Adress Of The Recipient:")
                                recipient = input("> ")
                                print("-" * 50)
                                print("Please Enter The Amount Of Coins To Send In Currency (ex: 0.1): ")
                                amount = input("> ")
                                print("-" * 50)
                                print("Please Enter Your Password: ")
                                password = input("> ")
                                print("-" * 50)
                                print("Sending...")
                                module.sendCoins(public_adress, recipient, amount, password)
                                print("Sent!")
                                input("Press Enter To Continue...")
                                break
            except:
                isInvalid = True
                continue


def receiveCoins():
    terminal.clear()
    print("You can receive coins from the user by giving them the adress in the wallets page.")
    input("Press Enter To Continue...")
    terminal.clear()
    show.showAllWalletsAndBalances()
