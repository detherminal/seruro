import os
import json

def saveToPico(key, public_adress, name):
    user = os.getlogin()
    with open("/run/media/" + user + "/CIRCUITPY/wallets/" + name + ".keys", "w") as file:
        wallet = {
            "name": name.capitalize(),
            "encrypted_private_key": key,
            "public_adress": public_adress
        }
        file.write(json.dumps(wallet))
        file.close()