import terminal
import config
import wallets

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def setup():
    terminal.clear()
    print("Setup")
    print("-" * 50)
    print("Configuring Pico...")
    config.initialConfig()

