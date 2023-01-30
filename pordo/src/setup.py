import terminal
import json
import coins.eth as eth

def setup():
    isInvalid = False
    terminal.clear()
    while True:
        print("Setup")
        print("-" * 50)
        print("Choose A Blockchain (Enter The Number Of Option): ")
        with open("coins.json", "r") as blockchains:
            blockchains = json.load(blockchains)
            coins = blockchains["coins"]
            count = 0
            for coin in coins:
                count += 1
                print(str(count) + " - " + coins[coin]["name"])
        if (isInvalid):
            print("Invalid Option")
        answer = input("> ")
        if (answer == "1"):
            eth.setup()
            break
        terminal.clear()
        isInvalid = True
        continue

