# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CBFTIF_V1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
import sys
import fabio
import os

class Ui_MainWindow(QtWidgets.QMainWindow):
    # It is very important to replace the 'object' to QtWidgets.QMainWindow from pyuic, without the '()'.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 184)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SeFolder = QtWidgets.QPushButton(self.centralwidget)
        self.SeFolder.setGeometry(QtCore.QRect(50, 30, 111, 20))
        self.SeFolder.setObjectName("SeFolder")
        self.Conv = QtWidgets.QPushButton(self.centralwidget)
        self.Conv.setGeometry(QtCore.QRect(50, 120, 111, 20))
        self.Conv.setObjectName("Conv")
        self.Disp = QtWidgets.QLabel(self.centralwidget)
        self.Disp.setGeometry(QtCore.QRect(210, 120, 101, 16))
        self.Disp.setText("")
        self.Disp.setObjectName("Disp")
        self.FolderLoc = QtWidgets.QLineEdit(self.centralwidget)
        self.FolderLoc.setGeometry(QtCore.QRect(50, 70, 381, 20))
        self.FolderLoc.setObjectName("FolderLoc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.SeFolder.clicked.connect(self.openfolder)
        self.Conv.clicked.connect(self.Converter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CBF to TIF converter"))
        self.SeFolder.setText(_translate("MainWindow", "Select folder"))
        self.Conv.setText(_translate("MainWindow", "Convert"))
        
    def openfolder(self):
        try:
            f = open('templastdir.txt','r')
            lastdir = f.read()
            directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder", lastdir)
            self.FolderLoc.setText(directory)
            f.close()
            os.remove('templastdir.txt')
            f1 = open('templastdir.txt','w')
            f1.write(directory)
            f1.close()
        except:
            directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder", "./") 
            self.FolderLoc.setText(directory)
            f1 = open('templastdir.txt','w')
            f1.write(directory)
            f1.close()
        
        
    def Converter(self):
        self.Disp.setStyleSheet('color: red')
        self.Disp.setText("Busy")
        QtWidgets.QApplication.processEvents()
        
        files = []
        # r=root, d=directories, f = files
        FL = self.FolderLoc.text()
        if os.path.exists(FL):
            
            for r, d, f in os.walk(FL):
                for file in f:
                    if '.cbf' in file:
                        files.append(os.path.join(r, file))
            
            for f1 in files:
                newN = f1[0:-3]+'tif'
                fabio.open(f1).convert("tif").save(newN)
            
            self.Disp.setStyleSheet('color: green')
            self.Disp.setText("Done")        
        else:
            self.Disp.setStyleSheet('color: red')
            self.Disp.setText("Error") 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())