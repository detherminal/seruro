import os
import subprocess

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def clear():
    # WARNING: USED SO MUCH, BE CAREFUL WHEN CHANGING
    os.system('cls' if os.name == 'nt' else 'clear')

def restartPico():
    subprocess.run("sudo mpremote exec 'machine.reset()'", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)