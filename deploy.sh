#!/bin/bash

# Copyright (C) 2023 Seruro Project

# This script copies the source code in ./src to Raspberry Pi Pico 
# WARNING: The source code doesn't start the Pico. You have to remove and reinsert the Pico to start the code.r
# This script requires rshell to be installed.

sudo rshell rm -rf /pyboard/* # Remove all files in the Pico.
sudo rshell rm -rf /seruro/* # Remove all files in the Pico.
sudo rshell cp ./src/* /pyboard/ # Copy the source code to the Pico.