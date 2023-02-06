import os
import json
import terminal
import subprocess

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def saveToPico(key, public_adress, name, currency):
    wallet = {
        "name": name.capitalize(),
        "encrypted_private_key": key,
        "public_adress": public_adress,
        "currency": currency
    }
    data = json.dumps(wallet)
    with open(name + ".keys", "w") as wallet:
        wallet.write(data)
    subprocess.run("sudo rshell --quiet cp ./" + name + ".keys /seruro/wallets/" + name + ".keys", shell=True)
    with open(name + ".keys", "w") as wallet:
        wallet.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") # This is to make sure that the key is not stored on the computer
    os.remove(name + ".keys")
    input("Press Enter To Continue...")
