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
#caput('13PIL1MSi:cam1:AutoIncrement',0)
caput('13PIL1MSi:cam1:FileTemplate','%s%s_%d.tif')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        font = QtGui.QFont()
        font.setPointSize(11)
        
        ##### Set Layout
        self.setWindowTitle("GSECARS tube heater")
        self.CW = QtWidgets.QWidget(self)
        # self.CWLayout = QtWidgets.QVBoxLayout(self.CW)
        self.CWLayout = QtWidgets.QGridLayout(self.CW)
        
        # Topleft section
        self.L1 = QtWidgets.QLabel("Data Folder", self.CW)
        self.L1.setFont(font)
        self.CWLayout.addWidget(self.L1, 0, 0, 1, 2)
        # self.B1 = QtWidgets.QPushButton('Update', self.CW)
        # self.CWLayout.addWidget(self.B1, 0, 2, 1, 2)
        S1 = caget('13PIL1MSi:cam1:FilePath',as_string=True)
        self.FolderN = QtWidgets.QLineEdit(S1,self.CW)
        # self.FolderN.setFrameShape(QtWidgets.QFrame.Panel)
        # self.FolderN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CWLayout.addWidget(self.FolderN, 0, 1, 1, 6)
        
        # TopRight section
        self.L2 =QtWidgets.QLabel("Sample Name", self.CW)
        self.L2.setFont(font)
        self.CWLayout.addWidget(self.L2, 0, 7, 1, 1)
        # self.FolderUpdate = QtWidgets.QPushButton('Update', self.CW)
        # self.CWLayout.addWidget(self.FolderUpdate, 0, 17, 1, 2)
        # self.Calibration = QtWidgets.QPushButton('Calibration', self.CW)
        # self.CWLayout.addWidget(self.Calibration, 0, 19, 1, 2)
        
        S1 = caget('13PIL1MSi:cam1:FileName',as_string=True)
        self.newsample = QtWidgets.QLineEdit(S1, self.CW)
        self.CWLayout.addWidget(self.newsample, 0, 8, 1, 2)
        # self.warn7 = QtWidgets.QLabel(self.CW)
        # self.CWLayout.addWidget(self.warn7, 1, 17, 1, 2)
        # self.Clear2 = QtWidgets.QPushButton('Clear log', self.CW)
        # self.CWLayout.addWidget(self.Clear2, 1, 19, 1, 2)
        
        # Warning section
        # self.warn1 = QtWidgets.QLabel(self.CW)
        # self.CWLayout.addWidget(self.warn1, 2, 1, 1, 1)
        # self.warn2 = QtWidgets.QLabel(self.CW)
        # # self.CWLayout.addWidget(self.warn2, 2, 2, 1, 1)
        # self.warn3 = QtWidgets.QLabel(self.CW)
        # self.CWLayout.addWidget(self.warn3, 2, 3, 1, 1)
        # self.warn4 = QtWidgets.QLabel(self.CW)
        # self.CWLayout.addWidget(self.warn4, 2, 4, 1, 1)
        # self.warn5 = QtWidgets.QLabel(self.CW)
        # self.CWLayout.addWidget(self.warn5, 2, 5, 1, 1)
        # self.warn6 = QtWidgets.QLabel(self.CW)
        # self.CWLayout.addWidget(self.warn6, 2, 6, 1, 1)
        # self.warn8 = QtWidgets.QLabel(self.CW)
        # self.CWLayout.addWidget(self.warn8, 2, 8, 1, 1)
        
        # self.L6 = QtWidgets.QLabel("BUSY", self.CW)
        # self.L6.setFont(font)
        # self.L6.setAlignment(QtCore.Qt.AlignCenter)
        # self.CWLayout.addWidget(self.L6, 3, 10, 1, 2)
        
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
        # L9 = QtWidgets.QLabel("nu", self.labelBox)
        # L9.setFont(font)
        # L9.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L9, 1, 2, 1, 1)
        # L10 = QtWidgets.QLabel("start", self.labelBox)
        # L10.setFont(font)
        # L10.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L10, 1, 3, 1, 1)
        # L11 = QtWidgets.QLabel("end", self.labelBox)
        # L11.setFont(font)
        # L11.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L11, 1, 4, 1, 1)
        # L12 = QtWidgets.QLabel("Step#", self.labelBox)
        # L12.setFont(font)
        # L12.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L12, 1, 5, 1, 1)
        # L13 = QtWidgets.QLabel("Time/frame", self.labelBox)
        # L13.setFont(font)
        # L13.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L13, 1, 6, 1, 1)
        # L14 = QtWidgets.QLabel("X", self.labelBox)
        # L14.setFont(font)
        # L14.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L14, 1, 7, 1, 1)
        # L15 = QtWidgets.QLabel("Y", self.labelBox)
        # L15.setFont(font)
        # L15.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L15, 1, 8, 1, 1)
        # L16 = QtWidgets.QLabel("Z", self.labelBox)
        # L16.setFont(font)
        # L16.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L16, 1, 9, 1, 1)
        # L17 = QtWidgets.QLabel("Sum", self.labelBox)
        # L17.setFont(font)
        # L17.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L17, 1, 10, 1, 1)
        # self.L18 = QtWidgets.QLabel("", self.labelBox)
        # # labelBLayout.addWidget(self.L18, 1, 11, 1, 1)
        # L19 = QtWidgets.QLabel("Collect?", self.labelBox)
        # L19.setFont(font)
        # L19.setAlignment(QtCore.Qt.AlignCenter)
        # labelBLayout.addWidget(L19, 1, 12, 1, 1)
        # self.L20 = QtWidgets.QLabel(self.labelBox)
        # labelBLayout.addWidget(self.L20, 1, 13, 1, 1)
        
        self.Col_Btn = QtWidgets.QPushButton('Collect', self.CW)
        self.Col_Btn.setFont(QtGui.QFont('Arial', 15))
        self.CWLayout.addWidget(self.Col_Btn, 2, 8, 1, 2)
        self.Add_Btn = QtWidgets.QPushButton('Add', self.CW)
        self.Add_Btn.setFont(QtGui.QFont('Arial', 15))
        self.CWLayout.addWidget(self.Add_Btn, 2, 0, 1, 2)
        # self.Rem_Btn = QtWidgets.QPushButton('Remove', self.CW)
        # self.CWLayout.addWidget(self.Rem_Btn, 3, 12, 1, 2)
        


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
        # self.ControlZone.setWidget(self.ControlWidget)

    #     self.buttonWidget = QtWidgets.QWidget(self.centralwidget)
    #     self.buttonAddGroupBox = QtWidgets.QPushButton('Add GroupBox', self.buttonWidget)
    #     self.buttonDeleteGroupBox = QtWidgets.QPushButton('DeleteLater GroupBox', self.buttonWidget)
    #     self.readvalue1 = QtWidgets.QPushButton('read value1', self.buttonWidget)
    #     self.readvalue2 = QtWidgets.QPushButton('read value2', self.buttonWidget)
    #     self.value1=QtWidgets.QLabel(self.buttonWidget)
    #     self.value2=QtWidgets.QLabel(self.buttonWidget)
    #     self.buttonLayout = QtWidgets.QGridLayout(self.buttonWidget)
    #     self.buttonLayout.addWidget(self.buttonAddGroupBox,          0, 0, 1, 1)
    #     self.buttonLayout.addWidget(self.buttonDeleteGroupBox,  0, 1, 1, 1)
    #     self.buttonLayout.addWidget(self.readvalue1,   1, 0, 1, 1)
    #     self.buttonLayout.addWidget(self.readvalue2, 1, 1, 1, 1)
    #     self.buttonLayout.addWidget(self.value1,    0,2,1,1)
    #     self.buttonLayout.addWidget(self.value2,    1,2,1,1)
        
        
    #     self.centralwidgetLayout.addWidget(self.buttonWidget)
    #     self.centralwidgetLayout.addWidget(self.scrollArea)
        self.setCentralWidget(self.CW)

        self.Add_Btn.clicked.connect(self.addpoints)
        
        self.Col_Btn.clicked.connect(self.Datacol_clicked)
        # self.Rem_Btn.clicked.connect(self.deleteLaterGroupBox)
        
        # self.selgroup = QtWidgets.QButtonGroup()
        # self.selgroup.buttonClicked.connect(self.selgroup_clicked)
        # self.movgroup = QtWidgets.QButtonGroup()
        self.remgroup = QtWidgets.QButtonGroup()
        self.remgroup.buttonClicked.connect(self.remgroup_clicked)
    #     self.readvalue1.clicked.connect(self.removeItemGroupBox)
    #     self.readvalue2.clicked.connect(self.removeWidgetGroupBox)

    def addpoints(self):
        count = self.ControlLayout.count()-1
        # pointBox = QtWidgets.QGroupBox('Point ' + str(count), self.ControlWidget)
        pointBox = QtWidgets.QGroupBox(self.ControlWidget)
        self.ControlLayout.insertWidget(count, pointBox)

        pointLayout = QtWidgets.QGridLayout(pointBox)
        for i in range(5):
            LE = QtWidgets.QLineEdit(pointBox)
            pointLayout.addWidget(LE, 0, i, 1, 1)
        # CK1 = QtWidgets.QCheckBox(pointBox)
        # pointLayout.addWidget(CK1, 0, 10, 1, 1)
        # Btn1 =  QtWidgets.QPushButton('Select',pointBox)
        # pointLayout.addWidget(Btn1, 0, 11, 1, 1)
        # CK2 = QtWidgets.QCheckBox(pointBox)
        # pointLayout.addWidget(CK2, 0, 12, 1, 1)
        # self.selgroup.addButton(Btn1)
        # Btn3 =  QtWidgets.QPushButton('Move',pointBox)
        # pointLayout.addWidget(Btn3, 0, 13, 1, 1)
        # self.movgroup.addButton(Btn3)
        Btn2 =  QtWidgets.QPushButton('Remove',pointBox)
        pointLayout.addWidget(Btn2, 0, 14, 1, 1)
        self.remgroup.addButton(Btn2)
        ####### test
        # print(self.remgroup.buttons())
        # print(Btn2.parentWidget())
        # count = self.ControlLayout.count()
        # print(count)
        # item = self.ControlLayout.itemAt(count - 2).widget()
        # print(item)
    
    # def remove_btn_clicked(button):
    #     widget = button.parentWidget()
    #     widget.deleteLater()
    
    def remgroup_clicked(self, button):
        # print(button, button.parent(), button.parent().parent())
        button.parent().deleteLater()
        # print(button.children()[1].children()[-3].children()[0].children())
    
    # def selgroup_clicked(self, button):
    #     # print(button.parent().children())
    #     button.parent().children()[8].setText(str(dummynum1))
    #     button.parent().children()[9].setText(str(dummynum2))
    #     button.parent().children()[10].setText(str(dummynum3))
    
    def Datacol_clicked(self):
        # msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, 'Checktime', 'Select')
        # ret =msg.question(msg, title, text)
        ret = QtWidgets.QMessageBox.question(self, 'Collect?', "Collect?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # print(self.ControlWidget.children()[1::])
        if ret == QtWidgets.QMessageBox.Yes:
            P1folder = self.FolderN.text()
            P1Name = self.newsample.text()
            caput(folder,P1folder)
            caput(fileName,P1Name)
            DummyF = caget('13PIL1MSi:cam1:FilePath_RBV',as_string=True)
            DummyL = re.split('/',DummyF)
            FileF = 'T:'
            for i in range(3,len(DummyL)):
                FileF = FileF+'\\'+DummyL[i]
            FileF = FileF + 'log.txt'
            logf = open(FileF, 'w')
            
            caput('13PIL1MSi:cam1:NumImages',1)
            caput(fileNum,1)
            caput('13PIL1MSi:cam1:FileTemplate','%s%s_%d.tif')
            caput('13PIL1MSi:cam1:TriggerMode',0)
            caput("13USB2408_1:PID1.FBON",1)
            
            boxlist = self.ControlWidget.children()[1::]
            for item in boxlist:
                
                # item.children()[1].setText(str(dummynum2))
                Tstart = float(item.children()[1].text())
                # print(Tstart)
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
            
            logf.close()
            caput("13USB2408_1:PID1.FBON",0)
            caput("13BMC:DAC1_4.VAL",0)
            caput('13PIL1MSi:cam1:TriggerMode',3)
                    
                # print(item.children())
                # if item.children()[13].isChecked() == True:
                #     item.children()[1].setText(dummystr2)
                #     item.children()[13].setChecked(0)

    # def deleteLaterGroupBox(self):
    #     count = self.ControlLayout.count()
    #     if count == 1:
    #         return
    #     item = self.ControlLayout.itemAt(count - 2)
    #     widget = item.widget()
    #     # print(item)
    #     widget.deleteLater()

    # def removeItemGroupBox(self):
    #     count = self.scrollAreaWidgetLayout.count()
    #     if count == 1:
    #         return
    #     item = self.scrollAreaWidgetLayout.itemAt(count - 2)

    #     self.value1.setText(item.widget().children()[2].text())
        
    # def removeWidgetGroupBox(self):
    #     count = self.scrollAreaWidgetLayout.count()
    #     if count == 1:
    #         return
    #     item = self.scrollAreaWidgetLayout.itemAt(count - 2)

    #     self.value2.setText(item.widget().children()[3].text())
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.resize(1300,530)

    mainwindow.show()
    app.exec()

if __name__ == '__main__':
    main()