# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:36:10 2019

@author: dzzhang
"""

import epics
import time
import sys
sys.path.append("//corvette/people_rw/specadm/Versions/spec6.08.02/src/splot/")
from SpecClient import SpecCommand,SpecVariable
import re
import os
import numpy as np
import BMCXtal_ui as ui
from PyQt4 import QtCore, QtGui


class uilogic(ui.Ui_MainWindow):
    def setupUi(self, MainWindow):
        ui.Ui_MainWindow.setupUi(self, MainWindow)
        ###################### Define actions #############
        ### Sample position
        self.Sel1.clicked.connect(lambda: self.Sel_click(self.LX1,self.LY1,self.LZ1))
        self.Mv1.clicked.connect(lambda: self.Mv_click(self.LX1,self.LY1,self.LZ1))
        self.Sel2.clicked.connect(lambda: self.Sel_click(self.LX2,self.LY2,self.LZ2))
        self.Mv2.clicked.connect(lambda: self.Mv_click(self.LX2,self.LY2,self.LZ2))
        self.Sel3.clicked.connect(lambda: self.Sel_click(self.LX3,self.LY3,self.LZ3))
        self.Mv3.clicked.connect(lambda: self.Mv_click(self.LX3,self.LY3,self.LZ3))
        self.Sel4.clicked.connect(lambda: self.Sel_click(self.LX4,self.LY4,self.LZ4))
        self.Mv4.clicked.connect(lambda: self.Mv_click(self.LX4,self.LY4,self.LZ4))
        self.Sel5.clicked.connect(lambda: self.Sel_click(self.LX5,self.LY5,self.LZ5))
        self.Mv5.clicked.connect(lambda: self.Mv_click(self.LX5,self.LY5,self.LZ5))
        self.Sel6.clicked.connect(lambda: self.Sel_click(self.LX6,self.LY6,self.LZ6))
        self.Mv6.clicked.connect(lambda: self.Mv_click(self.LX6,self.LY6,self.LZ6))
        
        ### Data, folder, sample name
        self.Col_Btn.clicked.connect(lambda: self.DataColl(self.Delt, self.Nu, self.KphiStart, self.KphiEnd, self.StpN, self.TimperFrm))
        
        self.FolderUpdate.clicked.connect(lambda: self.findfolder())

        self.SampleUpdate.clicked.connect(lambda: self.newsample(self.SampN))        
        
        ###################### Define actions #############

    def retranslateUi(self, MainWindow):
        ui.Ui_MainWindow.retranslateUi(self, MainWindow)

    def Sel_click(self, widget1, widget2, widget3):
        X = epics.caget('13BMC:m44.VAL')
        Y = epics.caget('13BMC:m45.VAL')
        Z = epics.caget('13BMC:m46.VAL')
        strX = "{0:.3f}".format(X)
        strY = "{0:.3f}".format(Y)
        strZ = "{0:.3f}".format(Z)
        widget1.setText(strX)
        widget2.setText(strY)
        widget3.setText(strZ)
        
    def Mv_click(self, widget1, widget2, widget3):
        strX = widget1.text()
        strY = widget2.text()
        strZ = widget3.text()
        X = float(strX)
        Y = float(strY)
        Z = float(strZ)
        X0 = epics.caget('13BMC:m44.RBV')
        XV = epics.caget('13BMC:m44.VELO')
        Y0 = epics.caget('13BMC:m45.RBV')
        YV = epics.caget('13BMC:m45.VELO')
        Z0 = epics.caget('13BMC:m46.RBV')
        ZV = epics.caget('13BMC:m46.VELO')        
        epics.caput('13BMC:m44.VAL',X)
        epics.caput('13BMC:m45.VAL',Y)
        epics.caput('13BMC:m46.VAL',Z)
        Ttem = max((X-X0)/XV,(Y-Y0)/YV, (Z-Z0)/ZV)+1.0
        time.sleep(Ttem)
    
    def Detmov(self, widget1, widget2):
        strX = widget1.text()
        strY = widget2.text()
        dl1 = float(strX)
        nu1 = float(strY)
        dl0 = epics.caget('13BMC:m37.RBV')
        nu0 = epics.caget('13BMC:m38.RBV')
        dlV = epics.caget('13BMC:m37.VELO')
        nuV = epics.caget('13BMC:m38.VELO')
        epics.caput('13BMC:m37.VAL',dl1)
        epics.caput('13BMC:m38.VAL',nu1)
        Ttem = max((dl1-dl0)/dlV,(nu1-nu0)/nuV)+8.0
        time.sleep(Ttem)
        
    def DataColl(self, Delt, Nu, KphiS, KphiE, StpN, TimNE):
        flgon = 1
        flgon = self.epicswarning(self.Delt, self.warn1, '13BMC:m37', flgon)
        flgon = self.epicswarning(self.Nu, self.warn2, '13BMC:m38', flgon)
        flgon = self.epicswarning(self.KphiStart, self.warn3, '13BMC:m33', flgon)
        flgon = self.epicswarning(self.KphiEnd, self.warn4, '13BMC:m33', flgon)
        flgon = self.stepwarning(self.StpN, self.warn5, flgon)
        flgon = self.speedwarning(self.TimperFrm, self.warn6, self.KphiStart, self.KphiEnd, self.StpN, flgon)
        if flgon:
            self.Detmov(Delt, Nu)
            xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
            kphivelo = epics.caget('13BMC:m33.VELO')
            kphiini = epics.caget('13BMC:m33.VAL')
            cmdcon = "xtal kphi " + KphiS.text()+' '+ KphiE.text()+' '+ StpN.text()+' '+ TimNE.text()
            eval("xtalcmd.executeCommand(\"%s\")" % cmdcon)
            Ttem = np.abs(kphiini-float(KphiS.text()))/kphivelo + float(TimNE.text())*float(StpN.text()) + 3
            time.sleep(Ttem)
            self.lastscan(self.LogL1, 'templog.txt')
    
    def findfolder(self):
        ProjPath = SpecVariable.SpecVariable('STARTUP_PROJECT_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        temp = ProjPath[25::]
        temp1 = 'T:'+temp+'images/'
        self.FolderN.setText(temp1)
        time.sleep(0.3)
    
    def newsample(self, newsample):
        SamNam = newsample.text()
        xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
        cmdcon = 'newsample '+SamNam
        eval("xtalcmd.executeCommand(\"%s\")" % cmdcon)
        time.sleep(0.2)
        self.nextscan(self.LogL1, 'templog.txt')
    
    def epicswarning(self, widget1, widget2, prefix, flg):
        # widget1 = input, widget2 = warning sign, prefix = epics motor name, flg = on/off
        num0 = widget1.text()
        time.sleep(0.02)
        try:
            num1 = float(num0)
            HLM = epics.caget(prefix+'.HLM')
            LLM = epics.caget(prefix+'.LLM')
            if num1 > HLM:
                widget2.setText('high lim')
                return flg*0
            elif num1 < LLM:
                widget2.setText('low lim')
                return flg*0
            else:
                widget2.setText('')
                return flg
        except:
            widget2.setText('not num')
            return flg*0
    
    def stepwarning(self, widget1, widget2, flg):
        num0 = widget1.text()
        try:
            num1 = int(num0)
            widget2.setText(str(num1))
            return flg
        except:
            widget2.setText('wrong')
            return flg*0
    
    def speedwarning(self, widget1, widget2, widget3, widget4, widget5, flg):
        # w1: time, w2: label, w3: kphistart, w4: kihiend, w5: num_of_step
        num0 = widget1.text()
        kphi0 = widget3.text()
        kphi1 = widget4.text()
        stp2 = widget5.text()
        try:
            num1 = float(num0)
            kphi10 = float(kphi0)
            kphi11 = float(kphi1)
            stp12 = float(stp2)
            spd = (kphi11-kphi10)/stp12/num1
            if num1 < 0.01:
                widget2.setText('too fast')
                return flg*0
            elif spd > 15.5:
                widget2.setText('too fast')
                return flg*0
            else:
                widget2.setText('')
                return flg
        except:
            widget2.setText('wrong')
            return flg*0
            
    def lastscan(self, widget1, tempfile):
        # only use after one scan is done. Newsample command creates a new logPath.
        LogPath = SpecVariable.SpecVariable('SCANLOG_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        FilePath = SpecVariable.SpecVariable('SCANLOG_FILE', 'corvette.cars.aps.anl.gov:6780').getValue()
        len1 = len(LogPath)
        dummy = FilePath[len1:-4]
        dummy1 = re.split('_', dummy)
        cmdcon = time.asctime()+'\n\t'+ dummy1[2] +' done, saved in folder: '+ dummy1[0]+'_'+dummy1[1]+'\n'
        f = open(tempfile, 'a+')
        dummy2 = f.read()
        f.close()
        os.remove(tempfile)
        dummy3 = cmdcon + dummy2
        f = open(tempfile, 'a+')
        f.write(dummy3)
        f.close()
        widget1.setText(dummy3)
    
    def nextscan(self, widget1, tempfile):
        # only use after press newsample
        LogPath = SpecVariable.SpecVariable('SCANLOG_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        MajorPath = SpecVariable.SpecVariable('STARTUP_PROJECT_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        len1 = len(MajorPath+"scandata/")
        dummy = LogPath[len1:-1]
        cmdcon = time.asctime()+'\n\tNew data will be saved in folder: ' + dummy + '\n'
        f = open(tempfile, 'a+')
        dummy2 = f.read()
        f.close()
        os.remove(tempfile)
        dummy3 = cmdcon + dummy2
        f = open(tempfile, 'a+')
        f.write(dummy3)
        f.close()
        widget1.setText(dummy3)
    
if __name__ == "__main__":
    xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
    eval("xtalcmd.executeCommand(\"%s\")" % 'wh')
    try:
        os.remove('templog.txt')
    except:
        pass
    time.sleep(0.3)
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui1 = uilogic()
    ui1.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())