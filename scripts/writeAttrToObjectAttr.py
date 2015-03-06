'''

'''


from scripting import *

# Get a CityEngine instance
ce = CE()

# Called for each shape after generation.
def finishModel(exportContextUUID, shapeUUID, modelUUID):
    ctx = ScriptExportModelSettings(exportContextUUID)
    shape = Shape(shapeUUID)
    model = Model(modelUUID)

    reports = model.getReports()
    
    reportArrayArea = reports['area']
    reportArrayexpVal1 = reports['expVal1']
    reportArrayexpVal2 = reports['expVal2']
    
    ce.setAttribute(shape, "area", reportArrayArea[0])
    ce.setAttribute(shape, "expVal1", reportArrayexpVal1[0])
    ce.setAttribute(shape, "expVal2", reportArrayexpVal2[0])
