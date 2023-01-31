# Getting Started

For getting started you must have a fully functioning [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) and a Male USB Type-A to Male Micro-USB Cable.

## Preparing The Pico

In this steps we will help you prepare your pico.

1 - Download [CircuitPython from the link](https://circuitpython.org/board/raspberry_pi_pico/) \
2 - Plug in cable thats connected to the Pico into computer while holding BOOTSEL button on the Pico. \
3 - Drag and drop the downloaded .uf2 file into Pico.

> Congrats! You have turned the Pico into a CircuitPython.

4 - If you use a Linux distribution, run the deploy.sh file by entering command: 
```
$ ./deploy.sh
```
This script will copy the files to the Pico. 

5 - If you use Windows, run the deploy.bat (Coming Soon) file by double clicking it.

6 - Pico is now ready to use. You can use the Pico with the Pordo. [Using Pico With The Porod](#using-pico-with-the-pordo)

## Using Pico With The Pordo:

1 - Clone the repository by entering command:
``` 
$ git clone https://github.com/detherminal/seruro.git
```

2 - Change directory to Pordo and run the main file:
```
$ python3 main.py
```

3 - Follow the instructions on the screen.