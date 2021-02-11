#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import screen_default
import os
from configparser import ConfigParser

INKY_IMPRESSION_PALETTE = [57, 48, 57, 255, 255, 255, 58, 91, 70,61, 59, 94, 156, 72, 75, 208, 190, 71,77, 106, 73, 255, 255, 255]

ini_file = os.path.expanduser("~") + "/pinkie.ini"
config = ConfigParser()
config.read(ini_file)

screen_default.setup(server=config['iamaduck']['server'],
                     user=config['iamaduck']['user'],
                     password=config['iamaduck']['password'],
                     allowlist=config['iamaduck']['allowlist'])

screen_default.update_image()

output_img = screen_default.get_image()

output_img.putpalette(INKY_IMPRESSION_PALETTE)

output_img.save('ping.gif')
