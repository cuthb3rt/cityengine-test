'''

'''
from scripting import *

# get a CityEngine instance



ce = CE()

def sampleSelect(layerName, attrName, value):
    shapes = ce.getObjectsFrom(ce.scene, ce.isShape)
    list = []
    for s in shapes:
        samplePos =  ce.getPosition(s)
        
        mappingLayer = ce.getObjectsFrom(ce.scene, ce.withName("'" + layerName + "'"))[0]

        if ce.sampleFloatLayerAttribute(mappingLayer, attrName, samplePos[0], samplePos[2]) >= value :
            list.append(s)
    ce.setSelection(list)



if __name__ == '__main__':
    sampleSelect("Mapping 1", "heiVal",0.5)
    pass

