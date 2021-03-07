# import lots of necessary stuff
import config
from PIL import Image,ImageDraw,ImageFont
import random
import math
import itertools

img = Image.new(mode='P',size=(config.WIDTH,config.HEIGHT), color=config.WHITE)
img_draw = ImageDraw.Draw(img)

colours = [(config.WHITE,"W"),
           (config.YELLOW,"Y"),
           (config.ORANGE,"O"),
           (config.GREEN,"G"),
           (config.BLUE,"B"),
           (config.RED,"R"),
           (config.BLACK,"K"),
           (config.CLEAN,"C")]

dc = dict(colours)

def setup():
    """Initialises values
    """

    return

def get_image():
    """Returns an image to be displayed on the screen
    """

    return img

def update_pattern():
    """Creates a test pattern image in preparation for display
    """

    info_font = ImageFont.truetype("fonts/FredokaOne/FredokaOne-Regular.ttf",18)
    img_draw.rectangle([0,0,config.WIDTH,config.HEIGHT],fill=config.BLACK)
    dx = math.floor((config.WIDTH - 40)/8)
    dy = math.floor((config.HEIGHT - 40)/8)
    for bg,bi in colours:
        img_draw.text([bg*dx+(dx/2)+10,1],bi,font=info_font,fill=config.WHITE)
        img_draw.text([bg*dx+(dx/2)+10,config.HEIGHT-19],bi,font=info_font,fill=config.WHITE)
        for fg,fi in colours:
            img_draw.rectangle([bg*dx+20,fg*dy+20,bg*dx+dx+20,fg*dy+dy+20],fill=bg)
            img_draw.line([bg*dx+25,fg*dy+25,bg*dx+dx+15,fg*dy+dy+15],fill=fg,width=5)
            if bg == 1:
                img_draw.text([1,fg*dy+(dy/2)+15],fi,font=info_font,fill=config.WHITE)
                img_draw.text([config.WIDTH-19,fg*dy+(dy/2)+15],fi,font=info_font,fill=config.WHITE)

def update_blank(fill_colour):
    """Creates a test blank image in preparation for display
    """

    info_font = ImageFont.truetype("fonts/FredokaOne/FredokaOne-Regular.ttf",18)
    img_draw.rectangle([0,0,config.WIDTH,config.HEIGHT],fill=config.BLACK)
    dx = math.floor((config.WIDTH - 40)/8)
    dy = math.floor((config.HEIGHT - 40)/8)
    i = dc[fill_colour]
    img_draw.text([1,1],i,font=info_font,fill=config.WHITE)
    img_draw.text([1,config.HEIGHT-19],i,font=info_font,fill=config.WHITE)
    img_draw.text([config.WIDTH-19,1],i,font=info_font,fill=config.WHITE)
    img_draw.text([config.WIDTH-19,config.HEIGHT-19],i,font=info_font,fill=config.WHITE)
    for bg,bi in colours:
        img_draw.text([bg*dx+(dx/2)+10,1],bi,font=info_font,fill=config.WHITE)
        img_draw.text([bg*dx+(dx/2)+10,config.HEIGHT-19],bi,font=info_font,fill=config.WHITE)
        for fg,fi in colours:
            if bg == 1:
                img_draw.text([1,fg*dy+(dy/2)+15],fi,font=info_font,fill=config.WHITE)
                img_draw.text([config.WIDTH-19,fg*dy+(dy/2)+15],fi,font=info_font,fill=config.WHITE)
    img_draw.rectangle([20,20,config.WIDTH-20,config.HEIGHT-20],fill=fill_colour)

