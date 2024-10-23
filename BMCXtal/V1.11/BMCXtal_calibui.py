# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMCXtal_calibui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 557)
        self.L1 = QtWidgets.QLabel(Dialog)
        self.L1.setGeometry(QtCore.QRect(30, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L1.setFont(font)
        self.L1.setObjectName("L1")
        self.L2 = QtWidgets.QLabel(Dialog)
        self.L2.setGeometry(QtCore.QRect(30, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L2.setFont(font)
        self.L2.setObjectName("L2")
        self.L3 = QtWidgets.QLabel(Dialog)
        self.L3.setGeometry(QtCore.QRect(30, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L3.setFont(font)
        self.L3.setObjectName("L3")
        self.R1 = QtWidgets.QRadioButton(Dialog)
        self.R1.setGeometry(QtCore.QRect(40, 190, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R1.setFont(font)
        self.R1.setObjectName("R1")
        self.R2 = QtWidgets.QRadioButton(Dialog)
        self.R2.setGeometry(QtCore.QRect(150, 190, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R2.setFont(font)
        self.R2.setChecked(True)
        self.R2.setObjectName("R2")
        self.B1 = QtWidgets.QPushButton(Dialog)
        self.B1.setGeometry(QtCore.QRect(320, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B1.setFont(font)
        self.B1.setObjectName("B1")
        self.CrysAlis = QtWidgets.QLabel(Dialog)
        self.CrysAlis.setGeometry(QtCore.QRect(50, 240, 391, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CrysAlis.setFont(font)
        self.CrysAlis.setFrameShape(QtWidgets.QFrame.Box)
        self.CrysAlis.setText("")
        self.CrysAlis.setObjectName("CrysAlis")
        self.T1 = QtWidgets.QLineEdit(Dialog)
        self.T1.setGeometry(QtCore.QRect(310, 40, 131, 31))
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(Dialog)
        self.T2.setGeometry(QtCore.QRect(310, 80, 131, 31))
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QLineEdit(Dialog)
        self.T3.setGeometry(QtCore.QRect(310, 120, 131, 31))
        self.T3.setObjectName("T3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calibration"))
        self.L1.setText(_translate("Dialog", "BMCPilatusDist (mm)"))
        self.L2.setText(_translate("Dialog", "BMCPilatusBeamX (px)"))
        self.L3.setText(_translate("Dialog", "BMCPilatusBeamY (px)"))
        self.R1.setText(_translate("Dialog", "TIF"))
        self.R2.setText(_translate("Dialog", "CBF"))
        self.B1.setText(_translate("Dialog", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
