# PX2_tools
Python tools for Partnership for Extreme Crystallography (PX2)

Components:

  -BMCXtal: single crystal diffraction data collection GUI used at PX2. Stable version requires Python 2.7.14, PyQt 4.11.4, SPEC 6.08.02, pyepics 3.3.3, fabio 0.9.0, numpy 1.16.5.
	
  -Gridscan: Grid powder scan with stationary detector position.
	
  -DACcorr: DAC correction program to find the rotation center.
	
  -PyRename: rename MARCCD TIF images to bruker mccd type file.
	
  -Pymask: mask bad pixels in Pilatus cbf images. Currently set for run 2019-1 April Pilatus detector setup. Need to change the masked out region for future use.
	
  -ShutterDelay: measure the pneumatic bench shutter delay at APS 13-BM-C.
