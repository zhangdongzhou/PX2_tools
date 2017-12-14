# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:45:28 2017

@author: dzzhang
"""

import sys

from PyQt5.Qt import *
from shutil import copyfile

 
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
        self.lbl1.move(30, 50-30)
        self.lbl2.move(30, 100-30)
        self.lbl3.move(30, 150-30)
        self.lbl4.move(30, 200-30)
        self.lbl5.move(150, 250-30)
        self.lbl1.setText(r'Initial prefix')
        self.lbl2.setText(r'New prefix')
        self.lbl2.adjustSize()
        self.lbl3.setText(r'Starting number')
        self.lbl3.adjustSize()
        self.lbl4.setText(r'End number')
        self.lbl4.adjustSize()        

        self.qle1 = QLineEdit(self)
        self.qle2 = QLineEdit(self)
        self.qle3 = QLineEdit(self)
        self.qle4 = QLineEdit(self)
        self.qle1.move(150, 50-30)
        self.qle2.move(150, 100-30)
        self.qle3.move(150, 150-30)
        self.qle4.move(150, 200-30)
        
        self.btn = QPushButton('Rename', self)
        self.btn.move(30, 250-30)
        self.btn.clicked.connect(self.rename)
 
        self.setGeometry(300, 300, 330, 280)
        self.setWindowTitle('PyRename: tiff to Bruker mccd')   

    def rename(self):
        iniprefix = self.qle1.text()
        newprefix = self.qle2.text()
        num0 = int(self.qle3.text())
        num1 = int(self.qle4.text())+1
        inipostfix = '.tif'
        newpostfix = '.mccd'
        for num in range(num0,num1):
            tempnum = '0'*(4-len(str(num)))+str(num)
            ininame = iniprefix+tempnum+inipostfix
            newname = newprefix+tempnum+newpostfix
            copyfile(ininame,newname)
        self.lbl5.setText('Rename done')
                
def main():
    app = QApplication(sys.argv)
    ex = DACcorr()
    ex.show()
    sys.exit(app.exec_())        
    
if __name__ == '__main__':
     main()
