'''

'''
from scripting import *

# get a CityEngine instance
ce = CE()





shapes = ce.getObjectsFrom(ce.scene, ce.isShape)

print len(shapes)
