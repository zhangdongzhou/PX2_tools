# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:13:28 2022

@author: Dongzhou_X99
"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


import epics
import time
from pyspec.client import SpecCommand,SpecVariable
import re
import os
import numpy as np

import BMCXtal_calibui as calibui
import fabio
###### Dummy section, remove in real code
dummynum1 = 0.01
dummynum2 = 0.03
dummynum3 = 0.04
dummystr1 = 'dummy/path/place/holder'
dummystr2 = 'checked'


class calibUI(QtWidgets.QDialog, calibui.Ui_Dialog):
    def __init__(self, parent=None):
        super(calibUI, self).__init__(parent)
        self.setupUi(self)
        
        Dist0 = SpecVariable.SpecVariable('BMCPilatusDist', 'corvette.cars.aps.anl.gov:6780').getValue()
        self.T1.setText(str(Dist0))
        beamX0 = SpecVariable.SpecVariable('BMCPilatusBeamX', 'corvette.cars.aps.anl.gov:6780').getValue()
        self.T2.setText(str(beamX0))
        beamY0 = SpecVariable.SpecVariable('BMCPilatusBeamY', 'corvette.cars.aps.anl.gov:6780').getValue()
        self.T3.setText(str(beamY0))
        self.R2.setChecked(True)
        
        ###################### Define actions #############
        self.B1.clicked.connect(lambda: self.update_clicked())
    
    def update_clicked(self):
        xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
        Dist = self.T1.text()
        cmdcon0 = 'BMCPilatusDist = '+ Dist
        eval("xtalcmd.executeCommand(\"%s\")" % cmdcon0)
        time.sleep(0.2)
        beamX = self.T2.text()
        cmdcon1 = 'BMCPilatusBeamX = '+ beamX
        eval("xtalcmd.executeCommand(\"%s\")" % cmdcon1)
        time.sleep(0.2)
        beamY = self.T3.text()
        cmdcon2 = 'BMCPilatusBeamY = '+ beamY
        eval("xtalcmd.executeCommand(\"%s\")" % cmdcon2)
        time.sleep(0.2)
        if self.R2.isChecked()==True:
            cmdcon3 = 'TIFCBF = 1'
            xtalcmd.executeCommand(cmdcon3)
        else:
            cmdcon3 = 'TIFCBF = 0'
            xtalcmd.executeCommand(cmdcon3)    
        CrysTxt = 'APEX parameters have been written.\nCrysAlis parameters are:\nDetectorDist = '
        CrysTxt = CrysTxt + Dist + '\nX0 = '
        CrysTxt = CrysTxt + str(float(beamX)+32.0) + '\nY0= '
        CrysTxt = CrysTxt + str(1044.0-float(beamY))
        self.CrysAlis.setText(CrysTxt)
        
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        font = QtGui.QFont()
        font.setPointSize(11)
        
        ##### Set Layout
        self.setWindowTitle("13BMC Single Crystal Data Collection")
        self.CW = QtWidgets.QWidget(self)
        # self.CWLayout = QtWidgets.QVBoxLayout(self.CW)
        self.CWLayout = QtWidgets.QGridLayout(self.CW)
        
        # Topleft section
        self.L1 = QtWidgets.QLabel("Data Folder", self.CW)
        self.L1.setFont(font)
        self.CWLayout.addWidget(self.L1, 0, 0, 1, 2)
        self.B1 = QtWidgets.QPushButton('Update', self.CW)
        self.CWLayout.addWidget(self.B1, 0, 2, 1, 2)
        self.FolderN = QtWidgets.QLabel('',self.CW)
        self.FolderN.setFrameShape(QtWidgets.QFrame.Panel)
        self.FolderN.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CWLayout.addWidget(self.FolderN, 1, 0, 1, 15)
        
        # TopRight section
        self.L2 =QtWidgets.QLabel("Image folder", self.CW)
        self.L2.setFont(font)
        self.CWLayout.addWidget(self.L2, 0, 15, 1, 2)
        self.FolderUpdate = QtWidgets.QPushButton('Update', self.CW)
        self.CWLayout.addWidget(self.FolderUpdate, 0, 17, 1, 2)
        self.Calibration = QtWidgets.QPushButton('Calibration', self.CW)
        self.CWLayout.addWidget(self.Calibration, 0, 19, 1, 2)
        
        self.newsample = QtWidgets.QLineEdit('', self.CW)
        self.CWLayout.addWidget(self.newsample, 1, 15, 1, 2)
        self.warn7 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn7, 1, 17, 1, 2)
        self.Clear2 = QtWidgets.QPushButton('Clear log', self.CW)
        self.CWLayout.addWidget(self.Clear2, 1, 19, 1, 2)
        
        # Warning section
        self.warn1 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn1, 2, 1, 1, 1)
        self.warn2 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn2, 2, 2, 1, 1)
        self.warn3 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn3, 2, 3, 1, 1)
        self.warn4 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn4, 2, 4, 1, 1)
        self.warn5 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn5, 2, 5, 1, 1)
        self.warn6 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn6, 2, 6, 1, 1)
        self.warn8 = QtWidgets.QLabel(self.CW)
        self.CWLayout.addWidget(self.warn8, 2, 8, 1, 1)
        
        self.L6 = QtWidgets.QLabel("", self.CW)
        self.L6.setFont(font)
        self.L6.setAlignment(QtCore.Qt.AlignCenter)
        self.CWLayout.addWidget(self.L6, 3, 10, 1, 2)
        
        # Labels below warning
        self.labelBox = QtWidgets.QGroupBox(self.CW)
        self.CWLayout.addWidget(self.labelBox, 4, 0, 1, 14)
        labelBLayout = QtWidgets.QGridLayout(self.labelBox)
        L2 = QtWidgets.QLabel("Sample", self.labelBox)
        L2.setFont(font)
        L2.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L2, 0, 0, 1, 1)
        L3 = QtWidgets.QLabel("Detector", self.labelBox)
        L3.setFont(font)
        L3.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L3, 0, 1, 1, 2)
        L4 = QtWidgets.QLabel("kphi", self.labelBox)
        L4.setFont(font)
        L4.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L4, 0, 3, 1, 2)
        L5 = QtWidgets.QLabel("Sample", self.labelBox)
        L5.setFont(font)
        L5.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L5, 0, 7, 1, 3)
        L7 = QtWidgets.QLabel("description", self.labelBox)
        L7.setFont(font)
        L7.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L7, 1, 0, 1, 1)
        L8 = QtWidgets.QLabel("del", self.labelBox)
        L8.setFont(font)
        L8.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L8, 1, 1, 1, 1)
        L9 = QtWidgets.QLabel("nu", self.labelBox)
        L9.setFont(font)
        L9.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L9, 1, 2, 1, 1)
        L10 = QtWidgets.QLabel("start", self.labelBox)
        L10.setFont(font)
        L10.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L10, 1, 3, 1, 1)
        L11 = QtWidgets.QLabel("end", self.labelBox)
        L11.setFont(font)
        L11.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L11, 1, 4, 1, 1)
        L12 = QtWidgets.QLabel("Step#", self.labelBox)
        L12.setFont(font)
        L12.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L12, 1, 5, 1, 1)
        L13 = QtWidgets.QLabel("Time/frame", self.labelBox)
        L13.setFont(font)
        L13.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L13, 1, 6, 1, 1)
        L14 = QtWidgets.QLabel("X", self.labelBox)
        L14.setFont(font)
        L14.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L14, 1, 7, 1, 1)
        L15 = QtWidgets.QLabel("Y", self.labelBox)
        L15.setFont(font)
        L15.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L15, 1, 8, 1, 1)
        L16 = QtWidgets.QLabel("Z", self.labelBox)
        L16.setFont(font)
        L16.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L16, 1, 9, 1, 1)
        L17 = QtWidgets.QLabel("Sum", self.labelBox)
        L17.setFont(font)
        # L17.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L17, 1, 10, 1, 1)
        # self.L18 = QtWidgets.QLabel("", self.labelBox)
        # labelBLayout.addWidget(self.L18, 1, 11, 1, 1)
        L19 = QtWidgets.QLabel("Collect?", self.labelBox)
        L19.setFont(font)
        L19.setAlignment(QtCore.Qt.AlignCenter)
        labelBLayout.addWidget(L19, 1, 12, 1, 1)
        self.L20 = QtWidgets.QLabel(self.labelBox)
        labelBLayout.addWidget(self.L20, 1, 13, 1, 1)
        
        self.Col_Btn = QtWidgets.QPushButton('Collect', self.CW)
        self.Col_Btn.setFont(QtGui.QFont('Arial', 15))
        self.CWLayout.addWidget(self.Col_Btn, 2, 10, 1, 2)
        self.Add_Btn = QtWidgets.QPushButton('Add', self.CW)
        self.Add_Btn.setFont(QtGui.QFont('Arial', 15))
        self.CWLayout.addWidget(self.Add_Btn, 2, 12, 1, 2)
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
        self.CWLayout.addWidget(self.LogZone, 2, 15, 14, 6)
        
        #Scroll area 2: add button
        self.ControlZone = QtWidgets.QScrollArea(self.CW)
        self.ControlZone.setWidgetResizable(True)
        self.ControlWidget = QtWidgets.QWidget()
        self.ControlWidget.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.ControlLayout = QtWidgets.QVBoxLayout(self.ControlWidget)
        self.ControlLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.ControlZone.setWidget(self.ControlWidget)
        self.CWLayout.addWidget(self.ControlZone, 5, 0, 11, 15)
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
        
        self.selgroup = QtWidgets.QButtonGroup()
        self.selgroup.buttonClicked.connect(self.selgroup_clicked)
        self.movgroup = QtWidgets.QButtonGroup()
        self.remgroup = QtWidgets.QButtonGroup()
        self.remgroup.buttonClicked.connect(self.remgroup_clicked)
    #     self.readvalue1.clicked.connect(self.removeItemGroupBox)
    #     self.readvalue2.clicked.connect(self.removeWidgetGroupBox)
        self.B1.clicked.connect(lambda: self.findfolder())

        self.FolderUpdate.clicked.connect(lambda: self.updatesample(self.newsample))
        
        self.Calibration.clicked.connect(lambda: self.calib_clicked())
        
        # self.Clear1.clicked.connect(lambda: self.Clear1_clicked())
        
        self.Clear2.clicked.connect(lambda: self.Clear2_clicked())

    def addpoints(self):
        count = self.ControlLayout.count()-1
        # pointBox = QtWidgets.QGroupBox('Point ' + str(count), self.ControlWidget)
        pointBox = QtWidgets.QGroupBox(self.ControlWidget)
        self.ControlLayout.insertWidget(count, pointBox)

        pointLayout = QtWidgets.QGridLayout(pointBox)
        for i in range(10):
            LE = QtWidgets.QLineEdit(pointBox)
            pointLayout.addWidget(LE, 0, i, 1, 1)
        CK1 = QtWidgets.QCheckBox(pointBox)
        pointLayout.addWidget(CK1, 0, 10, 1, 1)
        Btn1 =  QtWidgets.QPushButton('Select',pointBox)
        pointLayout.addWidget(Btn1, 0, 11, 1, 1)
        CK2 = QtWidgets.QCheckBox(pointBox)
        pointLayout.addWidget(CK2, 0, 12, 1, 1)
        self.selgroup.addButton(Btn1)
        Btn3 =  QtWidgets.QPushButton('Move',pointBox)
        pointLayout.addWidget(Btn3, 0, 13, 1, 1)
        self.movgroup.addButton(Btn3)
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
    
    def selgroup_clicked(self, button):
        # print(button.parent().children())
        
        X = epics.caget('13BMC:m44.VAL')
        Y = epics.caget('13BMC:m45.VAL')
        Z = epics.caget('13BMC:m46.VAL')
        strX = "{0:.3f}".format(X)
        strY = "{0:.3f}".format(Y)
        strZ = "{0:.3f}".format(Z)
        button.parent().children()[8].setText(strX)
        button.parent().children()[9].setText(strY)
        button.parent().children()[10].setText(strZ)

   
    def Datacol_clicked(self):
        
        boxlist = self.ControlWidget.children()[1::]
        # Initialization
        self.warn1.setText('')
        self.warn2.setText('')
        self.warn3.setText('')
        self.warn4.setText('')
        self.warn6.setText('')
        self.warn8.setText('')
        for item in boxlist:
            for i in range(2,11):
                item.children()[i].setStyleSheet('background-color: white')
        flgon = 1
        
        # Number check, check if each text is a number
        for item in boxlist:
            if item.children()[13].isChecked() == True:
                for i in range(2,11):
                    try:
                        float(item.children()[i].text())
                    except:
                        item.children()[i].setStyleSheet('background-color: red')
                        flgon = 0
                
                if flgon:
                    # print(flgon)
                    if float(item.children()[6].text()).is_integer() == 0:
                        item.children()[6].setStyleSheet('background-color: red')
                        flgon = 0
                    # print(flgon)
                        
       
        if flgon:
            for item in boxlist:
                if item.children()[13].isChecked() == True:
                    flgon1=self.HLLL(item.children()[2], self.warn1, 37, flgon)
                    flgon2=self.HLLL(item.children()[3], self.warn2, 38, flgon)
                    flgon3=self.HLLL(item.children()[4], self.warn3, 33, flgon)
                    flgon4=self.HLLL(item.children()[5], self.warn4, 33, flgon)
                    flgon5=self.HLLL(item.children()[8], self.warn8, 44, flgon)
                    flgon6=self.HLLL(item.children()[9], self.warn8, 45, flgon)
                    flgon7=self.HLLL(item.children()[10], self.warn8, 46, flgon)
                    
                    flgon8 = self.speedwarning(item.children()[7], self.warn6, item.children()[4], item.children()[5], item.children()[6], flgon)
                    
                    flgon = flgon1*flgon2*flgon3*flgon4*flgon5*flgon6*flgon7*flgon8

        
        # msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, 'Checktime', 'Select')
        # ret =msg.question(msg, title, text)
        if flgon:
            
            # Estimate time start
            Txrd = 0
            for item in boxlist:
                if item.children()[13].isChecked() == True:
                    Txrd = Txrd + 11
                    if item.children()[11].isChecked() == True:
                        Txrd = Txrd + 5
                    Nstep = float(item.children()[6].text())
                    Texpo = float(item.children()[7].text())
                    Txrd = Txrd + Nstep*Texpo
            
            WarnTxt = "Estimated XRD time in minutes: " + str(round(Txrd/60))
            
            
            # Estimate time end
            
            ret = QtWidgets.QMessageBox.question(self, 'MessageBox', WarnTxt, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            # print(self.ControlWidget.children()[1::])
            if ret == QtWidgets.QMessageBox.Yes:
                
                self.L6.setStyleSheet('color: red')
                self.L6.setText('BUSY')
                QtWidgets.QApplication.processEvents()
                
                boxlist = self.ControlWidget.children()[1::]
                for item in boxlist:
                    # print(item.children())
                    if item.children()[13].isChecked() == True:
                        self.Mv_click(item.children()[8],item.children()[9],item.children()[10], item.children()[1], self.LogL1, 'templog.txt')
                        self.PointCol(item.children())
                        # item.children()[1].setText(dummystr2)
                        item.children()[13].setChecked(0)
                        
                self.L6.setStyleSheet('color: green')
                self.L6.setText('DONE')
                    
    def PointCol(self, group):
        # group[1].setText(dummystr2)
        Delt = group[2]
        Nu = group[3]
        KphiS = group[4]
        KphiE = group[5]
        StpN = group[6]
        TimNE = group[7]
        self.Detmov(Delt, Nu)
        xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
        kphivelo = epics.caget('13BMC:m33.VELO')
        kphiini = epics.caget('13BMC:m33.VAL')
        cmdcon = "xtal kphi " + KphiS.text()+' '+ KphiE.text()+' '+ str(int(StpN.text()))+' '+ TimNE.text()
        eval("xtalcmd.executeCommand(\"%s\")" % cmdcon)
        Ttem = np.abs(kphiini-float(KphiS.text()))/kphivelo + float(TimNE.text())*float(StpN.text()) + 3.0
        time.sleep(Ttem)
        if (int(StpN.text())>1) and (group[11].isChecked() == True):
            time.sleep(2.0)
            DummyPath = SpecVariable.SpecVariable('SCANLOG_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
            DummyN = SpecVariable.SpecVariable('SCAN_N', 'corvette.cars.aps.anl.gov:6780').getValue()
            DumS = 'S'+(3-len(str(DummyN)))*'0'+str(DummyN)+'/'
            L = re.split('/', DummyPath)
            # For Win10 system
            FL = '//cars6/data/'+ L[5]+'/'+ L[6]+'/'+ L[7]+'/'+ L[8]+'/'+ L[9]+'/'+ L[10]+'/'+ L[11]+'/images/'+ L[13]+'/'+DumS
            files = []
            # r=root, d=directories, f = files
            for r, d, f in os.walk(FL):
                for file in f:
                    if '.cbf' in file:
                        files.append(os.path.join(r, file))
                    elif '.tif' in file:
                        files.append(os.path.join(r, file))
            img = fabio.open(files[0])
            for file in files[1:]:
                data = fabio.open(file).data
                img.data = img.data+data
            for xi in range(1043):
                for xj in range(981):
                    if img.data[xi, xj] <0:
                        img.data[xi, xj] = -1
            IML = FL+'sum.cbf'
            img.write(IML)
        self.lastscan(self.LogL1, 'templog.txt')
    

    def HLLL(self, widget, widget2, Nmot, flg):
        
        if flg:
            prefix = '13BMC:m'+str(Nmot)
            HLM = epics.caget(prefix+'.HLM')
            # print(HLM)
            LLM = epics.caget(prefix+'.LLM')
            # print(LLM)
            num1 = float(widget.text())
            if num1 > HLM:
                widget2.setText('high lim')
                widget2.setStyleSheet('color: red')
                widget.setStyleSheet('background-color: red')
                return flg*0
            elif num1 < LLM:
                widget2.setText('low lim')
                widget2.setStyleSheet('color: red')
                widget.setStyleSheet('background-color: red')
                return flg*0
            else:
                widget2.setText('')
                return flg        

    def speedwarning(self, widget1, widget2, widget3, widget4, widget5, flg):
        # w1: time, w2: label, w3: kphistart, w4: kihiend, w5: num_of_step
        if flg:
            tim0 = widget1.text()
            kphi0 = widget3.text()
            kphi1 = widget4.text()
            stp2 = widget5.text()
            try:
                tim1 = float(tim0)
                kphi10 = float(kphi0)
                kphi11 = float(kphi1)
                stp12 = float(stp2)
                spd = (kphi11-kphi10)/stp12/tim1
                if tim1 < 0.01:
                    widget2.setText('too fast')
                    widget2.setStyleSheet('color: red')
                    widget1.setStyleSheet('background-color: red')
                    return flg*0
                elif spd > float(epics.caget('13BMC:m33.VMAX')):
                    widget2.setText('too fast')
                    widget2.setStyleSheet('color: red')
                    widget1.setStyleSheet('background-color: red')
                    return flg*0
                else:
                    widget2.setText('')
                    return flg
            except:
                widget2.setText('wrong')
                widget2.setStyleSheet('color: red')
                return flg*0            

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
        Ttem = max(np.abs(dl1-dl0)/dlV,np.abs(nu1-nu0)/nuV)+4.0
        time.sleep(Ttem)
        xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
        eval("xtalcmd.executeCommand(\"%s\")" % 'wh')
        time.sleep(2)
        
    def lastscan(self, widget1, tempfile):
        # only use after one scan is done. Newsample command creates a new logPath.
        LogPath = SpecVariable.SpecVariable('SCANLOG_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        FilePath = SpecVariable.SpecVariable('SCANLOG_FILE', 'corvette.cars.aps.anl.gov:6780').getValue()
        len1 = len(LogPath)
        dummy = FilePath[len1:-4]
        dummy1 = re.split('_', dummy)
        cmdcon = time.asctime()+'\n    '+ dummy1[2] +' done, saved in folder: '+ dummy1[0]+'_'+dummy1[1]+'\n'
        f = open(tempfile, 'a+')
        f.seek(0)
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
        cmdcon = time.asctime()+'\n    New data will be saved in folder: ' + dummy + '\n'
        f = open(tempfile, 'a+')
        f.seek(0)
        dummy2 = f.read()
        f.close()
        os.remove(tempfile)
        dummy3 = cmdcon + dummy2
        f = open(tempfile, 'a+')
        f.write(dummy3)
        f.close()
        widget1.setText(dummy3)
        
    def findfolder(self):
        ProjPath = SpecVariable.SpecVariable('STARTUP_PROJECT_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        temp = ProjPath[25::]
        temp1 = 'T:'+temp+'images/'
        self.FolderN.setText(temp1)
        time.sleep(0.3)
    
    def updatesample(self, newsample):
        SamNam = newsample.text()
        self.warn7.setText('')
        if (SamNam.find('_')!=-1) or (SamNam.find('/')!=-1) or (SamNam.find('.')!=-1) or (SamNam.find(' ')!=-1):
            self.warn7.setText('Invalid symbol: _ / . space')
            self.warn7.setStyleSheet('color: red')
        else:
            xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
            cmdcon = 'newsample '+SamNam
            eval("xtalcmd.executeCommand(\"%s\")" % cmdcon)
            time.sleep(0.2)
            self.nextscan(self.LogL1, 'templog.txt')
            
    def Mv_click(self, widget1, widget2, widget3, widget4, widget5, tempfile):
        # widget1-3: X, Y, Z. widget4: sample label, widget5: logzone
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
        Ttem = max(np.abs(X-X0)/XV,np.abs(Y-Y0)/YV, np.abs(Z-Z0)/ZV)+1.0
        time.sleep(Ttem)
        cmdcon = time.asctime()+'\n    Move to ' + widget4.text()+': '+strX+', '+strY+', '+strZ + '\n'
        f = open(tempfile, 'a+')
        f.seek(0)
        dummy2 = f.read()
        f.close()
        os.remove(tempfile)
        dummy3 = cmdcon + dummy2
        f = open(tempfile, 'a+')
        f.write(dummy3)
        f.close()
        widget5.setText(dummy3)
        time.sleep(1)

    def Clear2_clicked(self):
        self.LogL1.setText('')
        try:
            os.remove('templog.txt')
        except:
            pass
        f = open('templog.txt','w')
        f.write('')
        f.close()
    
    def calib_clicked(self):
        self.dialog = calibUI(self)
        self.dialog.show()



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
    
    xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
    eval("xtalcmd.executeCommand(\"%s\")" % 'wh')
    eval("xtalcmd.executeCommand(\"%s\")" % 'qdo /home/specadm/macros_gsecars/single_scan.mac')
    eval("xtalcmd.executeCommand(\"%s\")" % 'ton')
    time.sleep(0.3)
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.resize(1480,600)

    mainwindow.show()
    app.exec()

if __name__ == '__main__':
    main()