#!/usr/bin/env python

# import lots of necessary stuff
import PIL
import screen_test

INKY_IMPRESSION_PALETTE = [57, 48, 57, 255, 255, 255, 58, 91, 70,61, 59, 94, 156, 72, 75, 208, 190, 71,77, 106, 73, 255, 255, 255]

screen_test.update_image()

output_img = screen_test.get_image()

output_img.putpalette(INKY_IMPRESSION_PALETTE)

output_img.save('ping.gif')
