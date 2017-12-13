# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:37:39 2017

@author: Dongzhou_X99
"""

import sys
#from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, 
#                             QLabel, QLineEdit, QPushButton,QInputDialog)
from PyQt5.Qt import *
import epics
import math
 
 
class DACcorr(QMainWindow):
     
    def __init__(self, parent=None):
        super(DACcorr,self).__init__(parent)
        self.initUI()
         

    
    
    def initUI(self):              
         
#        exitAction = QAction(QIcon('test.png'), 'Exit', self)
#        exitAction.setShortcut('Ctrl+Q')
#        exitAction.triggered.connect(qApp.quit)
#         
#        self.toolbar = self.addToolBar('Exit')
#        self.toolbar.addAction(exitAction)
        
        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)
        self.lbl3 = QLabel(self)
        self.lbl4 = QLabel(self)
        self.lbl5 = QLabel(self)
        self.lbl1.move(30, 50-30)
        self.lbl2.move(30, 100-30)
        self.lbl3.move(30, 150-30)
        self.lbl4.move(30, 200-30)
        self.lbl5.move(200, 250-30)
        self.lbl1.setText(r'Δkphi (m33)')
        self.lbl2.setText(r'Center of Sample_Y (m45) scan at kphi = 90')
        self.lbl2.adjustSize()
        self.lbl3.setText(r'Center of Sample_Y (m45) scan at kphi = 90+Δkphi')
        self.lbl3.adjustSize()
        self.lbl4.setText(r'Center of Sample_Y (m45) scan at kphi = 90-Δkphi')
        self.lbl4.adjustSize()        

        self.qle1 = QLineEdit(self)
        self.qle2 = QLineEdit(self)
        self.qle3 = QLineEdit(self)
        self.qle4 = QLineEdit(self)
        self.qle1.move(350, 50-30)
        self.qle2.move(350, 100-30)
        self.qle3.move(350, 150-30)
        self.qle4.move(350, 200-30)
#        self.lbl2.move(50, 200)
        
        self.btn = QPushButton('Make correction', self)
        self.btn.move(30, 250-30)
        self.btn.clicked.connect(self.updateUI)
 
#        qle1.textChanged[str].connect(self.onChanged)
#        qle2.textChanged[str].connect(self.onChanged2)
#        layoutMain =  QVBoxLayout()
#        self.setLayout(layoutMain)
        self.setGeometry(300, 300, 530, 280)
        self.setWindowTitle('DAC correction')   
#        self.show()
    def updateUI(self):
        try:
            dphi = float(self.qle1.text())
#            print(dphi)
            ctr = float(self.qle2.text())
            pls = float(self.qle3.text())
            mis = float(self.qle4.text())
            dx = (mis-pls)/(2*math.sin(dphi/180*math.pi))
            x_ini = epics.caget('13BMC:m44.VAL')
            x_fin = x_ini+dx
            txt1 = 'Move sample_X from '+str(x_ini)+' by '+str(dx)[0:8]+' to '+str(x_fin)[0:8]
            self.lbl5.setText(txt1)
            self.lbl5.adjustSize()
            epics.caput('13BMC:m44.VAL',x_fin)
        except:
            self.lbl5.setText('Invalid values')
                
        
#    def onChanged(self, text):
#         
#        self.lbl.setText(text)
#        self.lbl.adjustSize() 
#    def onChanged2(self, text):
#         
#        self.lbl2.setText(text)
#        self.lbl2.adjustSize() 
def main():
    app = QApplication(sys.argv)
    ex = DACcorr()
    ex.show()
    sys.exit(app.exec_())        
    
if __name__ == '__main__':
     main()
