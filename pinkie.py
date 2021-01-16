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

virus_img = Image.open("/home/pi/pinkie/virus.png")
duck_img = Image.open("/home/pi/pinkie/duck.png")

inky.set_image(duck_img)
inky.show()