import terminal
from web3 import Web3
import encrypt
import save
import json
import subprocess
import os

# Copyright (c) seruro
# Author: detherminal
# This file is part of pordo, and is released under the "MIT License Agreement". Please see the LICENSE file that should have been included as part of this package.

def create_wallet():
    terminal.clear()
    web3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com/"))
    print("Create Wallet")
    print("-" * 50)
    print("Creating Wallet...")
    private_key = web3.eth.account.create()._private_key.hex()
    print("Wallet Created")
    print("CAUTION: Do not lose your private key or you will lose access to your wallet!")
    print("Private Key: " + str(private_key))
    public_adress = web3.eth.account.from_key(private_key).address
    print("Public Address: " + str(public_adress))
    input("Press Enter to continue...")
    print("-" * 50)
    print("Please Enter Password To Encrypt Private Key: ")
    print("CAUTION: This password will be used to encrypt your private key and will be asked everytime you need to make a transaction, do not lose your password or you will lose access to your wallet!")
    password = input("> ")
    print("Encrypting Private Key...")
    encrypted_private_key = encrypt.AESEncrypt(password, private_key)
    print("Private Key Encrypted")
    private_key = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" # Clear Private Key From Memory
    save.saveToPico(encrypted_private_key, public_adress, "eth" , "Ether", getBalance(public_adress))
    print("Private Key Saved To Pico")

def import_wallet():
    terminal.clear()
    print("Import Wallet")
    print("-" * 50)
    print("CAUTION: Do not lose your private key or you will lose access to your wallet!")
    print("Please Enter Your Private Key: ")
    private_key = input("> ")
    public_adress = Web3(Web3.HTTPProvider("https://cloudflare-eth.com/")).eth.account.from_key(private_key).address
    print("Public Address: " + str(public_adress))
    print("-" * 50)
    print("Please Enter Password To Encrypt Private Key: ")
    print("CAUTION: This password will be used to encrypt your private key and will be asked everytime you need to make a transaction, do not lose your password or you will lose access to your wallet!")
    password = input("> ")
    print("Encrypting Private Key...")
    encrypted_private_key = encrypt.AESEncrypt(password, private_key)
    print("Private Key Encrypted")
    private_key = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" # Clear Private Key From Memory
    save.saveToPico(encrypted_private_key, public_adress, "eth" , "Ether", getBalance(public_adress))
    print("Private Key Saved To Pico")

def getBalance(public_adress):
    web3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com/"))
    return web3.from_wei(web3.eth.get_balance(public_adress), "ether")

def setup():
    isInvalid = False
    terminal.clear() 
    while True:
        print("Ethereum Wallet Setup")
        print("-" * 50)
        print("1 - Create Wallet")
        print("2 - Import Wallet")
        print("0 - Exit")
        if isInvalid:
            print("Invalid Choice")
        print("Please Enter Your Choice: ")
        choice = input("> ")
        if choice == "1":
            create_wallet()
            break
        elif choice == "2":
            import_wallet()
            break
        elif choice == "0":
            exit()
        else:
            isInvalid = True
            terminal.clear()
            continue

def sendCoins(public_adress, recipient, amount, password):
    web3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com/"))
    output = subprocess.check_output("sudo rshell --quiet cat /seruro/wallets/eth.keys", shell=True)
    file = json.load(output)
    encrypted_private_key = file["encrypted_private_key"]
    private_key = encrypt.AESDecrypt(password, encrypted_private_key)
    nonce = web3.eth.getTransactionCount(public_adress)
    tx = {
        "nonce": nonce,
        "to": recipient,
        "value": web3.toWei(amount, "ether"),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    }
    tx_json = json.dumps(tx)
    with open("eth.tx", "w") as tx_file:
        tx_file.write(tx_json)
    os.system("sudo rshell --quiet cp eth.tx /seruro/eth.tx")
    while True:
        print("Please Confirm Transaction On Your Pico")
        output = subprocess.check_output("sudo rshell --quiet ls -l /seruro/", shell=True)
        if "signed_tx.json" in output:
            break
        else:
            continue
    os.system("sudo rshell --quiet cp /seruro/eth.signed_tx ./eth.signed_tx")
    with open("eth.signed_tx", "r") as signed_tx_file:
        signed_tx = signed_tx_file.read()
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print("Transaction Sent")
    input("Press Enter To Continue...")