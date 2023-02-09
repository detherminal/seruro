import terminal
import connect
import show
import wallets
import transfer

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def getChoice(isConnected, isInvalid, isConnectedWarning):
    terminal.clear()
    while True:
        pordo = """
     ____               _       
    |  _ \ ___  _ __ __| | ___  
    | |_) / _ \| '__/ _` |/ _ \ 
    |  __/ (_) | | | (_| | (_) |
    |_|   \___/|_|  \__,_|\___/             
        """
        print(pordo)
        print("-" * 50)
        print("Main Menu")
        if (isConnected):
            print("Connection Status: Connected")
        else:
            print("Connection Status: Disconnected")
        print("-" * 50)
        print("Choose An Option (Enter The Number Of Option):")
        print("1 - Connect To Pico")
        print("2 - Show All Wallets And Balances")
        print("3 - Add Or Remove Wallets")
        print("4 - Send Coins")
        print("5 - Receive Coins")
        print("0 - Exit")
        if (isInvalid):
            print("Invalid Option!")
        elif (isConnectedWarning):
            print("Pico Not Connected!")
        option = input("> ")
        try:
            option = int(option)
            break
        except:
            terminal.clear()
            isInvalid = True
            continue
    return option

def main():
    terminal.clear() 
    terminal.restartPico()
    isConnected = False
    isInvalid = False
    isConnectedWarning = False
    while True:
        choice = getChoice(isConnected, isInvalid, isConnectedWarning)
        if (choice == 1):
            isInvalid == False
            isConnected = connect.connectToPico()
        elif (choice == 2):
            if (isConnected == False):
                isConnectedWarning = True
                isInvalid == False
                continue
            else:
                isConnectedWarning = False
                isInvalid == False
                show.showAllWalletsAndBalances()
        elif (choice == 3):
            if (isConnected == False):
                isConnectedWarning = True
                isInvalid == False
                continue
            else:
                isConnectedWarning = False
                isInvalid == False
                wallets.addOrRemoveWalletMenu()
        elif (choice == 4):
            if (isConnected == False):
                isConnectedWarning = True
                isInvalid == False
                continue
            else:
                isConnectedWarning = False
                isInvalid == False
                transfer.sendCoins()
            continue
        elif (choice == 5):
            if (isConnected == False):
                isConnectedWarning = True
                isInvalid == False
                continue
            else:
                isConnectedWarning = False
                isInvalid == False
                transfer.receiveCoins()
            continue
        elif (choice == 0):
            print("Exiting...")
            exit()
        else:
            isInvalid = True
            continue

if __name__ == '__main__':
    main()