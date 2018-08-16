from PySteppables import *
import CompuCell
import sys
import random 


from PlayerPython import *
import CompuCellSetup
from math import *
import numpy as np
from random import uniform

class HaptotaxisTest2DSteppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        # any code in the start function runs before MCS=0
        pass
    def step(self,mcs):        
        pass
        
                     
class FiberConcentrationCaseARandom50(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():   
            field_fiber[x,y,z]  = random.uniform(0, 1)
            field_fiber_cl[x,y,z]  = 0
                
    def step(self,mcs):
        fiber_concentration     = 0
        fiber_cl_concentration = 0  
        
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():
            fiber_concentration     += field_fiber[x,y,z]
            fiber_cl_concentration += field_fiber_cl[x,y,z]
                    
        fileName='CaseA_Random_50.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", fiber_concentration,",", fiber_cl_concentration
        fileHandle.close()
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
    
class FiberConcentrationCaseAUniform50(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        #****Average 0.5 everywhere:
        #for x,y,z in self.everyPixel():  
        #    field_fiber[x,y,z]  = 0.5
        #    field_fiber_cl[x,y,z]  = 0
        
        #****Half  0 Half 1
        for x,y,z in self.everyPixel():  
            if x >=150: 
                field_fiber[x,y,z]  = 1
                field_fiber_cl[x,y,z]  = 0
            else:
                field_fiber[x,y,z]  = 0
                field_fiber_cl[x,y,z]  = 0
                
    def step(self,mcs):
        fiber_concentration     = 0
        fiber_cl_concentration = 0  
        
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():
            fiber_concentration     += field_fiber[x,y,z]
            fiber_cl_concentration += field_fiber_cl[x,y,z]
                
      
                    
        fileName='CaseA_Uniform_50.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", fiber_concentration,",", fiber_cl_concentration
        fileHandle.close()
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
    
class FiberConcentrationCaseBRandom25(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():   
            field_fiber[x,y,z]  = random.uniform(0, 0.5)
            field_fiber_cl[x,y,z]  = 0
                
    def step(self,mcs):
        fiber_concentration     = 0
        fiber_cl_concentration = 0  
        
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():
            fiber_concentration     += field_fiber[x,y,z]
            fiber_cl_concentration += field_fiber_cl[x,y,z]
                    
        fileName='CaseB_Random_25.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", fiber_concentration,",", fiber_cl_concentration
        fileHandle.close()
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
    
class FiberConcentrationCaseBRandom50(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():   
            field_fiber[x,y,z]  = random.uniform(0.25, 0.75)
            field_fiber_cl[x,y,z]  = 0
                
    def step(self,mcs):
        fiber_concentration     = 0
        fiber_cl_concentration = 0  
        
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():
            fiber_concentration     += field_fiber[x,y,z]
            fiber_cl_concentration += field_fiber_cl[x,y,z]
                    
        fileName='CaseB_Random_50.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", fiber_concentration,",", fiber_cl_concentration
        fileHandle.close()
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
  
class FiberConcentrationCaseBRandom75(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():   
            field_fiber[x,y,z]  = random.uniform(0.5,1)
            field_fiber_cl[x,y,z]  = 0
                
    def step(self,mcs):
        fiber_concentration     = 0
        fiber_cl_concentration = 0  
        
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():
            fiber_concentration     += field_fiber[x,y,z]
            fiber_cl_concentration += field_fiber_cl[x,y,z]
                    
        fileName='CaseB_Random_75.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", fiber_concentration,",", fiber_cl_concentration
        fileHandle.close()
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
  

class FiberConcentrationCaseCUniform25(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        #****Average 0.25 everywhere:
        for x,y,z in self.everyPixel():  
            field_fiber[x,y,z]  = 0.25
            field_fiber_cl[x,y,z]  = 0
        
        #****Half  0 Half 1
        #for x,y,z in self.everyPixel():  
         #   if x >=150: 
         #       field_fiber[x,y,z]  = 0.5
         #       field_fiber_cl[x,y,z]  = 0
         #   else:
         #       field_fiber[x,y,z]  = 0
         #       field_fiber_cl[x,y,z]  = 0
                
    def step(self,mcs):
        fiber_concentration     = 0
        fiber_cl_concentration = 0  
        
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():
            fiber_concentration     += field_fiber[x,y,z]
            fiber_cl_concentration += field_fiber_cl[x,y,z]
                
      
                    
        fileName='CaseC_Uniform_25.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", fiber_concentration,",", fiber_cl_concentration
        fileHandle.close()
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return


class FiberConcentrationCaseCUniform75(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        #****Average 0.25 everywhere:
        for x,y,z in self.everyPixel():  
            field_fiber[x,y,z]  = 0.75
            field_fiber_cl[x,y,z]  = 0
        
        #****Half  0 Half 1
        #for x,y,z in self.everyPixel():  
         #   if x >=150: 
         #       field_fiber[x,y,z]  = 1
         #       field_fiber_cl[x,y,z]  = 0
         #   else:
         #       field_fiber[x,y,z]  = 0.5
         #       field_fiber_cl[x,y,z]  = 0
                
    def step(self,mcs):
        fiber_concentration     = 0
        fiber_cl_concentration = 0  
        
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
        for x,y,z in self.everyPixel():
            fiber_concentration     += field_fiber[x,y,z]
            fiber_cl_concentration += field_fiber_cl[x,y,z]
                                   
        fileName='CaseC_Uniform_75.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", fiber_concentration,",", fiber_cl_concentration
        fileHandle.close()
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
    

class LogData(SteppableBasePy):
    def __init__(self,_simulator,_frequency=10):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):   
        IDCount = 1

        for cell in self.cellListByType(1):
            cell_attribute=self.getDictionaryAttribute(cell)
                
            # Way to count the amount of generalized cells for a given cell type 
            cell_attribute["id"] = IDCount 
            IDCount += 1
       
    def step(self,mcs):
        
        #*****For every cell_ID of the same cell type, log cell position in term of xCOM and yCOM
        for cell in self.cellListByType(1):
            cell_attribute=self.getDictionaryAttribute(cell)

            #Log data into multiple separate cvs file by cell_ID                      
            #fileName='CellPosition_COM_'+str(cell_attribute["id"])+'.csv'

            #Log all data into one cvs file
            fileName='CellPosition_COM.csv'
            
            try:
                fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
            except IOError:
                print "Could not open file ", fileName," for writing. "
                return
            
            cell_attribute=self.getDictionaryAttribute(cell)
            print >>fileHandle,cell.id,",",mcs,",",cell.xCOM,",",cell.yCOM
            fileHandle.close()
            
        #******Log MMP and LOX Concentration 
        MMP = 0
        fieldMMP=self.getConcentrationField("MMP")
        for x in xrange(self.dim.x):             
            for y in xrange(self.dim.y):                 
                for z in xrange(self.dim.z): 
                    MMP += fieldMMP[x,y,z];
                    
        fileName='MMP_LOX.csv'
        try:
            fileHandle,fullFileName=self.openFileInSimulationOutputDirectory(fileName,"a")
        except IOError:
            print "Could not open file ", fileName," for writing. "
            return
            
        print >>fileHandle,mcs,",", MMP
        fileHandle.close()    
            
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
    
class ChemotaxisTest(SteppableBasePy):
    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
        field_fiber      = self.getConcentrationField("fiber")
        field_fiber_cl = self.getConcentrationField('fiber_cl')
        
         #for x,y,z in self.everyPixel():  
         #   field_fiber[x,y,z]  = 0.5
         #   field_fiber_cl[x,y,z]  = 0

        # The half uncrosslink and half crosslink test
        for x,y,z in self.everyPixel():  
            if x >=150:
                #field_fiber[x,y,z]  = random.uniform(0,1)
                field_fiber[x,y,z]  = 0.5
                field_fiber_cl[x,y,z]  = 0
            else:
                field_fiber[x,y,z]  = 0
                #field_fiber_cl[x,y,z]  = random.uniform(0,1)
                field_fiber_cl[x,y,z]  = 0.5
                
    def step(self,mcs):
        pass
                           
    def finish(self):
        # this function may be called at the end of simulation - used very infrequently though
        return
    
