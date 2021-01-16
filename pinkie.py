#!/usr/bin/env python

# import lots of necessary stuff
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime, timedelta
import re
import random
import pandas as pd
from inky.inky_uc8159 import Inky

print("""PinKIE

Displaying the world in the Kitchen

""")

inky = Inky()

img = Image.open("/home/pi/pinkie/background.png")
draw = ImageDraw.Draw(img)

virus_img = Image.open("/home/pi/pinkie/virus.png")
duck_img = Image.open("/home/pi/pinkie/duck.png")

x = random.randint(0, inky.WIDTH-51)
y = random.randint(0, inky.HEIGHT-51)
img.paste(virus_img,(x,y))
x = random.randint(0, inky.WIDTH-51)
y = random.randint(0, inky.HEIGHT-51)
img.paste(duck_img,(x,y))

inky.set_image(img)
inky.show()