# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMCXtal_calibui.ui'
#
# Created: Tue Jun 18 23:31:30 2019
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(516, 557)
        self.L1 = QtGui.QLabel(Dialog)
        self.L1.setGeometry(QtCore.QRect(30, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L1.setFont(font)
        self.L1.setObjectName(_fromUtf8("L1"))
        self.L2 = QtGui.QLabel(Dialog)
        self.L2.setGeometry(QtCore.QRect(30, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L2.setFont(font)
        self.L2.setObjectName(_fromUtf8("L2"))
        self.L3 = QtGui.QLabel(Dialog)
        self.L3.setGeometry(QtCore.QRect(30, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L3.setFont(font)
        self.L3.setObjectName(_fromUtf8("L3"))
        self.R1 = QtGui.QRadioButton(Dialog)
        self.R1.setGeometry(QtCore.QRect(40, 190, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R1.setFont(font)
        self.R1.setObjectName(_fromUtf8("R1"))
        self.R2 = QtGui.QRadioButton(Dialog)
        self.R2.setGeometry(QtCore.QRect(150, 190, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R2.setFont(font)
        self.R2.setObjectName(_fromUtf8("R2"))
        self.B1 = QtGui.QPushButton(Dialog)
        self.B1.setGeometry(QtCore.QRect(320, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B1.setFont(font)
        self.B1.setObjectName(_fromUtf8("B1"))
        self.CrysAlis = QtGui.QLabel(Dialog)
        self.CrysAlis.setGeometry(QtCore.QRect(50, 240, 391, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CrysAlis.setFont(font)
        self.CrysAlis.setFrameShape(QtGui.QFrame.Box)
        self.CrysAlis.setText(_fromUtf8(""))
        self.CrysAlis.setObjectName(_fromUtf8("CrysAlis"))
        self.T1 = QtGui.QLineEdit(Dialog)
        self.T1.setGeometry(QtCore.QRect(310, 40, 131, 31))
        self.T1.setObjectName(_fromUtf8("T1"))
        self.T2 = QtGui.QLineEdit(Dialog)
        self.T2.setGeometry(QtCore.QRect(310, 80, 131, 31))
        self.T2.setObjectName(_fromUtf8("T2"))
        self.T3 = QtGui.QLineEdit(Dialog)
        self.T3.setGeometry(QtCore.QRect(310, 120, 131, 31))
        self.T3.setObjectName(_fromUtf8("T3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Calibration", None))
        self.L1.setText(_translate("Dialog", "BMCPilatusDist (mm)", None))
        self.L2.setText(_translate("Dialog", "BMCPilatusBeamX (px)", None))
        self.L3.setText(_translate("Dialog", "BMCPilatusBeamY (px)", None))
        self.R1.setText(_translate("Dialog", "TIF", None))
        self.R2.setText(_translate("Dialog", "CBF", None))
        self.B1.setText(_translate("Dialog", "Update", None))
