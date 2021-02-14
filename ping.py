#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import screen_default
import config


config.setup()
screen_default.setup()

screen_default.update_image()

output_img = screen_default.get_image()

output_img.putpalette(config.PALETTE)

output_img.save('ping.gif')
