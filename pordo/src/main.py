import os

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def getChoice(isConnected, isInvalid):
    clearTerminal()
    while True:
        print("Pordo")
        print("-" * 10)
        if (isConnected):
            print("Connection Status: Connected")
        else:
            print("Connection Status: Disconnected")
        print("-" * 10)
        print("Choose An Option (Enter The Number Of Option):")
        print("1 - Connect To Pico")
        print("2 - Disconnect From Pico")
        print("3 - Show Wallet Balances")
        print("0 - Exit")
        if (isInvalid):
            print("Invalid Option")
        option = input("> ")
        try:
            option = int(option)
            break
        except:
            clearTerminal()
            isInvalid = True
            continue
    return option

def connectToPico():
    clearTerminal()
    print("Connecting To Pico...")
    input("Press Enter To Return Main Menu...")

def disconnectFromPico():
    clearTerminal()
    print("Disconnecting From Pico...")
    input("Press Enter To Return Main Menu...")

def showWalletBalances():
    clearTerminal()
    print("Showing Wallet Balances...")
    input("Press Enter To Return Main Menu...")

def main():
    clearTerminal() 
    isConnected = False
    isInvalid = False
    while True:
        choice = getChoice(isConnected, isInvalid)
        if (choice == 1):
            connectToPico()
        elif (choice == 2):
            disconnectFromPico()
        elif (choice == 3):
            showWalletBalances()
        elif (choice == 0):
            print("Exiting...")
            exit()
        else:
            isInvalid = True
            continue

if __name__ == '__main__':
    main()