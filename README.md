# MetastaticCancerECMRemodelingCC3D
Hybrid discrete-continuum model of ECM remodeling and its impact on metastatic cancer migration

[![DOI](https://zenodo.org/badge/145025121.svg)](https://zenodo.org/badge/latestdoi/145025121)

## Overview
This computational model describes the dynamic process of extracellular matrix remodeling in the vicinity of a primary tumor at the onset 
of metastasis. The system under investigation consists of cancer cells, two populations of collagen fibers,
and two enzymes that react to remodel the microenvironment, impacting cancer cell migration away from the primary tumor. The cancer cells are treated as discrete agents, and ECM components including collagen fibers and remodeling enzymes are modelled by a system of partial differential equations.

## Computational Model for Metastatic Cancer Migration through a Remodeling Extracellular Matrix
### Code Authors
Yen T. Nguyen Edalgo, Anya L. Zornes, Ashlee N. Ford Versypt, 
School of Chemical Engineering,
Oklahoma State University.
Corresponding author: A. N. Ford Versypt, ashleefv@okstate.edu

### Related publication for model details
Yen T. Nguyen Edalgo, Anya L. Zornes, Ashlee N. Ford Versypt, A Hybrid Discrete-Continuous Model of Metastatic Cancer Cell Migration through a Remodelling Extracellular Matrix,
Submitted to Journal of the Royal Society Interface, 2018.

### Files

* HaptotaxisTest2D.cc3d

This file includes the nominal case for running the model.

* Simulation folder

This folder includes the python, python steppables, and xml files that can be used to customize settings in the code for each simulation.
