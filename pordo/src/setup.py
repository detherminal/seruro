import terminal
import config
import wallets

def setup():
    terminal.clear()
    print("Setup")
    print("-" * 50)
    print("Configuring Pico...")
    config.initialConfig()
    print("Pico Configured")
    input("Press Enter To Continue Into Adding Wallet...")
    wallets.addWallet()

