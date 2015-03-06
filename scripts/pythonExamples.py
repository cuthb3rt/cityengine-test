'''
'''
from scripting import *

import time


# get a CityEngine instance
ce = CE()




def printTime():
    timeNow = time.strftime('%X %x %Z')
    print timeNow


def countSelectedShapes():
    sel = ce.selection()
    numberOfObjects = 0
    for object in sel:
        if ce.isShape(object):
            numberOfObjects += 1
    print numberOfObjects


if __name__ == '__main__':
    countSelectedShapes()
