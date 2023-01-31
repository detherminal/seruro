import os
import json
import terminal

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def saveToPico(key, public_adress, name, currency):
    user = os.getlogin()
    with open(terminal.getPicoPath() + "wallets/" + name + ".keys", "w") as file:
        wallet = {
            "name": name.capitalize(),
            "encrypted_private_key": key,
            "public_adress": public_adress,
            "currency": currency
        }
        file.write(json.dumps(wallet))
        file.close()