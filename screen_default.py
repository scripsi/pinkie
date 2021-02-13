# import lots of necessary stuff
from PIL import Image,ImageDraw,ImageFont
import random
import math
import imaplib
import email
from email import policy

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

LEADING = 2
MARGIN = 20

REFRESH_INTERVAL=10
UPDATE_INTERVAL=60

img = Image.new(mode='P',size=(WIDTH,HEIGHT), color=WHITE)
img_draw = ImageDraw.Draw(img)

fonts = ["fonts/Action_Man/Action_Man_Bold.ttf",
         "fonts/ArchitectsDaughter/ArchitectsDaughter-Regular.ttf",
         "fonts/FredokaOne/FredokaOne-Regular.ttf",
         "fonts/Lobster/Lobster-Regular.ttf",
         "fonts/LondrinaSolid/LondrinaSolid-Regular.ttf",
         "fonts/Merriweather/Merriweather-Regular.ttf",
         "fonts/Pacifico/Pacifico-Regular.ttf",
         "fonts/Pacifico/Pacifico-Regular.ttf",
         "fonts/RobotoSlab/RobotoSlab-Bold.ttf",
         "fonts/SpecialElite/SpecialElite-Regular.ttf",
         "fonts/StalinistOne/StalinistOne-Regular.ttf",
         "fonts/Ultra/Ultra-Regular.ttf"]

# colour schemes (background,foreground)
colours = [(BLACK,WHITE),(BLACK,YELLOW),(BLACK,ORANGE),
           (WHITE,BLACK),(WHITE,GREEN),(WHITE,BLUE),(WHITE,RED),
           (GREEN,BLACK),(GREEN,WHITE),(GREEN,YELLOW),
           (BLUE,WHITE),(BLUE,YELLOW),(BLUE,ORANGE),
           (RED,WHITE),(RED,YELLOW),(RED,ORANGE),
           (YELLOW,BLACK),(YELLOW,GREEN),(YELLOW,BLUE),(YELLOW,RED),
           (ORANGE,BLACK),(ORANGE,BLUE)]

quacks = []

def setup(server,user,password,allowlist):
    """Initialises values
    """

    try:
        # establish imap connection
        imap = imaplib.IMAP4(server)
        imap.login(user, password)
        imap.select('Inbox',readonly=True)

        # print("Downloading quacks ...")
        for sender in allowlist.split(','):
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
    bg,fg = random.choice(colours)

    fs,q = smoosh_text(quack, font, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    output_font = ImageFont.truetype(font, fs)

    ax, ay, bx, by = img_draw.multiline_textbbox((0,0),q,font=output_font,align="center",spacing=LEADING)
    x = ((WIDTH - (bx - ax)) / 2) - ax
    y = ((HEIGHT - (by - ay)) / 2) - ay
    img_draw.rectangle([0,0,WIDTH,HEIGHT],fill=bg)
    img_draw.multiline_text((x,y),q,fill=fg,font=output_font,spacing=LEADING,align="center")


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