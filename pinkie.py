#!/usr/bin/env python

# import lots of necessary stuff
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime, timedelta
import schedule
import re
import random
import pandas as pd
from inky.inky_uc8159 import Inky
from gpiozero import Button
from signal import pause

print("""PinKIE

Displaying the world in the Kitchen

""")

inky = Inky()
button_a = Button(5)
button_b = Button(6)
button_c = Button(16)
button_d = Button(24)

img = Image.open("/home/pi/pinkie/background.png")
draw = ImageDraw.Draw(img)

virus_img = Image.open("/home/pi/pinkie/virus.png")
duck_img = Image.open("/home/pi/pinkie/duck.png")

def show_image(image_to_show):
    x = random.randint(0, inky.WIDTH-51)
    y = random.randint(0, inky.HEIGHT-51)
    img.paste(image_to_show,(x,y))
    inky.set_image(img)
    inky.show()

def show_virus():
    show_image(virus_img)

def show_duck():
    show_image(duck_img)

button_a.when_released = show_virus
button_b.when_released = show_duck

pause()
