# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CanonControl_V0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests, re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 331, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        ############### password protect
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        ###############
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 40, 113, 20))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 130, 311, 22))
        self.horizontalSlider.setMinimum(-17000)
        self.horizontalSlider.setMaximum(17000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(630, 80, 22, 160))
        self.verticalSlider.setMinimum(197)
        self.verticalSlider.setMaximum(4126)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(460, 80, 22, 160))
        self.verticalSlider_2.setMinimum(-9000)
        self.verticalSlider_2.setMaximum(1000)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 101, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 90, 47, 13))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 150, 47, 13))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 100, 47, 120))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ############## logic
        self.horizontalSlider.valueChanged.connect(self.changePTZ)
        self.verticalSlider.valueChanged.connect(self.changePTZ)
        self.verticalSlider_2.valueChanged.connect(self.changePTZ)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Canon Webview Control"))
        self.lineEdit.setText(_translate("MainWindow", "164.54.160.138"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "164.54.160.138"))
        self.lineEdit_2.setText(_translate("MainWindow", "root"))
        self.lineEdit_3.setText(_translate("MainWindow", "hellocar"))
        self.label.setText(_translate("MainWindow", "Camera IP"))
        self.label_2.setText(_translate("MainWindow", "User"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Pan"))
        self.label_5.setText(_translate("MainWindow", "Tilt"))
        self.label_6.setText(_translate("MainWindow", "Out\n\n\nZoom\n\n\nIn"))
        
        ############# initialize
        usr = self.lineEdit_2.text()
        pwd = self.lineEdit_3.text()
        ip  = self.lineEdit.text()
        url = 'http://'+usr+':'+pwd+'@'+ip+':80/-wvhttp-01-/CameraPosition?'
        req1 = requests.get(url)
        for line in req1.text.splitlines():
            if re.match(r'pan_current_value',line):
                tmp = re.findall(r'-?\d+',line)
                pan = tmp[0]
                self.horizontalSlider.setProperty("value", int(pan))
            if re.match(r'tilt_current_value',line):
                tmp = re.findall(r'-?\d+',line)
                tilt = tmp[0]
                self.verticalSlider_2.setProperty("value", int(tilt))
            if re.match(r'zoom_current_value',line):
                tmp = re.findall(r'-?\d+',line)
                zoom = tmp[0]
                self.verticalSlider.setProperty("value", int(zoom))
                
                
            
    
    ############## function
    def changePTZ(self):
        usr = self.lineEdit_2.text()
        pwd = self.lineEdit_3.text()
        ip  = self.lineEdit.text()
        pan = self.horizontalSlider.value()
        tilt = self.verticalSlider_2.value()
        zoom = self.verticalSlider.value()
        url = 'http://'+usr+':'+pwd+'@'+ip+':80/-wvhttp-01-/CameraPosition?pan='+str(pan)+'&tilt='+str(tilt)+'&zoom='+str(zoom)
        requests.get(url)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

