import os
from configparser import ConfigParser

ini = ConfigParser()

INKY_IMPRESSION_PALETTE = [57, 48, 57, 255, 255, 255, 58, 91, 70,61, 59, 94, 156, 72, 75, 208, 190, 71,77, 106, 73, 255, 255, 255]


def setup():
    """Read and set up config
    """
    ini_file = os.path.expanduser("~") + "/pinkie.ini"
    ini.read(ini_file)