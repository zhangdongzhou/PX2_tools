# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:51:17 2024

@author: Dongzhou_X99
"""
import sys
import os
# import matplotlib.pyplot as plt
import matplotlib
from PyQt5 import QtCore, QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import (
   FigureCanvasQTAgg as FigureCanvas,
   NavigationToolbar2QT)
from matplotlib.figure import Figure

import numpy as np
import time
import re
from epics import caget, caput

matplotlib.use('Qt5Agg')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setWindowTitle("Scan & View, but in python")
        self.CW = QtWidgets.QWidget(self)
        self.CWLayout = QtWidgets.QGridLayout(self.CW)
        
        # top region
        self.L1 = QtWidgets.QLabel("Motor name", self.CW)
        self.L1.setFont(font)
        self.CWLayout.addWidget(self.L1, 0, 0, 1, 1)
        
        self.L2 = QtWidgets.QLabel("Position", self.CW)
        self.L2.setFont(font)
        self.CWLayout.addWidget(self.L2, 0, 1, 1, 1)
        
        self.L3 = QtWidgets.QLabel("Range", self.CW)
        self.L3.setFont(font)
        self.CWLayout.addWidget(self.L3, 0, 2, 1, 1)
        
        self.L4 = QtWidgets.QLabel("Step size", self.CW)
        self.L4.setFont(font)
        self.CWLayout.addWidget(self.L4, 0, 3, 1, 1)
        
        self.L5 = QtWidgets.QLabel("# Points", self.CW)
        self.L5.setFont(font)
        self.CWLayout.addWidget(self.L5, 0, 4, 1, 1)
        
        self.L6 = QtWidgets.QLabel("Time", self.CW)
        self.L6.setFont(font)
        self.CWLayout.addWidget(self.L6, 0, 5, 1, 1)
        
        self.L7 = QtWidgets.QLabel("Total time", self.CW)
        self.L7.setFont(font)
        self.CWLayout.addWidget(self.L7, 0, 6, 1, 1)
        
        self.MotorN = QtWidgets.QLineEdit('13BMC:m44', self.CW)
        self.CWLayout.addWidget(self.MotorN, 1, 0, 1, 1)
        
        self.MotorP = QtWidgets.QLabel('', self.CW)
        self.MotorP.setFrameShape(QtWidgets.QFrame.Panel)
        self.MotorP.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CWLayout.addWidget(self.MotorP, 1, 1, 1, 1)
        
        self.MotorR = QtWidgets.QLineEdit('0.05', self.CW)
        self.CWLayout.addWidget(self.MotorR, 1, 2, 1, 1)
        
        self.Step = QtWidgets.QLabel('', self.CW)
        self.Step.setFrameShape(QtWidgets.QFrame.Panel)
        self.Step.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CWLayout.addWidget(self.Step, 1, 3, 1, 1)
        
        self.NoP = QtWidgets.QLineEdit('11', self.CW)
        self.CWLayout.addWidget(self.NoP, 1, 4, 1, 1)
        
        self.TpP = QtWidgets.QLineEdit('0.5', self.CW)
        self.CWLayout.addWidget(self.TpP, 1, 5, 1, 1)
        
        self.TtP = QtWidgets.QLabel('', self.CW)
        self.TtP.setFrameShape(QtWidgets.QFrame.Panel)
        self.TtP.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CWLayout.addWidget(self.TtP, 1, 6, 1, 1)
        
        self.L8 = QtWidgets.QLabel("Scaler name", self.CW)
        self.L8.setFont(font)
        self.CWLayout.addWidget(self.L8, 2, 0, 1, 1)
        
        # self.L9 = QtWidgets.QLabel("Directory", self.CW)
        # self.L9.setFont(font)
        # self.CWLayout.addWidget(self.L9, 2, 3, 1, 5)
        
        self.DirectoryB = QtWidgets.QPushButton('Directory', self.CW)
        self.DirectoryB.setFont(QtGui.QFont('Arial', 14))
        self.CWLayout.addWidget(self.DirectoryB, 2, 3, 1, 1)
        
        self.L10 = QtWidgets.QLabel("Next File", self.CW)
        self.L10.setFont(font)
        self.CWLayout.addWidget(self.L10, 2, 6, 1, 1)
        
        self.ScalerN = QtWidgets.QLineEdit('13BMC:scaler1', self.CW)
        self.CWLayout.addWidget(self.ScalerN, 3, 0, 1, 1)
        
        self.Dir = QtWidgets.QLineEdit('C:/Users/dzzhang/', self.CW)
        self.CWLayout.addWidget(self.Dir, 3, 1, 1, 5)
        
        self.File = QtWidgets.QLineEdit('scan_0', self.CW)
        self.File.setToolTip('Format: string_number')
        self.CWLayout.addWidget(self.File, 3, 6, 1, 1)
        
        self.ScanB = QtWidgets.QPushButton('Scan', self.CW)
        self.ScanB.setFont(QtGui.QFont('Arial', 15))
        self.ScanB.setStyleSheet('color: green')
        self.CWLayout.addWidget(self.ScanB, 0, 7, 1, 1)
        
        self.AbortB = QtWidgets.QPushButton('Abort', self.CW)
        self.AbortB.setStyleSheet('color: red')
        self.CWLayout.addWidget(self.AbortB, 3, 7, 1, 1)
        
        self.NextFile = QtWidgets.QPushButton('>', self.CW)
        self.CWLayout.addWidget(self.NextFile, 2, 7, 1, 1)
        
        self.PreviousFile = QtWidgets.QPushButton('<', self.CW)
        self.CWLayout.addWidget(self.PreviousFile, 2, 5, 1, 1)
        
        ############ Bottom section
        self.L11 = QtWidgets.QLabel("Shutter", self.CW)
        self.L11.setFont(font)
        self.CWLayout.addWidget(self.L11, 9, 0, 1, 1)
        
        self.Shutter = QtWidgets.QLineEdit('13BMC:BenchAtten1', self.CW)
        self.CWLayout.addWidget(self.Shutter, 10, 0, 1, 1)
        
        self.L12 = QtWidgets.QLabel("Channel", self.CW)
        self.L12.setFont(font)
        self.CWLayout.addWidget(self.L12, 9, 1, 1, 1)
        
        self.ScalerC = QtWidgets.QLineEdit('S2', self.CW)
        self.CWLayout.addWidget(self.ScalerC, 10, 1, 1, 1)
        
        self.PositionB = QtWidgets.QPushButton('Position', self.CW)
        self.CWLayout.addWidget(self.PositionB, 9, 2, 1, 1)
        
        self.CenterB = QtWidgets.QPushButton('Center', self.CW)
        self.CenterB.setFont(QtGui.QFont('Arial', 15))
        self.CenterB.setStyleSheet('color: blue')
        self.CWLayout.addWidget(self.CenterB, 9, 3, 1, 1)
        
        self.MoveB = QtWidgets.QPushButton('Move', self.CW)
        self.MoveB.setFont(QtGui.QFont('Arial', 15))
        self.MoveB.setStyleSheet('color: blue')
        self.CWLayout.addWidget(self.MoveB, 10,2, 1, 1)
        
        self.L14 = QtWidgets.QLabel("", self.CW) # move motor label
        self.L14.setFont(font)
        self.CWLayout.addWidget(self.L14, 10, 3, 1, 1)
        
        self.L13 = QtWidgets.QLabel("", self.CW) # move motor value
        self.L13.setFont(font)
        self.CWLayout.addWidget(self.L13, 10, 4, 1, 1)
        
        # Figure
        
        self.groupbox = QtWidgets.QGroupBox()
        self.lay_2 = QtWidgets.QVBoxLayout()
        
        # x_axis = np.loadtxt('dummy.txt')[:,0]
        # y_axis = np.loadtxt('dummy.txt')[:,1]
        x_axis = np.array([0])
        y_axis = np.array([0])

        self.area_plot = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar2QT(self.area_plot, self)
       
        self.area_plot.figure.clf() #remove the initial axis labels
        self.figure = self.area_plot.figure
        self.ax = self.figure.add_subplot(111) #add subplot, retrieve axis object
       
        self.canvasp = self.figure.canvas
        self.ax.plot(x_axis, y_axis)

        self.lay_2.addWidget(toolbar)
        self.lay_2.addWidget(self.area_plot)
        self.groupbox.setLayout(self.lay_2)
        self.CWLayout.addWidget(self.groupbox, 4, 0, 5, 8)
        
        
        self.setLayout(self.lay_2)
        # self.X = []
        # self.Y = []
        self.globalflag = 1
        # self.data = np.loadtxt('dummy.txt')
        self.readlog()
        try:
            self.plotscan()
        except:
            pass


        self.setCentralWidget(self.CW)        

        # self.checkThreadTimer = QtCore.QTimer(self)
        # print(self.checkThreadTimer.isActive())
        # self.checkThreadTimer.start()
        # self.checkThreadTimer.setInterval(500) #.5 seconds
        # self.checkThreadTimer.setSingleShot(False)
        # self.checkThreadTimer.timeout.connect(self.readListValues)
        # self.checkThreadTimer.timeout.connect(self.graph_update)
        # self.slider.valueChanged[int].connect(self.graph_uptade)
        # self.checkThreadTimer.stop()
       
        # self.canvasp.mpl_connect('button_press_event', self.one_click)
        # self.ScalerN.returnPressed.connect(self.ScalerNupdate)
        self.MotorR.returnPressed.connect(self.MotorRupdate)
        self.NoP.returnPressed.connect(self.NoPupdate)
        self.ScanB.clicked.connect(self.scanclick)
        self.DirectoryB.clicked.connect(self.selectfolder)
        self.MotorN.returnPressed.connect(self.motorenter)
        self.NextFile.clicked.connect(self.increaseplot)
        self.PreviousFile.clicked.connect(self.decreaseplot)
        self.AbortB.clicked.connect(self.abortclick)
        self.PositionB.clicked.connect(self.oneclick)
        self.CenterB.clicked.connect(self.twoclick)
        self.MoveB.clicked.connect(self.MoveFun)
        self.TpP.returnPressed.connect(self.TtPupdate)

    # def ScalerNupdate(self):
        # print(self.ScalerN.text())
    

    def graph_update(self, x_axis, y_axis):
        # self.checkThreadTimer.start()
        QtWidgets.QApplication.processEvents()
        # self.X.append(self.data[self.i,0])
        # self.Y.append(self.data[self.i,1])
        # x_axis = self.X
        # y_axis = self.Y
        # time.sleep(0.5)
        # print(time.time())
        self.ax.cla()
        self.ax.plot(x_axis, y_axis, 'r')
        xlabel = self.MotorN.text()+'.RBV'
        ylabel = self.ScalerN.text()+'.'+self.ScalerC.text()
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(self.File.text())
        self.area_plot.figure.canvas.draw()
       # if self.dataWasReadEvent.is_set():
           # self.dataWasReadEvent.clear() 
       # self.checkThreadTimer.start()
       # while self.i<11:
       #      # self.checkThreadTimer.start()
       #      QtWidgets.QApplication.processEvents()
       #      self.X.append(self.data[self.i,0])
       #      self.Y.append(self.data[self.i,1])
       #      x_axis = self.X
       #      y_axis = self.Y
       #      time.sleep(0.5)
       #      print(time.time())
       #      self.ax.cla()
       #      self.ax.plot(x_axis, y_axis, 'r')
       #      self.area_plot.figure.canvas.draw()
           
       #      self.i = self.i+1
            # self.canvas.draw()
            # self.canvas.repaint()
        # self.checkThreadTimer.stop()
        
    def oneclick(self):
        self.plotscan()
        self.clickcount = 0
        self.clickcountlimit = 1
        # self.L13.setText('aaaaaa')
        self.value = []
        self.cidpress = self.canvasp.mpl_connect('button_press_event', self.one_click)
        # print(self.value)
        # a = self.on_click('button_press_event')
        # print(a)
        if self.clickcount > 0:
            # self.L13.setText(str(np.mean(self.value)))
            # print(self.value)
            # self.L13.setText(str(self.value))
            self.canvasp.mpl_disconnect(self.cidpress)
    
    def twoclick(self):
        self.plotscan()
        self.clickcount = 0
        self.clickcountlimit = 2
        # self.L13.setText('aaaaaa')
        self.value = []
        self.cidpress = self.canvasp.mpl_connect('button_press_event', self.one_click)
        # print(self.value)
        # a = self.on_click('button_press_event')
        # print(a)
        if self.clickcount > 0:
            # self.L13.setText(str(np.mean(self.value)))
            # print(self.value)
            # self.L13.setText(str(self.value))
            self.canvasp.mpl_disconnect(self.cidpress)
        
    def one_click(self, event):
          # self.canvasp.mpl_connect('button_press_event', self)
          # print(self.i)
          if self.clickcount < self.clickcountlimit:
              if event.inaxes is not None:
                  x, y = event.xdata, event.ydata
                  # print(x, y)
                  x0 = self.ax.get_xlim()[0]
                  x1 = self.ax.get_xlim()[1]
                  y0 = self.ax.get_ylim()[0]
                  y1 = self.ax.get_ylim()[1]
                  self.ax.plot([x0,x1],[y,y],'r-')
                  self.ax.plot([x,x],[y0,y1],'r-')
                  self.ax.set_xlim([x0, x1])
                  self.ax.set_ylim([y0, y1])
                  self.area_plot.figure.canvas.draw()
                  self.clickcount = self.clickcount+1
                  
                  self.value.append(x)
                  # self.L13.setText(np.mean(self.value))
                  # print(self.value)
          else:
              Motor = self.ax.get_xlabel()[0:-4] # 13BMC:m44, no ".VAL"
              Motorval = Motor + '.VAL'
              MotorN = Motor + ' to'
              self.L14.setText(MotorN)
              self.L13.setText(str(round(np.mean(self.value),3)))
                  # print(x1)
                  
    def MoveFun(self):
        Motor = self.ax.get_xlabel()[0:-4] # 13BMC:m44, no ".VAL"
        Motorval = Motor + '.VAL'
        MotorN = Motor + ' to'
        self.L14.setText(MotorN)
        val = round(np.mean(self.value),4)
        self.L13.setText(str(val))
        msg = QtWidgets.QMessageBox()
        msg.setText('Move '+MotorN+' '+str(val)+'?')
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        retval = msg.exec()
        if retval == QtWidgets.QMessageBox.Yes:
            caput(Motorval, val)
    
    def checklim(self):
        motor = self.MotorN.text()
        try:
            RBV = caget(motor+'.RBV')
            HLM = caget(motor+'.HLM')
            LLM = caget(motor+'.LLM')
            cen = float(self.MotorP.text())
            ran = float(self.MotorR.text())
        except:
            self.globalflag = 0
        else:
            if cen+ran > HLM:
                self.MotorR.setText("high limit")
                self.MotorR.setStyleSheet("color: red;")
                self.globalflag = 0
            if cen-ran < LLM:
                self.MotorR.setText("low limit")
                self.MotorR.setStyleSheet("color: red;")
                self.globalflag = 0
    
    def updatestepsize(self):
        try:
            ran = float(self.MotorR.text())
            nop = float(self.NoP.text())
        except:
            self.Step.setText('')
            self.globalflag = 0
        else:
            if int(nop) > 1:
                stp = round(ran*2/(nop-1),4)
                self.Step.setText(str(stp))
            else:
                self.Step.setText('')
                self.globalflag = 0
                
    def MotorRupdate(self):
        self.MotorR.setStyleSheet("color: black;")
        try:
            val = float(self.MotorR.text())
        except:
            # self.MotorR.setStyleSheet("color: red;")
            self.MotorR.setText('')
            self.Step.setText('')
            self.globalflag = 0
        else:
            self.checklim()
            self.updatestepsize()
            self.TtPupdate()
            
    def NoPupdate(self):
        self.NoP.setStyleSheet("color: black;")
        try:
            val = int(self.NoP.text())
        except:
            # self.NoP.setStyleSheet("color: red;")
            self.NoP.setText('')
            self.Step.setText('')
            self.globalflag = 0
        else:
            self.checklim()
            if val <= 1:
                self.NoP.setStyleSheet("color: red;")
                self.NoP.setText('must >1')
                self.globalflag = 0
            else:
                self.updatestepsize()
                self.TtPupdate()
    
    # def checktime(self):
        
            

    def TtPupdate(self):
        self.TpP.setStyleSheet("color: black;")
        try:
            tim = float(self.TpP.text())
        except:
            self.TpP.setStyleSheet("color: red;")
        else:
            if tim <= 0:
                self.TpP.setStyleSheet("color: red;")
            else:
                motorS = self.MotorN.text()+'.VELO'
                speed = caget(motorS)
                motorA = self.MotorN.text()+'.ACCL'
                acce = caget(motorA)
                ran = float(self.MotorR.text())
                nop = float(self.NoP.text())
                ttp = 4*ran/speed+nop*(tim+0.15)+(nop+1)*(acce+0.15)
                self.TtP.setText(str(round(ttp,2)))
    
    def selectfolder(self):
        directory = QtWidgets.QFileDialog().getExistingDirectory(None,'folder','C:/Users/dzzhang/')
        self.Dir.setText(directory+'/')
    
    def movemotortime(self,end):
        motor = self.MotorN.text()+'.VAL'
        start = caget(motor)
        motorS = self.MotorN.text()+'.VELO'
        speed = caget(motorS)
        motorA = self.MotorN.text()+'.ACCL'
        acce = caget(motorA)
        Ttotal = np.abs(end-start)/speed+acce
        return Ttotal
    
    def movemotor(self, end):
        Ttotal = self.movemotortime(end)
        motor = self.MotorN.text()+'.VAL'
        caput(motor, end)
        time.sleep(Ttotal+0.15)
        
    def count(self, Tstep):
        scalerT = self.ScalerN.text()+'.TP'
        caput(scalerT, Tstep)
        scaler = self.ScalerN.text()+'.CNT'
        caput(scaler, 1)
        time.sleep(Tstep+0.15)
        scalerV = self.ScalerN.text()+'.'+self.ScalerC.text()
        return (caget(scalerV))

    def writeascii(self, x_axis, y_axis):
        asciiN = self.Dir.text()+self.File.text()
        motorN = self.MotorN.text()+'.RBV'
        scalerN = self.ScalerN.text()+'.'+self.ScalerC.text()
        comment = motorN + '\n'+scalerN
        data0 = np.array([x_axis])
        data1 = np.array([y_axis])
        data = np.concatenate((data0.T,data1.T),axis=1)
        np.savetxt(asciiN,data,header=comment)
    
    def readascii(self, asciiN):
        data = np.loadtxt(asciiN)
        data0 = data[:,0]
        data1 = data[:,1]
        f=open(asciiN,'r')
        xlabel = f.readline()[2:-1]
        ylabel = f.readline()[2:-1]
        return(data0, data1, xlabel, ylabel)
    
    def plotscan(self):
        asciiN = self.Dir.text()+self.File.text()
        (x_axis, y_axis, xlabel, ylabel) = self.readascii(asciiN)
        self.ax.cla()
        self.ax.plot(x_axis, y_axis, 'b')
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(self.File.text())
        self.area_plot.figure.canvas.draw()
    
    def increasescan(self):
        scanN = self.File.text()
        [prefix,ind] = re.split('_',scanN)
        newind = str(int(ind)+1)
        newscanN = prefix+'_'+newind
        asciiN = self.Dir.text()+newscanN
        if os.path.exists(asciiN) == False:
            self.File.setText(newscanN)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText('File exists, overwrite?')
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            retval = msg.exec()
            if retval == QtWidgets.QMessageBox.Yes:
                self.File.setText(newscanN)
            else:
                self.globalflag = 0    
            
    def increaseplot(self):
        scanN = self.File.text()
        [prefix,ind] = re.split('_',scanN)
        newind = str(int(ind)+1)
        newscanN = prefix+'_'+newind
        asciiN = self.Dir.text()+newscanN
        if os.path.exists(asciiN) == True:
            self.File.setText(newscanN)
            self.plotscan()
    
    def decreaseplot(self):
        scanN = self.File.text()
        [prefix,ind] = re.split('_',scanN)
        newind = str(int(ind)-1)
        newscanN = prefix+'_'+newind
        asciiN = self.Dir.text()+newscanN
        if os.path.exists(asciiN) == True:
            self.File.setText(newscanN)
            self.plotscan()

    def scanclick(self):
        self.globalflag = 1
        self.checklim()
        self.MotorRupdate()
        self.NoPupdate()
        self.increasescan()
        shutter = self.Shutter.text()
        if self.globalflag == 1:
            caput(shutter,1)
            xcen = float(self.MotorP.text())
            xstart = xcen - float(self.MotorR.text())
            xend = xcen + float(self.MotorR.text())
            Npts = int(self.NoP.text())
            x_list = np.linspace(xstart, xend, num=Npts)
            x_axis = []
            y_axis = []
            tstep = float(self.TpP.text())
            for i in range(Npts):
                if self.globalflag == 1:
                    xgoal = x_list[i]
                    self.movemotor(xgoal)
                    xgoal1 = caget(self.MotorN.text()+'.RBV')
                    x_axis.append(xgoal1)
                    ygoal = self.count(tstep)
                    # print(ygoal)
                    y_axis.append(ygoal)
                    self.graph_update(x_axis, y_axis)
            caput(shutter,0)
            self.movemotor(xcen)
            self.writeascii(x_axis, y_axis)
            self.plotscan()
            self.savelog()
        else:
            self.plotscan()
            self.globalflag = 1
    
    def savelog(self):
        f = open('Scanwlog','w')
        tmp = self.MotorN.text()+'\n'
        f.write(tmp)
        tmp = self.MotorR.text()+'\n'
        f.write(tmp)
        tmp = self.NoP.text()+'\n'
        f.write(tmp)
        tmp = self.TpP.text()+'\n'
        f.write(tmp)
        tmp = self.ScalerN.text()+'\n'
        f.write(tmp)
        tmp = self.Dir.text()+'\n'
        f.write(tmp)
        tmp = self.File.text()+'\n'
        f.write(tmp)
        tmp = self.Shutter.text()+'\n'
        f.write(tmp)
        tmp = self.ScalerC.text()+'\n'
        f.write(tmp)
        f.close()
    
    def readlog(self):
        f = open('Scanwlog','r')
        tmp = f.readline()[0:-1]
        self.MotorN.setText(tmp)
        tmp = f.readline()[0:-1]
        self.MotorR.setText(tmp)
        tmp = f.readline()[0:-1]
        self.NoP.setText(tmp)
        tmp = f.readline()[0:-1]
        self.TpP.setText(tmp)
        tmp = f.readline()[0:-1]
        self.ScalerN.setText(tmp)
        tmp = f.readline()[0:-1]
        self.Dir.setText(tmp)
        tmp = f.readline()[0:-1]
        self.File.setText(tmp)
        tmp = f.readline()[0:-1]
        self.Shutter.setText(tmp)
        tmp = f.readline()[0:-1]
        self.ScalerC.setText(tmp)
        f.close()
    
    def motorenter(self):
        motorN = self.MotorN.text()+'.VAL'
        val = caget(motorN)
        self.MotorP.setText(str(round(val,3)))
        self.MotorRupdate()
    
    def abortclick(self):
        self.globalflag = 0
        shutter = self.Shutter.text()
        caput(shutter,0)
        if self.MotorP.text() !='':
            xcen = float(self.MotorP.text())
            self.movemotor(xcen)

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.resize(700,800)

    mainwindow.show()
    app.exec()

if __name__ == '__main__':
    main()