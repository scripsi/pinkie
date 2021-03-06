# import lots of necessary stuff
import config
from PIL import Image,ImageDraw,ImageFont
import random
import math
import imaplib
import email
from email import policy
import itertools

LEADING = 2
MARGIN = 20

img = Image.new(mode='P',size=(config.WIDTH,config.HEIGHT), color=config.WHITE)
img_draw = ImageDraw.Draw(img)

fonts = ["fonts/Action_Man/Action_Man_Bold.ttf",
         "fonts/ArchitectsDaughter/ArchitectsDaughter-Regular.ttf",
         "fonts/Bangers/Bangers-Regular.ttf",
         "fonts/ComicNeue/ComicNeue-Bold.ttf",
         "fonts/FredokaOne/FredokaOne-Regular.ttf",
         "fonts/HachiMaruPop/HachiMaruPop-Regular.ttf",
         "fonts/Lobster/Lobster-Regular.ttf",
         "fonts/LondrinaSolid/LondrinaSolid-Regular.ttf",
         "fonts/Merienda/Merienda-Regular.ttf",
         "fonts/Merriweather/Merriweather-Regular.ttf",
         "fonts/Pacifico/Pacifico-Regular.ttf",
         "fonts/Ranchers/Ranchers-Regular.ttf",
         "fonts/RobotoSlab/RobotoSlab-Bold.ttf",
         "fonts/RockSalt/RockSalt-Regular.ttf",
         "fonts/SpecialElite/SpecialElite-Regular.ttf",
         "fonts/StalinistOne/StalinistOne-Regular.ttf",
         "fonts/Ultra/Ultra-Regular.ttf"]

# colour schemes (background,foreground)
colours = [(config.BLACK,config.WHITE,"White on Black"),
           (config.BLACK,config.YELLOW,"Yellow on Black"),
           (config.BLACK,config.ORANGE,"Orange on Black"),
           (config.BLACK,config.GREEN,"Green on Black"),
           (config.BLACK,config.BLUE,"Blue on Black"),
           (config.BLACK,config.RED,"Red on Black"),
           (config.WHITE,config.BLACK,"Black on White"),
           (config.WHITE,config.GREEN,"Green on White"),
           (config.WHITE,config.BLUE,"Blue on White"),
           (config.WHITE,config.RED,"Red on White"),
           (config.WHITE,config.YELLOW,"Yellow on White"),
           (config.WHITE,config.ORANGE,"Orange on White"),
           (config.GREEN,config.WHITE,"White on Green"),
           (config.GREEN,config.YELLOW,"Yellow on Green"),
           (config.GREEN,config.ORANGE,"Orange on Green"),
           (config.GREEN,config.RED,"Red on Green"),
           (config.GREEN,config.BLUE,"Blue on Green"),
           (config.GREEN,config.BLACK,"Black on Green"),
           (config.BLUE,config.WHITE,"White on Blue"),
           (config.BLUE,config.YELLOW,"Yellow on Blue"),
           (config.BLUE,config.ORANGE,"Orange on Blue"),
           (config.BLUE,config.RED,"Red on Blue"),
           (config.BLUE,config.GREEN,"Green on Blue"),
           (config.BLUE,config.BLACK,"Black on Blue"),
           (config.RED,config.WHITE,"White on Red"),
           (config.RED,config.YELLOW,"Yellow on Red"),
           (config.RED,config.ORANGE,"Orange on Red"),
           (config.RED,config.GREEN,"Green on Red"),
           (config.RED,config.BLUE,"Blue on Red"),
           (config.RED,config.BLACK,"Black on Red"),
           (config.YELLOW,config.BLACK,"Black on Yellow"),
           (config.YELLOW,config.GREEN,"Green on Yellow"),
           (config.YELLOW,config.BLUE,"Blue on Yellow"),
           (config.YELLOW,config.RED,"Red on Yellow"),
           (config.YELLOW,config.ORANGE,"Orange on Yellow"),
           (config.YELLOW,config.WHITE,"White on Yellow"),
           (config.ORANGE,config.BLACK,"Black on Orange"),
           (config.ORANGE,config.WHITE,"White on Orange"),
           (config.ORANGE,config.RED,"Red on Orange"),
           (config.ORANGE,config.YELLOW,"Yellow on Orange"),
           (config.ORANGE,config.GREEN,"Green on Orange"),
           (config.ORANGE,config.BLUE,"Blue on Orange")]

colours_iter = itertools.cycle(colours)

last_colours = ""

quacks = []

def setup():
    """Initialises values
    """

    try:
        # establish imap connection
        imap = imaplib.IMAP4(config.ini['screen_default']['server'])
        imap.login(config.ini['screen_default']['user'],
                   config.ini['screen_default']['password'])
        imap.select('Inbox',readonly=True)

        # print("Downloading quacks ...")
        for sender in config.ini['screen_default']['allowlist'].split(','):
            response, msg_nums = imap.search(None, 'FROM', sender)
            for msg_num in msg_nums[0].split():
                response, msg_data = imap.fetch(msg_num, '(BODY.PEEK[HEADER])')
                msg = email.message_from_bytes(msg_data[0][1],policy=policy.default)
                # msg_sender_name, msg_sender_email = email.utils.parseaddr(msg['From'])
                # The following line removes newlines (\r\n) sometimes present in long subjects
                q = ''.join(msg['Subject'].splitlines())
                quacks.append(q)
        imap.close()
        imap.logout()
        # print("... completed")
    except:
        quacks.append("No Quacks")

    # print(quacks)

def get_image():
    """Returns an image to be displayed on the screen
    """

    return img

def update_image():
    """Updates the image in preparation for display
    """

    quack = random.choice(quacks)
    font = random.choice(fonts)
    bg,fg,colours_name = next(colours_iter)

    fs,q = smoosh_text(quack, font, config.WIDTH - (MARGIN * 2), config.HEIGHT - 20 - (MARGIN * 2))
    output_font = ImageFont.truetype(font, fs)

    info_text = colours_name + " after " + last_colours
    last_colours = colours_name
    info_font = ImageFont.truetype("fonts/FredokaOne/FredokaOne-Regular.ttf",18)
    img_draw.rectangle([0,0,config.WIDTH,20],fill=config.WHITE)
    img_draw.text([1,1],info_text,font=info_font,fill=config.BLACK)

    ax, ay, bx, by = img_draw.multiline_textbbox((0,0),q,font=output_font,align="center",spacing=LEADING)
    x = ((config.WIDTH - (bx - ax)) / 2) - ax
    y = ((config.HEIGHT - (by - ay)) / 2) - ay
    img_draw.rectangle([0,20,config.WIDTH,config.HEIGHT-20],fill=bg)
    img_draw.multiline_text((x,y + 20),q,fill=fg,font=output_font,spacing=LEADING,align="center")


def smoosh_text(text, font_name, box_width, box_height):
    """Wraps, centres and shrinks a text string to fit a rectangular image area
    """
    # Create a font instance for testing, at size 100
    test_font = ImageFont.truetype(font_name, 100)
    # Find the width of a space
    ax, ay, bx, by = img_draw.textbbox((0,0),' ',font=test_font,spacing=0)
    space_width = bx - ax
    # split the text into individual words
    words = text.split()
    # Find the biggest words
    # print("Word size optimisation ...")
    word_width_max = 0
    word_height_max = 0
    word_width_total = 0
    for w in words:
        ax, ay, bx, by = img_draw.textbbox((0,0),w,font=test_font,spacing=0)
        w_width = bx - ax
        word_width_total += w_width
        w_height = by - ay
        if w_width > word_width_max:
            word_width_max = w_width
            widest_word = w
        if w_height > word_height_max:
            word_height_max = w_height
            tallest_word = w
    # print("Widest word is: ", widest_word)
    # print("Tallest word is: ", tallest_word)

    # Set the maximum font size so that the biggest words will fit
    font_size = math.floor((box_width / (word_width_max/100)))
    font_size = math.floor(min(font_size, (box_height / (word_height_max/100))))
    # print("First round font size is: ", font_size)

    # Now set the maximum font size so that the total area occupied by the text fits the area available
    # print("Area optimisation ...")
    box_area = box_width * box_height
    unit_text_width = ((len(words)-1) * (space_width / 100)) + (word_width_total / 100)
    unit_line_height = word_height_max / 100
    unit_text_area = unit_text_width * unit_line_height
    font_size = math.floor(min(font_size,math.sqrt(box_area / unit_text_area)))
    # print("Second round font size is: ", font_size)

    # Finally, try and find the maximum font size where the text actually fits
    # print("Line length optimisation ...")
    unfitted = True
    lines = []
    while unfitted:
        # print("Trying font size: ", font_size, "...")
        line_height = (unit_line_height * font_size) + LEADING
        display_font = ImageFont.truetype(font_name, font_size)
        lines.clear()
        line = ''
        for w in words:
            if line == '':
                l = w
            else:
                l = line + ' ' + w
            ax, ay, bx, by = img_draw.textbbox((0,0),l,font=display_font,spacing=0)
            line_width = bx - ax
            if line_width > box_width:
                lines.append(line)
                line = w
            else:
                line = l
        if line != '':
            lines.append(line)
        ax, ay, bx, by = img_draw.multiline_textbbox((0,0),"\n".join(lines),font=display_font,align="center",spacing=LEADING)
        if by - ay > box_height:
            # print("Too big.")
            font_size -= 1
        else:
            # print("It fits!")
            unfitted = False

    # print("Third round font size is: ", font_size)
    # for l in lines:
    #   print(l)

    return font_size, "\n".join(lines)