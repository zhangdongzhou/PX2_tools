# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMCXtal_ui.ui'
#
# Created: Sat Jun 29 10:46:03 2019
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 640)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.FolderN = QtGui.QLabel(self.centralwidget)
        self.FolderN.setGeometry(QtCore.QRect(40, 70, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FolderN.setFont(font)
        self.FolderN.setFrameShape(QtGui.QFrame.Panel)
        self.FolderN.setFrameShadow(QtGui.QFrame.Sunken)
        self.FolderN.setText(_fromUtf8(""))
        self.FolderN.setObjectName(_fromUtf8("FolderN"))
        self.FolderUpdate = QtGui.QPushButton(self.centralwidget)
        self.FolderUpdate.setGeometry(QtCore.QRect(150, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FolderUpdate.setFont(font)
        self.FolderUpdate.setObjectName(_fromUtf8("FolderUpdate"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.SampleUpdate = QtGui.QPushButton(self.centralwidget)
        self.SampleUpdate.setGeometry(QtCore.QRect(740, 30, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SampleUpdate.setFont(font)
        self.SampleUpdate.setObjectName(_fromUtf8("SampleUpdate"))
        self.SampN = QtGui.QLineEdit(self.centralwidget)
        self.SampN.setGeometry(QtCore.QRect(630, 70, 181, 31))
        self.SampN.setObjectName(_fromUtf8("SampN"))
        self.Nu = QtGui.QLineEdit(self.centralwidget)
        self.Nu.setGeometry(QtCore.QRect(110, 180, 50, 25))
        self.Nu.setObjectName(_fromUtf8("Nu"))
        self.StpN = QtGui.QLineEdit(self.centralwidget)
        self.StpN.setGeometry(QtCore.QRect(310, 180, 50, 25))
        self.StpN.setObjectName(_fromUtf8("StpN"))
        self.Delt = QtGui.QLineEdit(self.centralwidget)
        self.Delt.setGeometry(QtCore.QRect(50, 180, 50, 25))
        self.Delt.setObjectName(_fromUtf8("Delt"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 150, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.KphiEnd = QtGui.QLineEdit(self.centralwidget)
        self.KphiEnd.setGeometry(QtCore.QRect(240, 180, 50, 25))
        self.KphiEnd.setObjectName(_fromUtf8("KphiEnd"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(370, 150, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 120, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 150, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 147, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.KphiStart = QtGui.QLineEdit(self.centralwidget)
        self.KphiStart.setGeometry(QtCore.QRect(180, 180, 50, 25))
        self.KphiStart.setObjectName(_fromUtf8("KphiStart"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 150, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.TimperFrm = QtGui.QLineEdit(self.centralwidget)
        self.TimperFrm.setGeometry(QtCore.QRect(370, 180, 50, 25))
        self.TimperFrm.setObjectName(_fromUtf8("TimperFrm"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 150, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(200, 120, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.Col_Btn = QtGui.QPushButton(self.centralwidget)
        self.Col_Btn.setGeometry(QtCore.QRect(480, 160, 141, 46))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Col_Btn.setFont(font)
        self.Col_Btn.setObjectName(_fromUtf8("Col_Btn"))
        self.C3 = QtGui.QLineEdit(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(90, 420, 100, 25))
        self.C3.setObjectName(_fromUtf8("C3"))
        self.Sel6 = QtGui.QPushButton(self.centralwidget)
        self.Sel6.setGeometry(QtCore.QRect(400, 540, 75, 25))
        self.Sel6.setObjectName(_fromUtf8("Sel6"))
        self.Mv1 = QtGui.QPushButton(self.centralwidget)
        self.Mv1.setGeometry(QtCore.QRect(500, 340, 75, 25))
        self.Mv1.setObjectName(_fromUtf8("Mv1"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(50, 500, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.LZ2 = QtGui.QLineEdit(self.centralwidget)
        self.LZ2.setGeometry(QtCore.QRect(330, 380, 50, 25))
        self.LZ2.setObjectName(_fromUtf8("LZ2"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(50, 340, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.LX4 = QtGui.QLineEdit(self.centralwidget)
        self.LX4.setGeometry(QtCore.QRect(210, 460, 50, 25))
        self.LX4.setObjectName(_fromUtf8("LX4"))
        self.LX2 = QtGui.QLineEdit(self.centralwidget)
        self.LX2.setGeometry(QtCore.QRect(210, 380, 50, 25))
        self.LX2.setObjectName(_fromUtf8("LX2"))
        self.LZ1 = QtGui.QLineEdit(self.centralwidget)
        self.LZ1.setGeometry(QtCore.QRect(330, 340, 50, 25))
        self.LZ1.setObjectName(_fromUtf8("LZ1"))
        self.Sel3 = QtGui.QPushButton(self.centralwidget)
        self.Sel3.setGeometry(QtCore.QRect(400, 420, 75, 25))
        self.Sel3.setObjectName(_fromUtf8("Sel3"))
        self.LX6 = QtGui.QLineEdit(self.centralwidget)
        self.LX6.setGeometry(QtCore.QRect(210, 540, 50, 25))
        self.LX6.setObjectName(_fromUtf8("LX6"))
        self.label_24 = QtGui.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(330, 310, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.LX5 = QtGui.QLineEdit(self.centralwidget)
        self.LX5.setGeometry(QtCore.QRect(210, 500, 50, 25))
        self.LX5.setObjectName(_fromUtf8("LX5"))
        self.Mv2 = QtGui.QPushButton(self.centralwidget)
        self.Mv2.setGeometry(QtCore.QRect(500, 380, 75, 25))
        self.Mv2.setObjectName(_fromUtf8("Mv2"))
        self.LY6 = QtGui.QLineEdit(self.centralwidget)
        self.LY6.setGeometry(QtCore.QRect(270, 540, 50, 25))
        self.LY6.setObjectName(_fromUtf8("LY6"))
        self.LY2 = QtGui.QLineEdit(self.centralwidget)
        self.LY2.setGeometry(QtCore.QRect(270, 380, 50, 25))
        self.LY2.setObjectName(_fromUtf8("LY2"))
        self.C4 = QtGui.QLineEdit(self.centralwidget)
        self.C4.setGeometry(QtCore.QRect(90, 460, 100, 25))
        self.C4.setObjectName(_fromUtf8("C4"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 380, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(235, 280, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.Sel4 = QtGui.QPushButton(self.centralwidget)
        self.Sel4.setGeometry(QtCore.QRect(400, 460, 75, 25))
        self.Sel4.setObjectName(_fromUtf8("Sel4"))
        self.LZ5 = QtGui.QLineEdit(self.centralwidget)
        self.LZ5.setGeometry(QtCore.QRect(330, 500, 50, 25))
        self.LZ5.setObjectName(_fromUtf8("LZ5"))
        self.C1 = QtGui.QLineEdit(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(90, 340, 100, 25))
        self.C1.setObjectName(_fromUtf8("C1"))
        self.LZ3 = QtGui.QLineEdit(self.centralwidget)
        self.LZ3.setGeometry(QtCore.QRect(330, 420, 50, 25))
        self.LZ3.setObjectName(_fromUtf8("LZ3"))
        self.Mv3 = QtGui.QPushButton(self.centralwidget)
        self.Mv3.setGeometry(QtCore.QRect(500, 420, 75, 25))
        self.Mv3.setObjectName(_fromUtf8("Mv3"))
        self.C6 = QtGui.QLineEdit(self.centralwidget)
        self.C6.setGeometry(QtCore.QRect(90, 540, 100, 25))
        self.C6.setObjectName(_fromUtf8("C6"))
        self.LZ4 = QtGui.QLineEdit(self.centralwidget)
        self.LZ4.setGeometry(QtCore.QRect(330, 460, 50, 25))
        self.LZ4.setObjectName(_fromUtf8("LZ4"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(270, 310, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.Sel5 = QtGui.QPushButton(self.centralwidget)
        self.Sel5.setGeometry(QtCore.QRect(400, 500, 75, 25))
        self.Sel5.setObjectName(_fromUtf8("Sel5"))
        self.LY3 = QtGui.QLineEdit(self.centralwidget)
        self.LY3.setGeometry(QtCore.QRect(270, 420, 50, 25))
        self.LY3.setObjectName(_fromUtf8("LY3"))
        self.LY4 = QtGui.QLineEdit(self.centralwidget)
        self.LY4.setGeometry(QtCore.QRect(270, 460, 50, 25))
        self.LY4.setObjectName(_fromUtf8("LY4"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 420, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.LX3 = QtGui.QLineEdit(self.centralwidget)
        self.LX3.setGeometry(QtCore.QRect(210, 420, 50, 25))
        self.LX3.setObjectName(_fromUtf8("LX3"))
        self.C2 = QtGui.QLineEdit(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(90, 380, 100, 25))
        self.C2.setObjectName(_fromUtf8("C2"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(90, 290, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.Sel1 = QtGui.QPushButton(self.centralwidget)
        self.Sel1.setGeometry(QtCore.QRect(400, 340, 75, 25))
        self.Sel1.setObjectName(_fromUtf8("Sel1"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(50, 540, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.C5 = QtGui.QLineEdit(self.centralwidget)
        self.C5.setGeometry(QtCore.QRect(90, 500, 100, 25))
        self.C5.setObjectName(_fromUtf8("C5"))
        self.Mv4 = QtGui.QPushButton(self.centralwidget)
        self.Mv4.setGeometry(QtCore.QRect(500, 460, 75, 25))
        self.Mv4.setObjectName(_fromUtf8("Mv4"))
        self.LZ6 = QtGui.QLineEdit(self.centralwidget)
        self.LZ6.setGeometry(QtCore.QRect(330, 540, 50, 25))
        self.LZ6.setObjectName(_fromUtf8("LZ6"))
        self.LX1 = QtGui.QLineEdit(self.centralwidget)
        self.LX1.setGeometry(QtCore.QRect(210, 340, 50, 25))
        self.LX1.setObjectName(_fromUtf8("LX1"))
        self.Mv6 = QtGui.QPushButton(self.centralwidget)
        self.Mv6.setGeometry(QtCore.QRect(500, 540, 75, 25))
        self.Mv6.setObjectName(_fromUtf8("Mv6"))
        self.LY5 = QtGui.QLineEdit(self.centralwidget)
        self.LY5.setGeometry(QtCore.QRect(270, 500, 50, 25))
        self.LY5.setObjectName(_fromUtf8("LY5"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(50, 460, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(210, 310, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.Sel2 = QtGui.QPushButton(self.centralwidget)
        self.Sel2.setGeometry(QtCore.QRect(400, 380, 75, 25))
        self.Sel2.setObjectName(_fromUtf8("Sel2"))
        self.LY1 = QtGui.QLineEdit(self.centralwidget)
        self.LY1.setGeometry(QtCore.QRect(270, 340, 50, 25))
        self.LY1.setObjectName(_fromUtf8("LY1"))
        self.Mv5 = QtGui.QPushButton(self.centralwidget)
        self.Mv5.setGeometry(QtCore.QRect(500, 500, 75, 25))
        self.Mv5.setObjectName(_fromUtf8("Mv5"))
        self.LogZone = QtGui.QScrollArea(self.centralwidget)
        self.LogZone.setGeometry(QtCore.QRect(630, 130, 331, 441))
        self.LogZone.setWidgetResizable(True)
        self.LogZone.setObjectName(_fromUtf8("LogZone"))
        self.LogWidget = QtGui.QWidget()
        self.LogWidget.setGeometry(QtCore.QRect(0, 0, 329, 439))
        self.LogWidget.setObjectName(_fromUtf8("LogWidget"))
        self.LogL1 = QtGui.QLabel(self.LogWidget)
        self.LogL1.setGeometry(QtCore.QRect(0, 0, 331, 441))
        self.LogL1.setText(_fromUtf8(""))
        self.LogL1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.LogL1.setObjectName(_fromUtf8("LogL1"))
        self.LogZone.setWidget(self.LogWidget)
        self.warn1 = QtGui.QLabel(self.centralwidget)
        self.warn1.setGeometry(QtCore.QRect(50, 210, 46, 21))
        self.warn1.setText(_fromUtf8(""))
        self.warn1.setObjectName(_fromUtf8("warn1"))
        self.warn2 = QtGui.QLabel(self.centralwidget)
        self.warn2.setGeometry(QtCore.QRect(110, 210, 46, 21))
        self.warn2.setText(_fromUtf8(""))
        self.warn2.setObjectName(_fromUtf8("warn2"))
        self.warn4 = QtGui.QLabel(self.centralwidget)
        self.warn4.setGeometry(QtCore.QRect(240, 210, 46, 21))
        self.warn4.setText(_fromUtf8(""))
        self.warn4.setObjectName(_fromUtf8("warn4"))
        self.warn3 = QtGui.QLabel(self.centralwidget)
        self.warn3.setGeometry(QtCore.QRect(180, 210, 46, 21))
        self.warn3.setText(_fromUtf8(""))
        self.warn3.setObjectName(_fromUtf8("warn3"))
        self.warn5 = QtGui.QLabel(self.centralwidget)
        self.warn5.setGeometry(QtCore.QRect(310, 210, 46, 21))
        self.warn5.setText(_fromUtf8(""))
        self.warn5.setObjectName(_fromUtf8("warn5"))
        self.warn6 = QtGui.QLabel(self.centralwidget)
        self.warn6.setGeometry(QtCore.QRect(370, 210, 46, 21))
        self.warn6.setText(_fromUtf8(""))
        self.warn6.setObjectName(_fromUtf8("warn6"))
        self.Calibration = QtGui.QPushButton(self.centralwidget)
        self.Calibration.setGeometry(QtCore.QRect(840, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Calibration.setFont(font)
        self.Calibration.setObjectName(_fromUtf8("Calibration"))
        self.CK1 = QtGui.QCheckBox(self.centralwidget)
        self.CK1.setGeometry(QtCore.QRect(590, 340, 21, 21))
        self.CK1.setText(_fromUtf8(""))
        self.CK1.setObjectName(_fromUtf8("CK1"))
        self.CK2 = QtGui.QCheckBox(self.centralwidget)
        self.CK2.setGeometry(QtCore.QRect(590, 380, 21, 21))
        self.CK2.setText(_fromUtf8(""))
        self.CK2.setObjectName(_fromUtf8("CK2"))
        self.CK3 = QtGui.QCheckBox(self.centralwidget)
        self.CK3.setGeometry(QtCore.QRect(590, 420, 21, 21))
        self.CK3.setText(_fromUtf8(""))
        self.CK3.setObjectName(_fromUtf8("CK3"))
        self.CK4 = QtGui.QCheckBox(self.centralwidget)
        self.CK4.setGeometry(QtCore.QRect(590, 460, 21, 21))
        self.CK4.setText(_fromUtf8(""))
        self.CK4.setObjectName(_fromUtf8("CK4"))
        self.CK5 = QtGui.QCheckBox(self.centralwidget)
        self.CK5.setGeometry(QtCore.QRect(590, 500, 21, 21))
        self.CK5.setText(_fromUtf8(""))
        self.CK5.setObjectName(_fromUtf8("CK5"))
        self.CK6 = QtGui.QCheckBox(self.centralwidget)
        self.CK6.setGeometry(QtCore.QRect(590, 540, 21, 21))
        self.CK6.setText(_fromUtf8(""))
        self.CK6.setObjectName(_fromUtf8("CK6"))
        self.SUMCK = QtGui.QCheckBox(self.centralwidget)
        self.SUMCK.setGeometry(QtCore.QRect(440, 180, 16, 21))
        self.SUMCK.setText(_fromUtf8(""))
        self.SUMCK.setObjectName(_fromUtf8("SUMCK"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 150, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "13BMC Single Crystal Data Collection", None))
        self.label.setText(_translate("MainWindow", "Data folder", None))
        self.FolderUpdate.setText(_translate("MainWindow", "Update", None))
        self.label_3.setText(_translate("MainWindow", "Sample", None))
        self.SampleUpdate.setText(_translate("MainWindow", "Update", None))
        self.label_6.setText(_translate("MainWindow", "Del", None))
        self.label_11.setText(_translate("MainWindow", "Time", None))
        self.label_12.setText(_translate("MainWindow", "Detector", None))
        self.label_9.setText(_translate("MainWindow", "Start", None))
        self.label_10.setText(_translate("MainWindow", "Step#", None))
        self.label_8.setText(_translate("MainWindow", "End", None))
        self.label_7.setText(_translate("MainWindow", "Nu", None))
        self.label_13.setText(_translate("MainWindow", "kphi", None))
        self.Col_Btn.setText(_translate("MainWindow", "Collect!", None))
        self.Sel6.setText(_translate("MainWindow", "Select", None))
        self.Mv1.setText(_translate("MainWindow", "Move", None))
        self.label_19.setText(_translate("MainWindow", "C5", None))
        self.label_16.setText(_translate("MainWindow", "C1", None))
        self.Sel3.setText(_translate("MainWindow", "Select", None))
        self.label_24.setText(_translate("MainWindow", "Z", None))
        self.Mv2.setText(_translate("MainWindow", "Move", None))
        self.label_14.setText(_translate("MainWindow", "C2", None))
        self.label_21.setText(_translate("MainWindow", "Sample Position", None))
        self.Sel4.setText(_translate("MainWindow", "Select", None))
        self.Mv3.setText(_translate("MainWindow", "Move", None))
        self.label_23.setText(_translate("MainWindow", "Y", None))
        self.Sel5.setText(_translate("MainWindow", "Select", None))
        self.label_17.setText(_translate("MainWindow", "C3", None))
        self.label_20.setText(_translate("MainWindow", "Sample Description", None))
        self.Sel1.setText(_translate("MainWindow", "Select", None))
        self.label_18.setText(_translate("MainWindow", "C6", None))
        self.Mv4.setText(_translate("MainWindow", "Move", None))
        self.Mv6.setText(_translate("MainWindow", "Move", None))
        self.label_15.setText(_translate("MainWindow", "C4", None))
        self.label_22.setText(_translate("MainWindow", "X", None))
        self.Sel2.setText(_translate("MainWindow", "Select", None))
        self.Mv5.setText(_translate("MainWindow", "Move", None))
        self.Calibration.setText(_translate("MainWindow", "Calibration", None))
        self.label_2.setText(_translate("MainWindow", "SUM", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

