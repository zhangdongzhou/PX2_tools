# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:13:28 2022

@author: Dongzhou_X99
"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
from epics import caput, caget
import time
import re


tick = 0.5
folder='13PIL1MSi:cam1:FilePath'
fileName='13PIL1MSi:cam1:FileName'
fileNum='13PIL1MSi:cam1:FileNumber'
acquire='13PIL1MSi:cam1:Acquire'
exposuretime='13PIL1MSi:cam1:AcquireTime'
acquireperiod='13PIL1MSi:cam1:AcquirePeriod'

caput('13PIL1MSi:cam1:NumImages',1)
caput(fileNum,1)
caput('13PIL1MSi:cam1:FileTemplate','%s%s_%d.tif')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        font = QtGui.QFont()
        font.setPointSize(11)
        
        ##### Set Layout
        self.setWindowTitle("GSECARS tube heater")
        self.CW = QtWidgets.QWidget(self)
        self.CWLayout = QtWidgets.QGridLayout(self.CW)
        
        # Topleft section
        self.L1 = QtWidgets.QLabel("Data Folder", self.CW)
        self.L1.setFont(font)
        self.CWLayout.addWidget(self.L1, 0, 0, 1, 2)
        
        S1 = caget('13PIL1MSi:cam1:FilePath',as_string=True)
        self.FolderN = QtWidgets.QLineEdit(S1,self.CW)
        
        self.CWLayout.addWidget(self.FolderN, 0, 1, 1, 6)
        
        # TopRight section
        self.L2 =QtWidgets.QLabel("Sample Name", self.CW)
        self.L2.setFont(font)
        self.CWLayout.addWidget(self.L2, 0, 7, 1, 1)
   
        S1 = caget('13PIL1MSi:cam1:FileName',as_string=True)
        self.newsample = QtWidgets.QLineEdit(S1, self.CW)
        self.CWLayout.addWidget(self.newsample, 0, 8, 1, 2)
        
        
        self.warn1 = QtWidgets.QLabel('',self.CW)
        self.warn1.setFont(font)
        self.warn1.setText('IDLE')
        self.warn1.setStyleSheet('color: blue')
        self.CWLayout.addWidget(self.warn1, 1, 1, 1, 1)
        
        
        
        # Labels below warning
        self.labelBox = QtWidgets.QGroupBox(self.CW)
        self.CWLayout.addWidget(self.labelBox, 3, 0, 1, 10)
        labelBLayout = QtWidgets.QGridLayout(self.labelBox)
        L2 = QtWidgets.QLabel("Tstart (K)", self.labelBox)
        L2.setFont(font)
        L2.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L2, 0, 0, 1, 1)
        L3 = QtWidgets.QLabel("Tend (K)", self.labelBox)
        L3.setFont(font)
        L3.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L3, 0, 1, 1, 1)
        L4 = QtWidgets.QLabel("Time (s)", self.labelBox)
        L4.setFont(font)
        L4.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L4, 0, 2, 1, 1)
        L5 = QtWidgets.QLabel("Exposure (s)", self.labelBox)
        L5.setFont(font)
        L5.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L5, 0, 3, 1, 1)
        L6 = QtWidgets.QLabel("XRD interval (s)", self.labelBox)
        L6.setFont(font)
        L6.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L6, 0, 4, 1, 1)
        L7 = QtWidgets.QLabel("     ", self.labelBox)
        L7.setFont(font)
        L7.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L7, 0, 5, 1, 1)
 
        
        self.Col_Btn = QtWidgets.QPushButton('Collect', self.CW)
        self.Col_Btn.setFont(QtGui.QFont('Arial', 15))
        self.CWLayout.addWidget(self.Col_Btn, 2, 8, 1, 2)
        self.Add_Btn = QtWidgets.QPushButton('Add', self.CW)
        self.Add_Btn.setFont(QtGui.QFont('Arial', 15))
        self.CWLayout.addWidget(self.Add_Btn, 2, 0, 1, 2)
        
        


        # Scroll area 1: Logzone
        self.LogZone = QtWidgets.QScrollArea(self.CW)
        self.LogZone.setWidgetResizable(True)
        self.LogWidget = QtWidgets.QWidget()
        self.LogWidget.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.LogLayout = QtWidgets.QVBoxLayout(self.LogWidget)
        self.LogL1 = QtWidgets.QLabel(self.LogWidget)
        self.LogL1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LogL1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.LogLayout.addWidget(self.LogL1)
        self.LogZone.setWidget(self.LogWidget)
        self.CWLayout.addWidget(self.LogZone, 0, 10, 10, 6)
        
        #Scroll area 2: add button
        self.ControlZone = QtWidgets.QScrollArea(self.CW)
        self.ControlZone.setWidgetResizable(True)
        self.ControlWidget = QtWidgets.QWidget()
        self.ControlWidget.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.ControlLayout = QtWidgets.QVBoxLayout(self.ControlWidget)
        self.ControlLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.ControlZone.setWidget(self.ControlWidget)
        self.CWLayout.addWidget(self.ControlZone, 4, 0, 6, 10)
   
        self.setCentralWidget(self.CW)

        self.Add_Btn.clicked.connect(self.addpoints)
        
        self.Col_Btn.clicked.connect(self.Datacol_clicked)
        
        self.remgroup = QtWidgets.QButtonGroup()
        self.remgroup.buttonClicked.connect(self.remgroup_clicked)
    

    def addpoints(self):
        count = self.ControlLayout.count()-1
        
        pointBox = QtWidgets.QGroupBox(self.ControlWidget)
        self.ControlLayout.insertWidget(count, pointBox)

        pointLayout = QtWidgets.QGridLayout(pointBox)
        for i in range(5):
            LE = QtWidgets.QLineEdit(pointBox)
            pointLayout.addWidget(LE, 0, i, 1, 1)
        
        Btn2 =  QtWidgets.QPushButton('Remove',pointBox)
        pointLayout.addWidget(Btn2, 0, 14, 1, 1)
        self.remgroup.addButton(Btn2)
        
    
    def remgroup_clicked(self, button):
        button.parent().deleteLater()
        
    
    
    def Datacol_clicked(self):
        
        ret = QtWidgets.QMessageBox.question(self, 'Collect?', "Collect?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if ret == QtWidgets.QMessageBox.Yes:
            P1folder = self.FolderN.text()
            P1Name = self.newsample.text()
            caput(folder,P1folder)
            caput(fileName,P1Name)
            time.sleep(0.5)
            DummyF = caget('13PIL1MSi:cam1:FilePath_RBV',as_string=True)
            DummyL = re.split('/',DummyF)
            FileF = 'T:'
            for i in range(3,len(DummyL)):
                FileF = FileF+'\\'+DummyL[i]
            FileF = FileF + 'log.txt'
            logf = open(FileF, 'w')
            LogS = ''
            
            caput('13PIL1MSi:cam1:NumImages',1)
            caput(fileNum,1)
            caput('13PIL1MSi:cam1:FileTemplate','%s%s_%d.tif')
            caput('13PIL1MSi:cam1:TriggerMode',0)
            caput("13USB2408_1:PID1.FBON",1)
            
            boxlist = self.ControlWidget.children()[1::]
            self.warn1.setText('BUSY')
            self.warn1.setStyleSheet('color: red')
            QtWidgets.QApplication.processEvents()
            
            for item in boxlist:
                
                Tstart = float(item.children()[1].text())
                Tend = float(item.children()[2].text())
                Ramptim = float(item.children()[3].text())
                Expotim = float(item.children()[4].text())
                Acqint = float(item.children()[5].text())
                
                slope = (Tend-Tstart)/Ramptim
                Nexp = int(round(Ramptim/tick))
                Nacq = int(round(Acqint/tick))
                
                caput(exposuretime,Expotim)
                caput(acquireperiod,Expotim+0.004)
                
                for i in range(Nexp):
                    i1 = i % Nacq
                    if i1 == 0:
                        TdummyL = np.zeros(Nacq)
                        caput(acquire,1)
                    Ttmp = Tstart + float(i)*tick*slope
                    caput("13USB2408_1:PID1.VAL",Ttmp)
                    time.sleep(tick)
                    TdummyL[i1] = float(caget("13USB2408_1:PID1.CVAL"))
                    if i1 == Nacq-1:
                        tmptim = time.asctime( time.localtime(time.time()) )
                        tmptemp = '{:.2f}'.format(np.average(TdummyL))
                        DummyF = caget('13PIL1MSi:cam1:FullFileName_RBV',as_string=True)
                        DummyL = re.split('/',DummyF)
                        tmpname = DummyL[-1]
                        logf.write(tmptim+'|'+str(tmptemp)+'|'+tmpname+'\n')
                        LogS = LogS+tmptim+'\ntemperature: '+str(tmptemp)+' '+tmpname+'\n'
                        self.LogL1.setText(LogS)
                        QtWidgets.QApplication.processEvents()
            
            logf.close()
            caput("13USB2408_1:PID1.FBON",0)
            caput("13BMC:DAC1_4.VAL",0)
            caput('13PIL1MSi:cam1:TriggerMode',3)
            self.warn1.setText('DONE')
            self.warn1.setStyleSheet('color: green')
                    

        
def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.resize(1300,530)

    mainwindow.show()
    app.exec()

if __name__ == '__main__':
    main()