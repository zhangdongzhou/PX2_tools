# PX2_tools
Python tools for Partnership for Extreme Crystallography (PX2)

Components:

  -BMCXtal: single crystal diffraction data collection GUI used at PX2. Requires Python 2.7, PyQt4, SPEC 6.08.02, Spyder3.2.8, pyepics.
	
  -Gridscan: Grid powder scan with stationary detector position.
	
  -DACcorr: DAC correction program to find the rotation center.
	
  -PyRename: rename MARCCD TIF images to bruker mccd type file.
	
  -Pymask: mask bad pixels in Pilatus cbf images. Currently set for run 2019-1 April Pilatus detector setup. Need to change the masked out region for future use.
	
  -ShutterDelay: measure the pneumatic bench shutter delay at APS 13-BM-C.
