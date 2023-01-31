import os
import json

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def initialConfig():
    user = os.getlogin()
    if (os.path.exists("config.json")):
        return
    else:
        with open("/run/media/" + user + "/CIRCUITPY/config.json", "w") as file:
            initialConfig = {
                "isSetup": True,
                "coins": []
            }
            file.write(json.dumps(initialConfig))
            file.close()
    os.mkdir("/run/media/" + user + "/CIRCUITPY/wallets")


def addCoin(coin):
    user = os.getlogin()
    with open("/run/media/" + user + "/CIRCUITPY/config.json", "r") as file:
        config = json.load(file)
        file.close()
    config["coins"].append(coin)
    with open("/run/media/" + user + "/CIRCUITPY/config.json", "w") as file:
        file.write(json.dumps(config))
        file.close()