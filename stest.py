#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import config
import time
from inky.inky_uc8159 import Inky
from gpiozero import Button
from signal import pause
import screen_test
import os
import itertools
from configparser import ConfigParser

print("""PinKIE

Displaying the world in the Kitchen

""")

inky = Inky()
button_a = Button(5)
button_b = Button(6)
button_c = Button(16)
button_d = Button(24)

colours = [config.WHITE,
           config.YELLOW,
           config.ORANGE,
           config.GREEN,
           config.BLUE,
           config.RED,
           config.BLACK,
           config.CLEAN]

colours_iter = itertools.cycle(colours)

def show_pattern():
    screen_test.update_pattern()
    inky.set_image(screen_test.get_image())
    inky.show()


def show_blank():
    screen_test.update_blank(next(colours_iter))
    inky.set_image(screen_test.get_image())
    inky.show()

def show_clean():
    screen_test.update_blank(config.CLEAN)
    inky.set_image(screen_test.get_image())
    inky.show()

def show_white():
    screen_test.update_blank(config.WHITE)
    inky.set_image(screen_test.get_image())
    inky.show()

button_a.when_released = show_pattern
button_b.when_released = show_blank
button_c.when_released = show_clean
button_d.when_released = show_white

config.setup()
screen_test.setup()
show_pattern()

while True:
    pause()
