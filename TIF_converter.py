# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:41:58 2020

@author: dzzhang
"""

import fabio
import os

files = []
# r=root, d=directories, f = files
FL = os.getcwd() # Folder Location
for r, d, f in os.walk(FL):
    for file in f:
        if '.cbf' in file:
            files.append(os.path.join(r, file))

for f1 in files:
    newN = f1[0:-3]+'tif'
    fabio.open(f1).convert("tif").save(newN)










































