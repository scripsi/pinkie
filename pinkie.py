#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import schedule
import time
from inky.inky_uc8159 import Inky
from gpiozero import Button
from signal import pause
import screen_default
import os
from configparser import ConfigParser

print("""PinKIE

Displaying the world in the Kitchen

""")

inky = Inky()
button_a = Button(5)
button_b = Button(6)
button_c = Button(16)
button_d = Button(24)

ini_file = os.path.expanduser("~") + "/pinkie.ini"
config = ConfigParser()
config.read(ini_file)

def show_image(image_to_show):

    if image_to_show == "default":
        screen_default.update_image()
        inky.set_image(screen_default.get_image())
        inky.show()

def show_default():
    show_image("default")


button_a.when_released = show_default
button_b.when_released = show_default
button_c.when_released = show_default
button_d.when_released = show_default

screen_default.setup(server=config['iamaduck']['server'],
                     user=config['iamaduck']['user'],
                     password=config['iamaduck']['password'],
                     allowlist=config['iamaduck']['allowlist'])
show_default()
schedule.every(5).minutes.do(show_default)

while True:
    schedule.run_pending()
    time.sleep(1)
