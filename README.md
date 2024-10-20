# PX2_tools
Python tools for Partnership for Extreme Crystallography (PX2)

Components:

  -BMCXtal: single crystal diffraction data collection GUI used at PX2. Stable version requires Python3, PyQt5, SPEC 6.09+, pyepics, fabio, numpy.
	
  -Gridscan: Grid powder scan with stationary detector position.
	
  -DACcorr: DAC correction program to find the rotation center. Requires Python3, PyQt5, pyepics
	
  -PyRename: rename MARCCD TIF images to bruker mccd type file.
	
  -Pymask: mask bad pixels in Pilatus cbf images. Currently set for run 2019-1 April Pilatus detector setup. Need to change the masked out region for future use.
	
  -ShutterDelay: measure the pneumatic bench shutter delay at APS 13-BM-C.

  -CBFTIF (replacing Tif_converter with user interface): converts cbf images to tif images, so that they can be processed by ATREX. It will convert all the cbf images in one folder. Requires Python3, PyQt5, fabio

  -DACAxis: Calculator that can get the Miller indices of the crystal along the X-ray direction, which is needed for Brillouin experiment. Works with both ATREX/RSV and APEX p4p files. Requires Python3, PyQt5, regex.
  
  -PilatusMerge: Merge Pilatus images to remove the blanks. Uses the same calibration as Dioptas. Requires fabio and pyFAI.
  
  -Scanw: a copycat of the GSECARS IDL-based ScanW 1-D scanning software, but in python. It drives 1 EPICS motor and reads one EPICS scaler/detector. Requires Python3, pyEPICS and PyQt5.

  ### Notes on Python environment
  
  BMCXtal, DACcorr, CBFTIF, DACAxis needs Python3, PyQt5, numpy, pyepics, fabio. At beamline they all should work with virtual environment "BMCXtal". To run some codes in your own computers, please install pyepics and fabio in Anaconda3 environment, and in Anaconda3 prompt run "python the_script_name.py"
