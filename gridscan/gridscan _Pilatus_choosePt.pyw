# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:17:37 2018

@author: dzzhang
"""

import sys
from PyQt5.Qt import *
import epics
import time
import re

class DACcorr(QMainWindow):
     
    def __init__(self, parent=None):
        super(DACcorr,self).__init__(parent)
        self.initUI()    
    
    def initUI(self):              
               
        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)
        self.lbl3 = QLabel(self)
        self.lbl4 = QLabel(self)
        self.lbl5 = QLabel(self)
        self.lbl6 = QLabel(self)
        self.lbl7 = QLabel(self)
        self.lbl8 = QLabel(self)
        self.lbl9 = QLabel(self)
        self.lbl10 = QLabel(self)
        self.lbl11 = QLabel(self)
        
        self.lbl1.move(30, 20)
        self.lbl2.move(30, 80)
        self.lbl3.move(200, 80)
        self.lbl4.move(370, 80)
        self.lbl5.move(540, 80)
        self.lbl6.move(30, 130)
        self.lbl7.move(200, 130)
        self.lbl8.move(370, 130)
        self.lbl9.move(540, 130)
        self.lbl10.move(150, 170)
        self.lbl11.move(200, 20)
        
        
        self.lbl1.setText(r'Name')
        self.lbl11.setText(r'Exposure time')
        self.lbl2.setText(r'X motor')
        self.lbl2.adjustSize()
        self.lbl3.setText(r'X start')
        self.lbl3.adjustSize()
        self.lbl4.setText(r'X end')
        self.lbl4.adjustSize()        
        self.lbl5.setText(r'X step')
        self.lbl5.adjustSize()
        self.lbl6.setText(r'Y motor')
        self.lbl6.adjustSize()
        self.lbl7.setText(r'Y start')
        self.lbl7.adjustSize()   
        self.lbl8.setText(r'Y end')
        self.lbl8.adjustSize()
        self.lbl9.setText(r'Y step')
        self.lbl9.adjustSize()
  
        
        self.qle1 = QLineEdit(self)
        self.qle2 = QLineEdit(self)
        self.qle2.setText("13BMC:m46")
        self.qle3 = QLineEdit(self)
        self.qle4 = QLineEdit(self)
        self.qle5 = QLineEdit(self)
        self.qle5.setPlaceholderText(">=2")
        self.qle6 = QLineEdit(self)
        self.qle6.setText("13BMC:m44")
        self.qle7 = QLineEdit(self)
        self.qle8 = QLineEdit(self)
        self.qle9 = QLineEdit(self)
        self.qle9.setPlaceholderText(">=2")
        self.qle11 = QLineEdit(self)

        self.qle1.move(80, 20)
        self.qle2.move(80, 70)
        self.qle3.move(250, 70)
        self.qle4.move(420, 70)
        self.qle5.move(590, 70)
        self.qle6.move(80, 120)
        self.qle7.move(250, 120)
        self.qle8.move(420, 120)
        self.qle9.move(590, 120)
        self.qle11.move(280, 20)
        
        self.btn = QPushButton('Start Scan', self)
        self.btn.move(30, 170)
        self.btn.clicked.connect(self.collectgrid)
        
        self.btn = QPushButton('New log', self)
        self.btn.move(260, 170)
        self.btn.clicked.connect(self.Newlog)        

        self.btn = QPushButton('Choose points', self)
        self.btn.move(360, 170)
        self.btn.clicked.connect(self.ChoosePoints)
        
        self.btn = QPushButton('Run points', self)
        self.btn.move(460, 170)
        self.btn.clicked.connect(self.RunPoints)        
 
        self.setGeometry(300, 200, 750, 220)
        self.setWindowTitle('PX2 Grid Scan, using Pilatus1MSi')   
        
    def Newlog(self):
        tmp = ''
        f = open('./pointlog', 'w')
        f.write(tmp)
        f.close()
    
    def ChoosePoints(self):
        XX = epics.caget('13BMC:m44', as_string=True)
        YY = epics.caget('13BMC:m45', as_string=True)
        ZZ = epics.caget('13BMC:m46', as_string=True)
        tmp = XX + '\t' + YY + '\t' + ZZ +'\n'
        f = open('./pointlog', 'a')
        f.write(tmp)
        f.close()
        
    def RunPoints(self):
        epics.caput('13PIL1MSi:cam1:FileNumber',1)
        epics.caput('13PIL1MSi:cam1:AutoIncrement',1)
        f = open('./pointlog', 'r')
        tmp = f.readline()
        while(tmp !=''):
            L0 = re.split('\t', tmp)
            epics.caput('13BMC:m44', L0[0])
            epics.caput('13BMC:m45', L0[1])
            epics.caput('13BMC:m46', L0[2])
            time.sleep(2)
            tmp = self.qle1.text()
            epics.caput('13PIL1MSi:cam1:FileName',tmp)
            exp_tim = float(self.qle11.text())
            epics.caput('13PIL1MSi:cam1:AcquireTime',exp_tim)
            epics.caput('13PIL1MSi:cam1:AcquirePeriod',exp_tim+0.5)
            epics.caput('13PIL1MSi:cam1:Acquire',1)
            time.sleep(exp_tim+5) 
            tmp = f.readline()
        

    def collectgrid(self):
        
        X_srt = float(self.qle3.text())
        X_end = float(self.qle4.text())
        X_Ntp = int(self.qle5.text())
        
        Y_srt = float(self.qle7.text())
        Y_end = float(self.qle8.text())
        Y_Ntp = int(self.qle9.text())
        
        tmp = self.qle2.text()+'.HLM'
        XU = epics.caget(tmp)
        tmp = self.qle2.text()+'.LLM'
        XD = epics.caget(tmp)
        
        tmp = self.qle6.text()+'.HLM'
        YU = epics.caget(tmp)
        tmp = self.qle6.text()+'.LLM'
        YD = epics.caget(tmp)
        
        exp_tim = float(self.qle11.text())
        
        if X_srt <= XD or X_end <= XD:
            self.lbl10.setText('X low limit error')
        elif X_srt >= XU or X_end >= XU:
            self.lbl10.setText('X high limit error')
        elif Y_srt <= YD or Y_end <= YD:
            self.lbl10.setText('Y low limit error')
        elif Y_srt >= YU or Y_end >= YU:
            self.lbl10.setText('Y high limit error')
        else:
            epics.caput('13PIL1MSi:cam1:AutoIncrement',0)
            X_siz = (X_end-X_srt)/(X_Ntp-1)
            Y_siz = (Y_end-Y_srt)/(Y_Ntp-1)
            for M_X in range(X_Ntp):
                for N_Y in range(Y_Ntp):
                    X_aim = X_srt + X_siz*M_X
                    Y_aim = Y_srt + Y_siz*N_Y
                    tmp = self.qle2.text()+'.VAL'
                    epics.caput(tmp, X_aim)
                    tmp = self.qle6.text()+'.VAL'
                    epics.caput(tmp, Y_aim)
                    tmp = self.qle1.text()+'_X'+str(M_X)+'_Y'+str(N_Y)
                    epics.caput('13PIL1MSi:cam1:FileName',tmp)
                    time.sleep(5)
                    epics.caput('13PIL1MSi:cam1:AcquireTime',exp_tim)
                    epics.caput('13PIL1MSi:cam1:AcquirePeriod',exp_tim+0.5)
                    epics.caput('13PIL1MSi:cam1:NumImages',1)
                    epics.caput('13PIL1MSi:cam1:Acquire',1)
                    time.sleep(exp_tim+5)                
            epics.caput('13PIL1MSi:cam1:AutoIncrement',1)
            self.lbl10.setText('Collection done')

def main():
    app = QApplication(sys.argv)
    ex = DACcorr()
    ex.show()
    sys.exit(app.exec_())        
    
if __name__ == '__main__':
     main()
