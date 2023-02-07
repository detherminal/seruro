# Getting Started

For getting started you must have a fully functioning [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) and a [Waveshare 1.3inch LCD Display](https://www.waveshare.com/pico-lcd-1.3.htm). If you only have a Pico, you can use the wallet as a view-only wallet (You can't sign transactions so you can't send any coins.)

## Preparing The Pico

In this steps we will help you prepare your pico.

1 - Download [MicroPython from the link](https://micropython.org/download/)
> Note: Please download the firmware for your Pico or Pico-W

2 - Plug in cable thats connected to the Pico into computer while holding BOOTSEL button on the Pico. 

3 - Drag and drop the downloaded .uf2 file into Pico.

> Congrats! You have turned the Pico into a MicroPython.

4 - Run the following code to upload the code to Pico:
```bash
$ bash deploy.sh
```

5 - Pico is now ready to use. You can use the Pico with the Pordo. [Using Pico With The Pordo](#using-pico-with-the-pordo)

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