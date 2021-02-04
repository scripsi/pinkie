#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import schedule
from inky.inky_uc8159 import Inky
from gpiozero import Button
from signal import pause
import screen_test

print("""PinKIE

Displaying the world in the Kitchen

""")

inky = Inky()
button_a = Button(5)
button_b = Button(6)
button_c = Button(16)
button_d = Button(24)

def show_image(image_to_show):

    if image_to_show == "test":
        screen_test.update_image()
        inky.set_image(screen_test.get_image())
        inky.show()
    else:
        inky.clear()

def show_test():
    show_image("test")

def show_clear():
    show_image("clear")

button_a.when_released = show_test
button_b.when_released = show_clear

pause()
