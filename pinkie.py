#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import schedule
from inky.inky_uc8159 import Inky
from gpiozero import Button
from signal import pause
import screen_default

print("""PinKIE

Displaying the world in the Kitchen

""")

inky = Inky()
button_a = Button(5)
button_b = Button(6)
button_c = Button(16)
button_d = Button(24)

def show_image(image_to_show):

    if image_to_show == "default":
        screen_default.update_image()
        inky.set_image(screen_default.get_image())
        inky.show()

def show_default():
    show_image("default")


button_a.when_released = show_default
# button_b.when_released = show_clear

pause()
