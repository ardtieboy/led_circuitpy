# Itsy Bitsy M0 Express IO demo
# Welcome to CircuitPython 2.2 :)

import board
import gc
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import neopixel
import adafruit_dotstar
from random import randint, getrandbits, uniform

gc.collect()   # make some rooooom

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# NeoPixel strip (of 30 LEDs) connected on D5
NUMPIXELS = 30
neopixels = neopixel.NeoPixel(board.D5, NUMPIXELS, brightness=0.8, auto_write=False)
default_flame = [225, 128, 0]

button = DigitalInOut(board.D7)
button.direction = Direction.INPUT
button.pull = Pull.UP

on_off = DigitalInOut(board.D9)
on_off.direction = Direction.INPUT
on_off.pull = Pull.UP

m = 0
led_modes = ["fire", "seawheel", "firewheel", "discowheel" ,"rainbow", "off"]
current_led_mode = led_modes[m]

######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

def firewheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 128):
        pos -= 128
        return [255, 256+int(pos*2), 0]
    else:
        return [255,512-(pos*2)-1,0]

def seawheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 128):
        pos -= 128
        return [0, 255, 256+int(pos*2)]
    else:
        return [0, 255, 512-(pos*2)-1]

def discowheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 128):
        pos -= 128
        return [255, 0, 256+int(pos*2)]
    else:
        return [255, 0, 512-(pos*2)-1]

def get_new_mode(m, max):
    return (m + 1) % max

def fire(pos):
    flicker = randint(-55,55)
    g = default_flame[1]+flicker
    if(g<0): g =0
    return [255,g,0]


######################### MAIN LOOP ##############################

i = 0
while True:
  print("ping")
  current_led_mode = led_modes[m]
  print(current_led_mode)

  if current_led_mode == "rainbow":
      for p in range(NUMPIXELS):
          idx = int ((p * 256 / NUMPIXELS) + i)
          neopixels[p] = wheel(idx & 255)
      neopixels.show()
  elif current_led_mode == "fire":
      for p in range(NUMPIXELS):
          neopixels[p] = fire(p)
      neopixels.show()
  elif current_led_mode == "firewheel":
      for p in range(NUMPIXELS):
          idx = int ((p * 256 / NUMPIXELS) + i)
          neopixels[p] = firewheel(idx & 255)
      neopixels.show()
  elif current_led_mode == "seawheel":
      for p in range(NUMPIXELS):
          idx = int ((p * 256 / NUMPIXELS) + i)
          neopixels[p] = seawheel(idx & 255)
      neopixels.show()
  elif current_led_mode == "discowheel":
      for p in range(NUMPIXELS):
          idx = int ((p * 256 / NUMPIXELS) + i)
          neopixels[p] = discowheel(idx & 255)
      neopixels.show()
  elif current_led_mode == "off":
      neopixels.fill((0,0,0))
      neopixels.show()

  if not button.value:
      print("Button D7 pressed!", end ="\t")
      m = get_new_mode(m, len(led_modes)-1)
      time.sleep(0.2)

  if not on_off.value:
      print("Button D9 pressed!", end ="\t")
      if m != len(led_modes)-1:
        m = len(led_modes)-1
      else:
        m = 0
      time.sleep(0.2)

  i = (i+1) % 256  # run from 0 to 255
  time.sleep(0.01) # make bigger to slow down

  print("")