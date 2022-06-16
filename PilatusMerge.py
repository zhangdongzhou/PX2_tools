# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 22:44:28 2022

@author: DongzhouX470
"""


from PyQt5 import QtCore, QtWidgets
import sys
import matplotlib.pyplot as plt
import fabio
import pyFAI

import numpy as np

def R1(x):
    return np.array([[1, 0, 0],
               [0, np.cos(x), -np.sin(x)],
               [0, np.sin(x), np.cos(x)]])

def R2(x):
    return np.array([[np.cos(x), 0, np.sin(x)],
               [0, 1, 0],
               [-np.sin(x), 0, np.cos(x)]])

def R3(x):
    return np.array([[np.cos(x), -np.sin(x),0],
               [np.sin(x), np.cos(x), 0],
               [0,0,1]])

def Rtth(x):
    return np.array([[np.cos(x), 0, np.sin(x)],
               [0, 1, 0],
               [-np.sin(x), 0, np.cos(x)]])

def Rchi(x):
    return np.array([[np.cos(x), -np.sin(x),0],
               [np.sin(x), np.cos(x), 0],
               [0,0,1]])

##########################################

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
    

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
####################################

        self.originfile = QtWidgets.QPushButton(self.centralwidget)
        self.originfile.setGeometry(QtCore.QRect(57, 40, 175, 35))
        self.originfile.setObjectName("file")
        self.originfile.setStyleSheet("background-color:rgb(111,180,219)")
        self.originfile.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  
            "QPushButton:hover{color:green}"  
            "QPushButton{border-radius:6px}"  
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  
        )


        self.originfileT = QtWidgets.QLabel(self.centralwidget)
        self.originfileT.setGeometry(QtCore.QRect(300, 40, 480, 35))
        self.originfileT.setObjectName("file")
        self.originfileT.setStyleSheet("background-color:rgb(240, 240, 240)")

#################################################

        self.originponi = QtWidgets.QPushButton(self.centralwidget)
        self.originponi.setGeometry(QtCore.QRect(57, 100, 175, 35))
        self.originponi.setObjectName("file")
        self.originponi.setStyleSheet("background-color:rgb(111,180,219)")
        self.originponi.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  
            "QPushButton:hover{color:green}"  
            "QPushButton{border-radius:6px}"  
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  
        )

        self.originponiT = QtWidgets.QLabel(self.centralwidget)
        self.originponiT.setGeometry(QtCore.QRect(300, 100, 480, 35))
        self.originponiT.setObjectName("file")
        self.originponiT.setStyleSheet("background-color:rgb(240, 240, 240)")

#################################################

        self.destinfile = QtWidgets.QPushButton(self.centralwidget)
        self.destinfile.setGeometry(QtCore.QRect(57, 160, 175, 35))
        self.destinfile.setObjectName("file")
        self.destinfile.setStyleSheet("background-color:rgb(111,180,219)")
        self.destinfile.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  
            "QPushButton:hover{color:green}"  
            "QPushButton{border-radius:6px}"  
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  
        )


        self.destinfileT = QtWidgets.QLabel(self.centralwidget)
        self.destinfileT.setGeometry(QtCore.QRect(300, 160, 480, 35))
        self.destinfileT.setObjectName("file")
        self.destinfileT.setStyleSheet("background-color:rgb(240, 240, 240)")

#################################################

        self.destinponi = QtWidgets.QPushButton(self.centralwidget)
        self.destinponi.setGeometry(QtCore.QRect(57, 220, 175, 35))
        self.destinponi.setObjectName("file")
        self.destinponi.setStyleSheet("background-color:rgb(111,180,219)")
        self.destinponi.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  #
            "QPushButton:hover{color:green}"  # 
            "QPushButton{border-radius:6px}"  # 
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  
        )

        self.destinponiT = QtWidgets.QLabel(self.centralwidget)
        self.destinponiT.setGeometry(QtCore.QRect(300, 220, 480, 35))
        self.destinponiT.setObjectName("file")
        self.destinponiT.setStyleSheet("background-color:rgb(240, 240, 240)")

#################################################


        self.outfolder = QtWidgets.QPushButton(self.centralwidget)
        self.outfolder.setGeometry(QtCore.QRect(57, 280, 175, 35))
        self.outfolder.setObjectName("file")
        self.outfolder.setStyleSheet("background-color:rgb(111,180,219)")
        self.outfolder.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  
            "QPushButton:hover{color:green}"  # 
            "QPushButton{border-radius:6px}"  #
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  
        )


        self.outfolderT = QtWidgets.QLabel(self.centralwidget)
        self.outfolderT.setGeometry(QtCore.QRect(300, 280, 480, 35))
        self.outfolderT.setObjectName("file")
        self.outfolderT.setStyleSheet("background-color:rgb(240, 240, 240)")

#################################################

        self.merge = QtWidgets.QPushButton(self.centralwidget)
        self.merge.setGeometry(QtCore.QRect(57, 340, 175, 40))
        self.merge.setObjectName("file")
        self.merge.setStyleSheet(
            "QPushButton{background-color:rgb(210,180, 111)}"  
            "QPushButton:hover{color:green}"  
            "QPushButton{border-radius:6px}"  
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  
        )

        self.mergeT = QtWidgets.QLabel(self.centralwidget)
        self.mergeT.setGeometry(QtCore.QRect(300, 340, 100, 40))
        self.mergeT.setObjectName("file")
        self.mergeT.setStyleSheet("background-color:rgb(240, 240, 240)")

#################################################

        self.prefixT = QtWidgets.QLabel(self.centralwidget)
        self.prefixT.setGeometry(QtCore.QRect(457, 340, 100, 40))
        self.prefixT.setObjectName("file")
        self.prefixT.setStyleSheet("background-color:rgb(240, 240, 240)")

        
        self.prefix = QtWidgets.QLineEdit(self.centralwidget)
        self.prefix.setGeometry(QtCore.QRect(580, 340, 200, 40))
#################################################


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
##################################################

        self.originfile.clicked.connect(self.originfilemsg)
        self.originponi.clicked.connect(self.originponimsg)
        self.destinfile.clicked.connect(self.destinfilemsg)
        self.destinponi.clicked.connect(self.destinponimsg)
        self.outfolder.clicked.connect(self.outfoldermsg)
        
        self.merge.clicked.connect(self.mergeF)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Merge Pilatus Images"))
        self.originfile.setText(_translate("MainWindow", "Origin Image"))
        self.originfileT.setText(_translate("MainWindow", ""))
        
        self.originponi.setText(_translate("MainWindow", "Origin poni"))
        self.originponiT.setText(_translate("MainWindow", ""))
        
        self.destinfile.setText(_translate("MainWindow", "Patch Image"))
        self.destinfileT.setText(_translate("MainWindow", ""))
        
        self.destinponi.setText(_translate("MainWindow", "Patch poni"))
        self.destinponiT.setText(_translate("MainWindow", ""))

        self.outfolder.setText(_translate("MainWindow", "Output folder"))
        self.outfolderT.setText(_translate("MainWindow", ""))
        
        self.merge.setText(_translate("MainWindow", "Merge!"))
        self.mergeT.setText(_translate("MainWindow", ""))
        
        self.prefixT.setText(_translate("MainWindow", "Sample Prefix"))
        self.prefix.setText(_translate("MainWindow", ""))

############################################

    def originfilemsg(self,Filepath):
        f = open('tmp1','r')
        Stmp = f.read()
        f.close()
        fileN,_filter = QtWidgets.QFileDialog.getOpenFileName(None,"Open origin image",Stmp)  
        self.originfileT.setText(fileN)
        f = open('tmp1','w')
        f.write(fileN)
        f.close()
        
    def originponimsg(self,Filepath):
        f = open('tmp2','r')
        Stmp = f.read()
        f.close()
        fileN,_filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open origin poni", Stmp, "(*.poni)")  
        self.originponiT.setText(fileN)
        f = open('tmp2','w')
        f.write(fileN)
        f.close()
        
    def destinfilemsg(self,Filepath):
        f = open('tmp3','r')
        Stmp = f.read()
        f.close()
        fileN,_filter = QtWidgets.QFileDialog.getOpenFileName(None,"open patch image", Stmp) 
        self.destinfileT.setText(fileN) 
        f = open('tmp3','w')
        f.write(fileN)
        f.close()
        
    def destinponimsg(self,Filepath):
        f = open('tmp4','r')
        Stmp = f.read()
        f.close()
        fileN,_filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open patch poni", Stmp, "(*.poni)") 
        self.destinponiT.setText(fileN)
        f = open('tmp4','w')
        f.write(fileN)
        f.close()

    def outfoldermsg(self,Filepath):
        f = open('tmp5','r')
        Stmp = f.read()
        f.close()
        fileN= QtWidgets.QFileDialog.getExistingDirectory(None, "Output folder", Stmp)  
        self.outfolderT.setText(fileN) 
        f = open('tmp5','w')
        f.write(fileN)
        f.close()
        
    def mergeF(self):

        plt.close('all')

        refImage = self.originfileT.text()
        padImage = self.destinfileT.text()
        refponi =  self.originponiT.text()
        padponi =  self.destinponiT.text()
        
        ai0=pyFAI.load(refponi)
        ai1=pyFAI.load(padponi)

        L = ai1.dist
        poni1 = ai1.poni2
        poni2 = ai1.poni1
        rot1 = -ai1.rot2
        rot2 = -ai1.rot1
        rot3 = ai1.rot3
        pix = ai1.pixel1

        img_file = refImage
        D0dataX = fabio.open(img_file).data
        D0data = np.flipud(D0dataX)
        
        MaxS = D0dataX.max()/100
        plt.figure('Origin')
        plt.imshow(D0dataX, vmin=0, vmax=MaxS)
        plt.show()


        img_file = padImage
        D1dataX = fabio.open(img_file).data
        D1data = np.flipud(D1dataX)

        plt.figure('Patch')
        plt.imshow(D1dataX, vmin=0, vmax=MaxS)
        plt.show()


        tth0M = np.radians(ai0.array_from_unit(unit="2th_deg"))
        chi0M = ai0.chiArray()


        Dwdata =np.zeros(D1data.shape, dtype=np.int32)

        for i in range(np.shape(Dwdata)[0]):
            for j in range(np.shape(Dwdata)[1]):
                Dwdata[i,j] = -1
                if D0data[i,j]>0:
                    Dwdata[i,j] = D0data[i,j]
                else:
                    
                    tth0 = tth0M[i,j]
                    chi0 = chi0M[i,j]
                    
                    
                    Dirt = np.matmul(np.matmul(Rchi(chi0), Rtth(tth0)), np.array([[0.0],[0.0],[1.0]]))
                    Rtotp = np.matmul(R1(rot1), np.matmul(R2(rot2), R3(-rot3)))

                    DummyM = np.matmul(Rtotp, Dirt)

                    alpha = L/DummyM[2]
                    j1 = (poni1+alpha*DummyM[0])/pix-0.5
                    i1 = (poni2+alpha*DummyM[1])/pix-0.5
                    
                    
                    dX = i1[0]-i
                    dY = j1[0]-j
                    MX = np.round(dX)
                    MY = np.round(dY)
                    
                    if (MX == np.floor(dX)) and (MY == np.floor(dY)) and (i+MX >=0) and (i+MX+1<np.shape(Dwdata)[0]) and (j+MY >=0) and (j+MY+1<np.shape(Dwdata)[1]):
                        rX = MX+1-dX
                        rY = MY+1-dY
                        Dwdata[i,j]=int(rX*rY*D1data[i+int(MX),j+int(MY)]+rX*(1-rY)*D1data[i+int(MX),j+int(MY)+1]+(1-rX)*rY*D1data[i+int(MX)+1,j+int(MY)]+(1-rX)*(1-rY)*D1data[i+int(MX)+1,j+int(MY)+1])
                        
                    if (MX == np.floor(dX)) and (MY == np.ceil(dY)) and (i+MX >=0) and (i+MX+1<np.shape(Dwdata)[0]) and (j+MY-1 >=0) and (j+MY<np.shape(Dwdata)[1]):
                        rX = MX+1-dX
                        rY = dY+1-MY
                        Dwdata[i,j]=int(rX*rY*D1data[i+int(MX),j+int(MY)]+rX*(1-rY)*D1data[i+int(MX),j+int(MY)-1]+(1-rX)*rY*D1data[i+int(MX)+1,j+int(MY)]+(1-rX)*(1-rY)*D1data[i+int(MX)+1,j+int(MY)-1])
                        
                    if (MX == np.ceil(dX)) and (MY == np.floor(dY)) and (i+MX-1 >=0) and (i+MX<np.shape(Dwdata)[0]) and (j+MY >=0) and (j+MY+1<np.shape(Dwdata)[1]):
                        rX = dX+1-MX
                        rY = MY+1-dY
                        Dwdata[i,j]=int(rX*rY*D1data[i+int(MX),j+int(MY)]+rX*(1-rY)*D1data[i+int(MX),j+int(MY)+1]+(1-rX)*rY*D1data[i+int(MX)-1,j+int(MY)]+(1-rX)*(1-rY)*D1data[i+int(MX)-1,j+int(MY)+1])
                        
                    if (MX == np.ceil(dX)) and (MY == np.ceil(dY)) and (i+MX-1 >=0) and (i+MX<np.shape(Dwdata)[0]) and (j+MY-1 >=0) and (j+MY<np.shape(Dwdata)[1]):
                        rX = dX+1-MX
                        rY = dY+1-MY
                        Dwdata[i,j]=int(rX*rY*D1data[i+int(MX),j+int(MY)]+rX*(1-rY)*D1data[i+int(MX),j+int(MY)-1]+(1-rX)*rY*D1data[i+int(MX)-1,j+int(MY)]+(1-rX)*(1-rY)*D1data[i+int(MX)-1,j+int(MY)-1])
        
        DwdataX = np.flipud(Dwdata)
        plt.figure('Merged')
        plt.imshow(DwdataX, vmin=0, vmax=MaxS)   
        plt.show()
        self.originfileT.setText('')
        self.originponiT.setText('')
        self.destinfileT.setText('')
        self.destinponiT.setText('')
        fld = self.outfolderT.text()
        if fld == '':
            fld = '.'
        prf = self.prefix.text()
        if prf =='':
            prf = 'output'
        
        obj = fabio.cbfimage.CbfImage(data=DwdataX)
        obj.write(fld+'/'+prf+".cbf")


        obj = fabio.tifimage.TifImage(data=DwdataX)
        obj.write(fld+'/'+prf+".tif")

        
        self.mergeT.setText('Done')
    
    
    
    
######################################

if __name__ == '__main__':
    
    f = open('tmp1','w')
    f.write('.')
    f.close()
    f = open('tmp2','w')
    f.write('.')
    f.close()
    f = open('tmp3','w')
    f.write('.')
    f.close()
    f = open('tmp4','w')
    f.write('.')
    f.close()
    f = open('tmp5','w')
    f.write('.')
    f.close()
    
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(mainWindow)

    mainWindow.show()

    sys.exit(app.exec_())

