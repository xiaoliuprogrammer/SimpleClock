# -*- coding: utf-8 -*-

# Name: Simple Clock
# Vesion: 1.1.0

#This is a clock software that allows users to learn about the current time.  
#The software was developed by xiaoliuprogrammer(Github).  


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        icon = QIcon("./assets/icon/icon.ico")
        MainWindow.setWindowIcon(icon)
        
        MainWindow.resize(600, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 600, 200))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 创建定时器并设置
        self.timer = QtCore.QTimer()    
        self.timer.timeout.connect(self.Display)    
        self.timer.start()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Clock"))

    def Display(self):
        self.DisplayTime()
        self.Reset_WH()
        

    def DisplayTime(self):
        #获取本地时间
        time_h = time.strftime('%H', time.localtime())
        time_m = time.strftime('%M', time.localtime())
        time_s = time.strftime('%S', time.localtime())

        #显示时间
        self.lcdNumber.display(time_h + ":" + time_m + ":" + time_s)

    def Reset_WH(self):
        #适应窗体大小
        window_width = MainWindow.width()
        window_height = MainWindow.height()
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, window_width, window_height))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
