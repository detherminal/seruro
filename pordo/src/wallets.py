import terminal
import coins.eth as eth
import config
import json

def addOrRemoveWalletMenu():
    print("Add Or Remove Wallet")

def addWallet():
    isInvalid = False
    terminal.clear()
    while True:
        print("Wallet Setup")
        print("-" * 50)
        print("Choose A Blockchain (Enter The Number Of Option): ")
        with open("coins.json", "r") as blockchains:
            blockchains = json.load(blockchains)
            coins = blockchains["coins"]
            count = 0
            for coin in coins:
                count += 1
                print(str(count) + " - " + coins[coin]["name"])
            print("0 - Exit")
        if (isInvalid):
            print("Invalid Option")
        answer = input("> ")
        if (answer == "1"):
            eth.setup()
            config.addCoin("eth")
            break
        elif (answer == "0"):
            break
        terminal.clear()
        isInvalid = True
        continue


def removeWallet():
    isInvalid = False
    terminal.clear()
    while True:
        print("Remove Wallet")
        print("-" * 50)

