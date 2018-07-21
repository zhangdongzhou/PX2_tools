# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:37:39 2017

@author: Dongzhou Zhang (dzzhang@cars.uchicago.edu)
Diamond correction tool for PX^2

Need: PyQt5, pyepics, python 3.5

Usage:
    Kphi go to 90 deg (or -90 deg)    
    Goto IDL scanw, scan m45, find and go to the center, put the center value in 
the code.
    Rotate Kphi by positive 5-20 degs, record the relative Kphi value in the
code.
    Scan m45 again. find the center (no need to move), put the value to the code.
    Rotate Kphi by negative 5-20 degs, scan m45 again. find the center (no need to 
move), put the value to the code.
    Press the button to finish the diamond correction.
    
Issues:
    Does NOT work for Kphi around 0 deg.
"""

import sys
from PyQt5.Qt import *
import epics
import numpy as np
import time
 
 
class DACcorr(QMainWindow):
     
    def __init__(self, parent=None):
        super(DACcorr,self).__init__(parent)
        self.initUI()
         

    
    
    def initUI(self):              
        self.setGeometry(300, 300, 280, 210)
        self.setWindowTitle('Shutter Delay')   
        
        self.btn = QPushButton('Measure Delay', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.updateUI)
        
        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)
        self.lbl3 = QLabel(self)
        self.lbl4 = QLabel(self)
        self.lbl5 = QLabel(self)
        self.lbl1.move(200, 30)
        self.lbl2.move(35, 100)
        self.lbl3.move(200, 100)
        self.lbl4.move(35, 150)
        self.lbl5.move(200, 150)
#        self.lbl1.setText(r'Wait 5s')
        self.lbl2.setText(r'Shutter open delay')
        self.lbl2.adjustSize()
#        self.lbl3.setText(r'Center of Sample_Y (m45) scan at kphi = 90+Δkphi')
#        self.lbl3.adjustSize()
        self.lbl4.setText(r'Shutter close delay')
        self.lbl4.adjustSize()        

#        self.qle1 = QLineEdit(self)
#        self.qle2 = QLineEdit(self)
#        self.qle3 = QLineEdit(self)
#        self.qle4 = QLineEdit(self)
#        self.qle1.move(350, 50-30)
#        self.qle2.move(350, 100-30)
#        self.qle3.move(350, 150-30)
#        self.qle4.move(350, 200-30)
        

 

    def updateUI(self):
        self.lbl1.setText(r'Wait 5s')
        for i in range (3):
            epics.caput('13BMC:Unidig1Bo12', 1)
            time.sleep(0.2)
            epics.caput('13BMC:Unidig1Bo12', 0)
            time.sleep(0.2)
        time.sleep(0.5)
        dT = 0.001
        epics.caput('13BMC:SIS1:Dwell', dT)
        epics.caput('13BMC:SIS1:ChannelAdvance', 0)
        epics.caput('13BMC:SIS1:EraseAll', 1)
        epics.caput('13BMC:SIS1:StartAll', 1)
        time.sleep(0.1)
        epics.caput('13BMC:Unidig1Bo12', 1)
        time.sleep(1)
        epics.caput('13BMC:Unidig1Bo12', 0)
        time.sleep(1.5)
        epics.caput('13BMC:SIS1:StopAll', 1)
        PVin =  epics.caget('13BMC:SIS1:mca4.VAL')
        PVout =  epics.caget('13BMC:SIS1:mca3.VAL')
        NN = epics.caget('13BMC:SIS1:CurrentChannel')
        m_in = 0
        n_in = 0
        temp1 = PVin[1]-PVin[0]
        temp2 = PVin[1]-PVin[0]
        for i in range(NN-1):
            if PVin[i+1]-PVin[i] > temp1:
                temp1 = PVin[i+1]-PVin[i]
                m_in = i
            if PVin[i+1]-PVin[i] < temp2:
                temp2 = PVin[i+1]-PVin[i]
                n_in = i
        m_out = 0
        n_out = 0
        temp1 = PVout[1]-PVout[0]
        temp2 = PVout[1]-PVout[0]
        for i in range(NN-1):
            if PVout[i+1]-PVout[i] > temp1:
                temp1 = PVout[i+1]-PVout[i]
                m_out = i
            if PVout[i+1]-PVout[i] < temp2:
                temp2 = PVout[i+1]-PVout[i]
                n_out = i
        m = (m_out-m_in)*dT
        n = (n_out-n_in)*dT
        str_in = str(m)+' sec'
        str_out = str(n)+' sec'
        self.lbl3.setText(str_in)
        self.lbl3.adjustSize()
        self.lbl5.setText(str_out)
        self.lbl5.adjustSize()
#        try:
##            dphi = float(self.qle1.text())
##            ctr = float(self.qle2.text())
##            pls = float(self.qle3.text())
##            mis = float(self.qle4.text())
##            dx = (mis-pls)/(2*math.sin(dphi/180*math.pi))
#            x_ini = epics.caget('13BMC:m44.VAL')
#            x_fin = x_ini+dx
#            txt1 = 'Move sample_X from '+str(x_ini)+' by '+str(dx)[0:8]+' to '+str(x_fin)[0:8]
#            self.lbl5.setText(txt1)
#            self.lbl5.adjustSize()
#            epics.caput('13BMC:m44.VAL',x_fin)
#        except:
#            self.lbl5.setText('Invalid values')
        self.lbl1.setText(r'done')
        epics.caput('13BMC:SIS1:ChannelAdvance', 1)
                
        
def main():
    app = QApplication(sys.argv)
    ex = DACcorr()
    ex.show()
    sys.exit(app.exec_())        
    
if __name__ == '__main__':
     main()
