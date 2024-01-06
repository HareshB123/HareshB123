
from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_widgets.Widgets import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QCustomSlideMenu(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 111, 411))
        self.widget.setObjectName("widget")
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 91, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(60, 120, 120, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 91, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_6 = QtWidgets.QFrame(self.widget)
        self.frame_6.setGeometry(QtCore.QRect(10, 100, 91, 61))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 91, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_7 = QtWidgets.QFrame(self.widget)
        self.frame_7.setGeometry(QtCore.QRect(10, 340, 91, 61))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 91, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 80, 671, 411))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 791, 61))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.menu_2 = QtWidgets.QFrame(self.frame_9)
        self.menu_2.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.menu_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_2.setObjectName("menu_2")
        self.menu = QtWidgets.QPushButton(self.menu_2)
        self.menu.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.menu.setStyleSheet("image:url(:/menu/home.jpg)")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "voice assistant"))
        self.pushButton_3.setText(_translate("MainWindow", "calculator"))
        self.pushButton_4.setText(_translate("MainWindow", "account"))


import home_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
