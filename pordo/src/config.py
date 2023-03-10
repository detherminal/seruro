import subprocess
import json
import terminal
import os

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def initialConfig():
    initialConfig = {
        "isSetup": True,
        "coins": []
    }
    json_data = json.dumps(initialConfig)
    with open("config.json", "w") as file:
        file.write(json_data)
        file.close()
    subprocess.run("sudo rshell --quiet cp ./config.json /seruro/config.json", shell=True)
    terminal.restartPico()
    os.remove("config.json")