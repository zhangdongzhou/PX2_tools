# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:52:19 2019

@author: dzzhang
"""

import numpy as np
import fabio
import re
###########
prefix = 'Prp_1_001_'
############
postfix= '.cbf'

for ind in range(340):
    ind1 =  ind+1
    numind = '%05d' % ind1
    oldfile = prefix+numind+postfix
    newfile = 'R'+oldfile
    im = fabio.open(oldfile)
    
    Data = np.array(im.data)
    #print(im.data[213, 495])
    #print(im.header)
    newmask = Data
    
    for i in range(212,407):
        for j in range(494,981):
            newmask[i, j] = -1
            
    im.data=newmask
    
    #print(im.data[213, 495])
    #print(im.header)
    
    im.write('temp.cbf')
    
    #f = open('Prp1_1_001_00001.cbf')
    
    #print(f.readline())
    
    f0 = open(oldfile,'r+b')
    f1 = open('temp.cbf','r+b')
    
    t0 = f0.read()
    t1 = f1.read()
    
    #print(t1)
    
    f0.close()
    f1.close()
    
    x0 = b'X-Binary-Size-Padding: 4095'
    x1 = b'X-Binary-Size-Padding: 1'
    
    l0 = re.split(x0, t0)
    l1 = re.split(x1, t1)
    
    n1 = l0[0]+x0+l1[1]
    
    x10 = b'X-Binary-Size: '
    x11 = b'X-Binary-ID: '
    
    la0 = re.split(x10, t1)
    lb0 = re.split(x10, n1)
    #print(la0[1])
    la1 = re.split(x11, la0[1])
    lb1 = re.split(x11, lb0[1])
    
    n1 = lb0[0] + x10+ la1[0] +x11 + lb1[1]
    
    
    f2 = open(newfile,'w+b')
    f2.write(n1)
    f2.close()

#f2 = open('Prp2_1_001_00001.cbf','r+b')

#print(f2.read())
#f2.close()