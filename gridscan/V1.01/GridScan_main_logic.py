# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:32:30 2020

@author: -
"""

import numpy as np
import re
import epics
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from GridScan_main_ui import Ui_MainWindow as mainW


class Logic_MainWindow(QtWidgets.QMainWindow, mainW):
    def __init__(self, parent=None):
        super(Logic_MainWindow, self).__init__(parent)
        self.setupUi(self)
        Linpath0 = epics.caget('13PIL1MSi:cam1:FilePath', as_string=1)
        Winpath0 = 'T:'+ Linpath0[11:]
        self.LinPath.setText(Linpath0)
        self.WinPath.setText(Winpath0)
        
        self.LinPath.returnPressed.connect(self.UpdatePath)
        self.StartScan.clicked.connect(self.collectgrid)
        self.Newlog.clicked.connect(self.Newlogfun)  
        self.SelPts.clicked.connect(self.ChoosePoints)
        self.RunPts.clicked.connect(self.RunPoints)
        self.SelSt.clicked.connect(self.SelStfun) 
        self.SelEnd.clicked.connect(self.SelEndfun) 
        
        
          
    def UpdatePath(self):
        Linpath0 = self.LinPath.text()
        Winpath0 = 'T:'+ Linpath0[11:]
        self.WinPath.setText(Winpath0)
        epics.caput('13PIL1MSi:cam1:FilePath', Linpath0)
        
    def collectgrid(self):
        epics.caput('13PIL1MSi:cam1:TriggerMode',0)
        X_srt = float(self.Hstart.text())
        X_end = float(self.Hend.text())
        X_Ntp = int(self.Hstep.text())
        
        Y_srt = float(self.Vstart.text())
        Y_end = float(self.Vend.text())
        Y_Ntp = int(self.Vstep.text())
        
        tmp = self.Hmotor.text()+'.HLM'
        XU = epics.caget(tmp)
        tmp = self.Hmotor.text()+'.LLM'
        XD = epics.caget(tmp)
        
        tmp = self.Vmotor.text()+'.HLM'
        YU = epics.caget(tmp)
        
        tmp = self.Vmotor.text()+'.LLM'
        YD = epics.caget(tmp)
        
        Phi = float(self.Phi.text())
        
        exp_tim = float(self.ExpTim.text())
        
        if X_srt <= XD or X_end <= XD:
            self.Notes.setText('H low limit error')
        elif X_srt >= XU or X_end >= XU:
            self.Notes.setText('H high limit error')
        elif Y_srt <= YD or Y_end <= YD:
            self.Notes.setText('V low limit error')
        elif Y_srt >= YU or Y_end >= YU:
            self.Notes.setText('V high limit error')
        elif self.Vmotor.text()=='13BMC:m45' and np.abs(Phi-90)>1.5 and np.abs(Phi+90)>1.5:
            self.Notes.setText('Check phi angle')
        elif self.Vmotor.text()=='13BMC:m44' and np.abs(Phi-0)>1.5:
            self.Notes.setText('Check phi angle')
        else:
            epics.caput('13BMC:m33.VAL',Phi)
            time.sleep(5)
            self.Notes.setText('')
            epics.caput('13PIL1MSi:cam1:AutoIncrement',0)
            X_siz = (X_end-X_srt)/(X_Ntp-1)
            Y_siz = (Y_end-Y_srt)/(Y_Ntp-1)
            for M_X in range(X_Ntp):
                for N_Y in range(Y_Ntp):
                    X_aim = X_srt + X_siz*M_X
                    Y_aim = Y_srt + Y_siz*N_Y
                    tmp = self.Hmotor.text()+'.VAL'
                    epics.caput(tmp, X_aim)
                    tmp = self.Vmotor.text()+'.VAL'
                    epics.caput(tmp, Y_aim)
                    tmp = self.FileNam.text()+'_X'+str(M_X)+'_Y'+str(N_Y)
                    epics.caput('13PIL1MSi:cam1:FileName',tmp)
                    time.sleep(2)
                    epics.caput('13PIL1MSi:cam1:AcquireTime',exp_tim)
                    epics.caput('13PIL1MSi:cam1:AcquirePeriod',exp_tim+0.5)
                    epics.caput('13PIL1MSi:cam1:NumImages',1)
                    epics.caput('13PIL1MSi:cam1:Acquire',1)
                    time.sleep(exp_tim+2)                
            epics.caput('13PIL1MSi:cam1:AutoIncrement',1)
            epics.caput('13PIL1MSi:cam1:TriggerMode',3)
            self.Notes.setText('Collection done')
    
    def SelStfun(self):
        tmp = self.Hmotor.text()+'.VAL'
        X_srt = epics.caget(tmp, as_string=1)
        self.Hstart.setText(X_srt)
        tmp = self.Vmotor.text()+'.VAL'
        Y_srt = epics.caget(tmp, as_string=1)
        self.Vstart.setText(Y_srt)

    def SelEndfun(self):
        tmp = self.Hmotor.text()+'.VAL'
        X_end = epics.caget(tmp, as_string=1)
        self.Hend.setText(X_end)
        tmp = self.Vmotor.text()+'.VAL'
        Y_end = epics.caget(tmp, as_string=1)
        self.Vend.setText(Y_end)
    
    def Newlogfun(self):
        tmp = ''
        f = open('./pointlog', 'w')
        f.write(tmp)
        f.close()
    
    def ChoosePoints(self):
        XX = epics.caget('13BMC:m44', as_string=True)
        YY = epics.caget('13BMC:m45', as_string=True)
        ZZ = epics.caget('13BMC:m46', as_string=True)
        tmp = XX + '\t' + YY + '\t' + ZZ +'\n'
        f = open('./pointlog', 'a')
        f.write(tmp)
        f.close()
        
    def RunPoints(self):
        epics.caput('13PIL1MSi:cam1:FileNumber',1)
        epics.caput('13PIL1MSi:cam1:AutoIncrement',1)
        f = open('./pointlog', 'r')
        tmp = f.readline()
        while(tmp !=''):
            L0 = re.split('\t', tmp)
            epics.caput('13BMC:m44', L0[0])
            epics.caput('13BMC:m45', L0[1])
            epics.caput('13BMC:m46', L0[2])
            time.sleep(2)
            tmp = self.qle1.text()
            epics.caput('13PIL1MSi:cam1:FileName',tmp)
            exp_tim = float(self.qle11.text())
            epics.caput('13PIL1MSi:cam1:AcquireTime',exp_tim)
            epics.caput('13PIL1MSi:cam1:AcquirePeriod',exp_tim+0.5)
            epics.caput('13PIL1MSi:cam1:Acquire',1)
            time.sleep(exp_tim+2) 
            tmp = f.readline()