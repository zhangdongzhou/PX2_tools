# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:35:20 2020

@author: Dongzhou_X99
"""

import time
import os


tempfile  = 'dummy.txt'
f = open(tempfile,'a+')
f.seek(0)
dummy0 = f.read()
f.close()

os.remove(tempfile)

f = open(tempfile, 'a+')
tst = time.asctime()+'\n'+dummy0
f.write(tst)
f.close()