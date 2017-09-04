import os
import sys


def changeCurrentDir(wdAppend):
    origWD = os.getcwd()
    newWD = origWD + wdAppend
    os.chdir(os.path.join(os.path.abspath(sys.path[0]), newWD))
    return os.getcwd() + '/'
