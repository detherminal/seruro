import terminal
import show

def sendCoins():
    print("Send Coins")
    input("Press Enter To Continue...")

def receiveCoins():
    terminal.clear()
    print("You can receive coins from the user by giving them the adress in the wallets page.")
    input("Press Enter To Continue...")
    terminal.clear()
    show.showAllWalletsAndBalances()
