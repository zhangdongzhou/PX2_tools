# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DACaxis.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
#
# author: Dongzhou Zhang (dzzhang@cars.uchicago.edu)
#
# Crystal orientation calculator for PX^2 single crystal diffraction
# Useful for Brillouin experiment
# Works with most P4P format once the crystal orientation is determined by
# e.g., APEX or ATREX/RSV

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import re
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 242)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.P4P = QtWidgets.QPushButton(self.centralwidget)
        self.P4P.setGeometry(QtCore.QRect(20, 20, 65, 20))
        self.P4P.setObjectName("P4P")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Cal = QtWidgets.QPushButton(self.centralwidget)
        self.Cal.setGeometry(QtCore.QRect(20, 170, 65, 20))
        self.Cal.setObjectName("Cal")
        self.A11 = QtWidgets.QLineEdit(self.centralwidget)
        self.A11.setGeometry(QtCore.QRect(110, 60, 71, 20))
        self.A11.setObjectName("A11")
        self.A12 = QtWidgets.QLineEdit(self.centralwidget)
        self.A12.setGeometry(QtCore.QRect(200, 60, 71, 20))
        self.A12.setObjectName("A12")
        self.A13 = QtWidgets.QLineEdit(self.centralwidget)
        self.A13.setGeometry(QtCore.QRect(290, 60, 71, 20))
        self.A13.setObjectName("A13")
        self.A22 = QtWidgets.QLineEdit(self.centralwidget)
        self.A22.setGeometry(QtCore.QRect(200, 90, 71, 20))
        self.A22.setObjectName("A22")
        self.A21 = QtWidgets.QLineEdit(self.centralwidget)
        self.A21.setGeometry(QtCore.QRect(110, 90, 71, 20))
        self.A21.setObjectName("A21")
        self.A23 = QtWidgets.QLineEdit(self.centralwidget)
        self.A23.setGeometry(QtCore.QRect(290, 90, 71, 20))
        self.A23.setObjectName("A23")
        self.A32 = QtWidgets.QLineEdit(self.centralwidget)
        self.A32.setGeometry(QtCore.QRect(200, 120, 71, 20))
        self.A32.setObjectName("A32")
        self.A31 = QtWidgets.QLineEdit(self.centralwidget)
        self.A31.setGeometry(QtCore.QRect(110, 120, 71, 20))
        self.A31.setObjectName("A31")
        self.A33 = QtWidgets.QLineEdit(self.centralwidget)
        self.A33.setGeometry(QtCore.QRect(290, 120, 71, 20))
        self.A33.setObjectName("A33")
        self.C1 = QtWidgets.QLabel(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(110, 170, 71, 20))
        self.C1.setText("")
        self.C1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.C1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.C1.setObjectName("C1")
        self.C2 = QtWidgets.QLabel(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(200, 170, 71, 20))
        self.C2.setText("")
        self.C2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.C2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.C2.setObjectName("C2")
        self.C3 = QtWidgets.QLabel(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(290, 170, 71, 20))
        self.C3.setText("")
        self.C3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.C3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.C3.setObjectName("C3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Cal.clicked.connect(self.Calculate)
        self.P4P.clicked.connect(self.LoadP4P)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crystal orientation along DAC axis"))
        self.P4P.setText(_translate("MainWindow", "Load p4p"))
        self.label.setText(_translate("MainWindow", "ORT1"))
        self.label_2.setText(_translate("MainWindow", "ORT2"))
        self.label_3.setText(_translate("MainWindow", "ORT3"))
        self.Cal.setText(_translate("MainWindow", "Calculate"))
        
    def LoadP4P(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self,
              "getOpenFileName","./",
              "P4P Files (*.p4p);;All Files (*)")
        with open(directory[0]) as f:
            Lines = f.readlines()
        try:
            for line in Lines:
                if re.match('ORT1', line):
                    C = re.findall(r"[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?", line)
                    self.A11.setText(str(C[1]))
                    self.A12.setText(str(C[2]))
                    self.A13.setText(str(C[3]))
                if re.match('ORT2', line):
                    C = re.findall(r"[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?", line)
                    self.A21.setText(str(C[1]))
                    self.A22.setText(str(C[2]))
                    self.A23.setText(str(C[3]))
                if re.match('ORT3', line):
                    C = re.findall(r"[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?", line)
                    self.A31.setText(str(C[1]))
                    self.A32.setText(str(C[2]))
                    self.A33.setText(str(C[3]))
        except:
            self.C1.setStyleSheet('color: red')
            self.C1.setText("Wrong P4P") 
    
    def Calculate(self):
        try:
            A11x = float(self.A11.text())
            A12x = float(self.A12.text())
            A13x = float(self.A13.text())
            A21x = float(self.A21.text())
            A22x = float(self.A22.text())
            A23x = float(self.A23.text())
            A31x = float(self.A31.text())
            A32x = float(self.A32.text())
            A33x = float(self.A33.text())
            A =  np.array([[A11x, A12x, A13x],
                           [A21x, A22x, A23x],
                           [A31x, A32x, A33x]])
            B =  np.linalg.inv(A)
            C = np.matmul(B, [[1], [0], [0]])
            C1x = np.round(float(C[0]), decimals=6)
            C2x = np.round(float(C[1]), decimals=6)
            C3x = np.round(float(C[2]), decimals=6)
            self.C1.setText(str(C1x))
            self.C2.setText(str(C2x))
            self.C3.setText(str(C3x))
        except:
            self.C1.setStyleSheet('color: red')
            self.C1.setText("Error") 
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
