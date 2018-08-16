
import sys
from os import environ
from os import getcwd
import string

sys.path.append(environ["PYTHON_MODULE_PATH"])


import CompuCellSetup


sim,simthread = CompuCellSetup.getCoreSimulationObjects()
        
# add extra attributes here
        
CompuCellSetup.initializeSimulationObjects(sim,simthread)
# Definitions of additional Python-managed fields go here
        
#Add Python steppables here
steppableRegistry=CompuCellSetup.getSteppableRegistry()
        
from HaptotaxisTest2DSteppables import HaptotaxisTest2DSteppable
steppableInstance=HaptotaxisTest2DSteppable(sim,_frequency=1)
steppableRegistry.registerSteppable(steppableInstance)
        

#*******************FIBER CONCENTRATINON CASES STUDY*************************

from HaptotaxisTest2DSteppables import FiberConcentrationCaseARandom50
instanceOfFiberConcentrationCaseARandom50=FiberConcentrationCaseARandom50(_simulator=sim,_frequency=1)
steppableRegistry.registerSteppable(instanceOfFiberConcentrationCaseARandom50)

#from HaptotaxisTest2DSteppables import FiberConcentrationCaseAUniform50
#instanceOfFiberConcentrationCaseAUniform50=FiberConcentrationCaseAUniform50(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(instanceOfFiberConcentrationCaseAUniform50)

#from HaptotaxisTest2DSteppables import FiberConcentrationCaseBRandom25
#instanceOfFiberConcentrationCaseBRandom25=FiberConcentrationCaseBRandom25(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(instanceOfFiberConcentrationCaseBRandom25)

#from HaptotaxisTest2DSteppables import FiberConcentrationCaseBRandom50
#instanceOfFiberConcentrationCaseBRandom50=FiberConcentrationCaseBRandom50(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(instanceOfFiberConcentrationCaseBRandom50)

#from HaptotaxisTest2DSteppables import FiberConcentrationCaseBRandom75
#instanceOfFiberConcentrationCaseBRandom75=FiberConcentrationCaseBRandom75(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(instanceOfFiberConcentrationCaseBRandom75)

#from HaptotaxisTest2DSteppables import FiberConcentrationCaseCUniform25
#instanceOfFiberConcentrationCaseCUniform25=FiberConcentrationCaseCUniform25(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(instanceOfFiberConcentrationCaseCUniform25)

#from HaptotaxisTest2DSteppables import FiberConcentrationCaseCUniform75
#instanceOfFiberConcentrationCaseCUniform75=FiberConcentrationCaseCUniform75(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(instanceOfFiberConcentrationCaseCUniform75)

#*******************FIBER CONCENTRATINON CASES STUDY*************************

from HaptotaxisTest2DSteppables import LogData
instanceOfLogData=LogData(_simulator=sim,_frequency=100)
steppableRegistry.registerSteppable(instanceOfLogData)

#from HaptotaxisTest2DSteppables import ChemotaxisTest
#instanceOfChemotaxisTest=ChemotaxisTest(_simulator=sim,_frequency=1)
#steppableRegistry.registerSteppable(instanceOfChemotaxisTest)

CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)
        
        
