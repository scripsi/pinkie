#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import screen_default
import config

# INKY_IMPRESSION_PALETTE = [57, 48, 57, 255, 255, 255, 58, 91, 70,61, 59, 94, 156, 72, 75, 208, 190, 71,77, 106, 73, 255, 255, 255]

config.setup()
screen_default.setup(server=config.ini['iamaduck']['server'],
                     user=config.ini['iamaduck']['user'],
                     password=config.ini['iamaduck']['password'],
                     allowlist=config.ini['iamaduck']['allowlist'])

screen_default.update_image()

output_img = screen_default.get_image()

output_img.putpalette(config.INKY_IMPRESSION_PALETTE)

output_img.save('ping.gif')
