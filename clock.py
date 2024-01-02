# -*- coding: utf-8 -*-

# Name: Simple Clock
# Vesion: 1.0.1

#This is a clock software that allows users to learn about the current time.  
#The software was developed by xiaoliuprogrammer(Github).  


from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber_hours = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_hours.setGeometry(QtCore.QRect(0, 0, 160, 200))
        self.lcdNumber_hours.setObjectName("lcdNumber_hours")
        self.lcdNumber_minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_minutes.setGeometry(QtCore.QRect(220, 0, 160, 200))
        self.lcdNumber_minutes.setObjectName("lcdNumber_minutes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 60, 200))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 0, 60, 200))
        self.label_2.setObjectName("label_2")
        self.lcdNumber_seconds = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_seconds.setGeometry(QtCore.QRect(440, 0, 160, 200))
        self.lcdNumber_seconds.setObjectName("lcdNumber_seconds")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 创建定时器并设置
        self.timer = QtCore.QTimer()    
        self.timer.timeout.connect(self.DisplayTime)    
        self.timer.start()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Clock"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">:</span></p></body></html>"))

    def DisplayTime(self):
        #获取本地时间
        time_h = time.strftime('%H', time.localtime())
        time_m = time.strftime('%M', time.localtime())
        time_s = time.strftime('%S', time.localtime())

        #显示时间
        self.lcdNumber_hours.setProperty("intValue", int(time_h))
        self.lcdNumber_minutes.setProperty("intValue", int(time_m))
        self.lcdNumber_seconds.setProperty("intValue", int(time_s))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
