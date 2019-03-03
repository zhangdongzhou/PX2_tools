# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMCXtal_Jan24.ui'
#
# Created: Thu Jan 24 2019
#      by: Dongzhou Zhang (dzhang@hawaii.edu)
#      current version: same as BMCXtal_Jan24.py
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import epics
import time
import sys
sys.path.append("//corvette/people_rw/specadm/Versions/spec6.08.02/src/splot/")
from SpecClient import SpecCommand,SpecVariable
import re
import os
import numpy as np

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
        font.setPointSize(10)
        self.FolderN.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
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
        self.Col_Btn.setGeometry(QtCore.QRect(450, 160, 161, 46))
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
        self.LogL1 = QtGui.QLabel()
        self.LogL1.setGeometry(QtCore.QRect(0, 0, 329, 439))
        self.LogL1.setObjectName(_fromUtf8("LogL1"))
        self.LogL1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.LogZone.setWidget(self.LogL1)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ###################### Define actions #############
        ### Sample position
        self.Sel1.clicked.connect(lambda: self.Sel_click(self.LX1,self.LY1,self.LZ1))
        self.Mv1.clicked.connect(lambda: self.Mv_click(self.LX1,self.LY1,self.LZ1))
        self.Sel2.clicked.connect(lambda: self.Sel_click(self.LX2,self.LY2,self.LZ2))
        self.Mv2.clicked.connect(lambda: self.Mv_click(self.LX2,self.LY2,self.LZ2))
        self.Sel3.clicked.connect(lambda: self.Sel_click(self.LX3,self.LY3,self.LZ3))
        self.Mv3.clicked.connect(lambda: self.Mv_click(self.LX3,self.LY3,self.LZ3))
        self.Sel4.clicked.connect(lambda: self.Sel_click(self.LX4,self.LY4,self.LZ4))
        self.Mv4.clicked.connect(lambda: self.Mv_click(self.LX4,self.LY4,self.LZ4))
        self.Sel5.clicked.connect(lambda: self.Sel_click(self.LX5,self.LY5,self.LZ5))
        self.Mv5.clicked.connect(lambda: self.Mv_click(self.LX5,self.LY5,self.LZ5))
        self.Sel6.clicked.connect(lambda: self.Sel_click(self.LX6,self.LY6,self.LZ6))
        self.Mv6.clicked.connect(lambda: self.Mv_click(self.LX6,self.LY6,self.LZ6))
        
        ### Data, folder, sample name
        self.Col_Btn.clicked.connect(lambda: self.DataColl(self.Delt, self.Nu, self.KphiStart, self.KphiEnd, self.StpN, self.TimperFrm))
        
        self.FolderUpdate.clicked.connect(lambda: self.findfolder())

        self.SampleUpdate.clicked.connect(lambda: self.newsample(self.SampN))        
        
        ###################### Define actions #############

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


        
    def Sel_click(self, widget1, widget2, widget3):
        X = epics.caget('13BMC:m44.VAL')
        Y = epics.caget('13BMC:m45.VAL')
        Z = epics.caget('13BMC:m46.VAL')
        strX = "{0:.3f}".format(X)
        strY = "{0:.3f}".format(Y)
        strZ = "{0:.3f}".format(Z)
        widget1.setText(strX)
        widget2.setText(strY)
        widget3.setText(strZ)
        
    def Mv_click(self, widget1, widget2, widget3):
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
        Ttem = max((X-X0)/XV,(Y-Y0)/YV, (Z-Z0)/ZV)+1.0
        time.sleep(Ttem)
    
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
        Ttem = max((dl1-dl0)/dlV,(nu1-nu0)/nuV)+5.0
        time.sleep(Ttem)
        
    def DataColl(self, Delt, Nu, KphiS, KphiE, StpN, TimNE):
        flgon = 1
        flgon = self.epicswarning(self.Delt, self.warn1, '13BMC:m37', flgon)
        flgon = self.epicswarning(self.Nu, self.warn2, '13BMC:m38', flgon)
        flgon = self.epicswarning(self.KphiStart, self.warn3, '13BMC:m33', flgon)
        flgon = self.epicswarning(self.KphiEnd, self.warn4, '13BMC:m33', flgon)
        flgon = self.stepwarning(self.StpN, self.warn5, flgon)
        flgon = self.speedwarning(self.TimperFrm, self.warn6, self.KphiStart, self.KphiEnd, self.StpN, flgon)
        if flgon:
            self.Detmov(Delt, Nu)
            xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
            kphivelo = epics.caget('13BMC:m33.VELO')
            kphiini = epics.caget('13BMC:m33.VAL')
            cmdcon = "xtal kphi " + KphiS.text()+' '+ KphiE.text()+' '+ StpN.text()+' '+ TimNE.text()
            eval("xtalcmd.executeCommand(\"%s\")" % cmdcon)
            Ttem = np.abs(kphiini-float(KphiS.text()))/kphivelo + float(TimNE.text())*float(StpN.text()) + 3
            time.sleep(Ttem)
            self.lastscan(self.LogL1, 'templog.txt')
    
    def findfolder(self):
        ProjPath = SpecVariable.SpecVariable('STARTUP_PROJECT_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        temp = ProjPath[25::]
        temp1 = 'T:'+temp+'images/'
        self.FolderN.setText(temp1)
        time.sleep(0.3)
    
    def newsample(self, newsample):
        SamNam = newsample.text()
        xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
        cmdcon = 'newsample '+SamNam
        eval("xtalcmd.executeCommand(\"%s\")" % cmdcon)
        time.sleep(0.2)
        self.nextscan(self.LogL1, 'templog.txt')

    def epicswarning(self, widget1, widget2, prefix, flg):
        # widget1 = input, widget2 = warning sign, prefix = epics motor name, flg = on/off
        num0 = widget1.text()
        time.sleep(0.02)
        try:
            num1 = float(num0)
            HLM = epics.caget(prefix+'.HLM')
            LLM = epics.caget(prefix+'.LLM')
            if num1 > HLM:
                widget2.setText('high lim')
                return flg*0
            elif num1 < LLM:
                widget2.setText('low lim')
                return flg*0
            else:
                widget2.setText('')
                return flg
        except:
            widget2.setText('not num')
            return flg*0
    
    def stepwarning(self, widget1, widget2, flg):
        num0 = widget1.text()
        try:
            num1 = int(num0)
            widget2.setText(str(num1))
            return flg
        except:
            widget2.setText('wrong')
            return flg*0
    
    def speedwarning(self, widget1, widget2, widget3, widget4, widget5, flg):
        # w1: time, w2: label, w3: kphistart, w4: kihiend, w5: num_of_step
        num0 = widget1.text()
        kphi0 = widget3.text()
        kphi1 = widget4.text()
        stp2 = widget5.text()
        try:
            num1 = float(num0)
            kphi10 = float(kphi0)
            kphi11 = float(kphi1)
            stp12 = float(stp2)
            spd = (kphi11-kphi10)/stp12/num1
            if num1 < 0.01:
                widget2.setText('too fast')
                return flg*0
            elif spd > 15.5:
                widget2.setText('too fast')
                return flg*0
            else:
                widget2.setText('')
                return flg
        except:
            widget2.setText('wrong')
            return flg*0
            
    def lastscan(self, widget1, tempfile):
        # only use after one scan is done. Newsample command creates a new logPath.
        LogPath = SpecVariable.SpecVariable('SCANLOG_PATH', 'corvette.cars.aps.anl.gov:6780').getValue()
        FilePath = SpecVariable.SpecVariable('SCANLOG_FILE', 'corvette.cars.aps.anl.gov:6780').getValue()
        len1 = len(LogPath)
        dummy = FilePath[len1:-4]
        dummy1 = re.split('_', dummy)
        cmdcon = time.asctime()+'\n\t'+ dummy1[2] +' done, saved in folder: '+ dummy1[0]+'_'+dummy1[1]+'\n'
        f = open(tempfile, 'a+')
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
        cmdcon = time.asctime()+'\n\tNew data will be saved in folder: ' + dummy + '\n'
        f = open(tempfile, 'a+')
        dummy2 = f.read()
        f.close()
        os.remove(tempfile)
        dummy3 = cmdcon + dummy2
        f = open(tempfile, 'a+')
        f.write(dummy3)
        f.close()
        widget1.setText(dummy3)
        

if __name__ == "__main__":
    xtalcmd = SpecCommand.SpecCommandA('','corvette.cars.aps.anl.gov:6780')
    eval("xtalcmd.executeCommand(\"%s\")" % 'wh')
    try:
        os.remove('templog.txt')
    except:
        pass
    time.sleep(0.3)
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())