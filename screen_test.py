# import lots of necessary stuff
from PIL import Image,ImageDraw,ImageFont
import random
import math

BLACK = 0
WHITE = 1
GREEN = 2
BLUE = 3
RED = 4
YELLOW = 5
ORANGE = 6
CLEAN = 7

WIDTH = 600
HEIGHT = 448

img = Image.new(mode='P',size=(WIDTH,HEIGHT), color=WHITE)
img_draw = ImageDraw.Draw(img)

fonts = ["fonts/Action_Man_Bold/Action_Man_Bold.ttf",
         "fonts/FredokaOne-Regular/FredokaOne-Regular.ttf",
         "fonts/Lobster-Regular/Lobster-Regular.ttf",
         "fonts/Pacifico-Regular/Pacifico-Regular.ttf",
         "fonts/SpecialElite-Regular/SpecialElite-Regular.ttf",
         "fonts/LondrinaSolid-Regular/LondrinaSolid-Regular.ttf",
         "fonts/RobotoSlab-Bold/RobotoSlab-Bold.ttf"]


def get_image():
    """Returns an image to be displayed on the screen
    """

    return img

def update_image():
    """Updates the image in preparation for display
    """
    w = (WIDTH/8)
    h = (HEIGHT /8)
    for fg in range(8):
        for bg in range(8):
            font = random.choice(fonts)
            x = fg * (WIDTH/8)
            y = bg * (HEIGHT /8)
            img_draw.rectangle((x,y,x+w,y+h),fill=bg)
            output_font = ImageFont.truetype(font, 50)
            img_draw.text((x+(w/2),y+(h/2)),"A",fill=fg,font=output_font,anchor="mm",spacing=0,align="center")
