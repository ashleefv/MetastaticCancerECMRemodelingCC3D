# MetastaticCancerECMRemodelingCC3D
Hybrid discrete-continuum model of ECM remodeling and its impact on metastatic cancer migration

[![DOI](https://zenodo.org/badge/145025121.svg)](https://zenodo.org/badge/latestdoi/145025121)

## Overview
This computational model describes the dynamic process of extracellular matrix remodeling in the vicinity of a primary tumor at the onset 
of metastasis. The system under investigation consists of cancer cells, two populations of collagen fibers,
and two enzymes that react to remodel the microenvironment, impacting cancer cell migration away from the primary tumor. The cancer cells are treated as discrete agents, and ECM components including collagen fibers and remodeling enzymes are modelled by a system of partial differential equations.

## Computational Model for Metastatic Cancer Migration through a Remodeling Extracellular Matrix
### Code Authors
Yen T. Nguyen Edalgo and Ashlee N. Ford Versypt, 
School of Chemical Engineering,
Oklahoma State University.
Corresponding author: A. N. Ford Versypt, ashleefv@okstate.edu

### Related publication for model details
Yen T. Nguyen Edalgo, Anya L. Zornes, and Ashlee N. Ford Versypt, A Hybrid Discrete-Continuous Model of Metastatic Cancer Cell Migration through a Remodeling Extracellular Matrix,
Under review, AIChE Journal, 2019.

### Files

* HaptotaxisTest2D.cc3d

This file includes the nominal case for running the model.

* Simulation folder

This folder includes the python, python steppables, and xml files that can be used to customize settings in the code for each simulation.

### Notes on generating figures

The figures in the manuscript were manually pieced together by collecting a series of output from each run. All of the simulations can be run from the codes provided.

For each condition with the settings provided, simulations are run for 10,000 MCS, and we recommend repeating for 10 runs. For each run, the following outputs are tracked:

1.	The trajectories of all the cancer cells at the initial time when MCS = 0 and at the final time when MCS = 10,000 are logged to a csv text file. These data are then used in the calculation of the cell migration metrics (population average displacement and gyradius) for a single run. The average over 10 runs are presented in Figures 8, 11, and 12 in the paper. To write output to the text file, in our Steppables Python file, we added the following lines of codes to the Python classes, i.e., FiberConcentrationCaseARandom50, FiberConcentrationCaseAUniform50, FiberConcentrationCaseBRandom25, etc. that implemented the conditions of interest. Please refer to our Steppables file HaptotaxisTest2DSteppables.py, which defines the cases, and HaptotaxisTest2D.py, which has options to specify which case to run by uncommenting the appropriate section of the script while commenting out the unused cases, and section 10 in the “CompuCell3D Python Scripting manual Version 3.7.5” for more details.

'''
fileName=’CaseA_Random_50.csv’ 
try : 
fileHandle , fullFileName=self .open \ 
FileInSimulationOutputDirectory(fileName ,”a”) 
except IOError :
print ”Could not open file ”, fileName,” for writing. ” 
return 
print >>fileHandle ,mcs,”,”, \
fiber_concentration ,”,”, \ 
fiber_cl concentration 
fileHandle . close () 
'''

2.	Simulation snapshots are logged every 1,000 MCS in the form of VTK files, which can be subsequently replayed in the CompuCell3D Player. This can be done by going to CompuCell3D Player, choose Configuration, then choose Save lattice every Nth MCS with N = 1000 and specify the Project Location to where the VTK files will be saved. Then analyze and take screenshots of the system in both cell and chemical fields (uncrosslinked and crosslinked fibers, MMPs, LOX) at the simulation times of interests. Arrangement of the screenshots for display in Figures 3-5, 6-7, and 9-10 for the paper were assembled in Microsoft PowerPoint. Out of all the 10 runs, we chose to present the system snapshots of the run with the cell migration metrics that best represented the calculated average values of the metrics. 
