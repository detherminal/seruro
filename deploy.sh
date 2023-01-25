#!/bin/bash

# Copyright (C) 2023 Seruro Project

# This script copies the source code in ./src to Raspberry Pi Pico 
# WARNING: The source code starts running immediately after copying.

cd src
cp -r ./ /run/media/$USER/CIRCUITPY
cd ..