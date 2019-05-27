# Circuit python

Demo project for making a ledstrip lamp

## Components

- NeoPixel Digital RGB LED Strip - Black 30 LED [ADA1460]
- Adafruit ItsyBitsy M0 Express - for CircuitPython & Arduino IDE [ADA3727] (special LL5V Pin for driving the led strip)

## Connections

white -> GND
red -> USB
blue -> 7
green -> 5

## Code

Rename `ledanimations_v1.py` to `main.py` and put it in the root of the ItsyBitsy M0.
`main.py` is the default demo file.

## Library

In the folder, there is a lib folder which should also present on the root of the ItsyBitsy M0.
In case of a bad power connection, this folder sometimes disappears. 
Simply put it back together with the main.py file and everything should work again.
