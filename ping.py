#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import screen_test
import config


config.setup()
screen_test.setup()

# screen_test.update_pattern()
screen_test.update_blank(config.RED)

output_img = screen_test.get_image()

output_img.putpalette(config.PALETTE)

output_img.save('ping.gif')
