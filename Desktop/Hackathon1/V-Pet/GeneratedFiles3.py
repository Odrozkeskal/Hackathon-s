# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mariy\Desktop\V-Pet Game\Game_window_energybar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(974, 779)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(80, 470, 281, 31))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.feed_Button = QtWidgets.QPushButton(self.centralwidget)
        self.feed_Button.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.feed_Button.setText("")
        self.feed_Button.setObjectName("feed_Button")
        self.walk_Button = QtWidgets.QPushButton(self.centralwidget)
        self.walk_Button.setGeometry(QtCore.QRect(100, 10, 71, 61))
        self.walk_Button.setText("")
        self.walk_Button.setObjectName("walk_Button")
        self.play_Button = QtWidgets.QPushButton(self.centralwidget)
        self.play_Button.setGeometry(QtCore.QRect(190, 10, 71, 61))
        self.play_Button.setText("")
        self.play_Button.setObjectName("play_Button")
        self.doctor_Button = QtWidgets.QPushButton(self.centralwidget)
        self.doctor_Button.setGeometry(QtCore.QRect(280, 10, 71, 61))
        self.doctor_Button.setText("")
        self.doctor_Button.setObjectName("doctor_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 80, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 80, 55, 16))
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 971, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 130, 501, 301))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(80, 540, 281, 31))
        self.progressBar_2.setProperty("value", 100)
        self.progressBar_2.setFormat("")
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(80, 610, 281, 31))
        self.progressBar_3.setProperty("value", 100)
        self.progressBar_3.setFormat("")
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 480, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 550, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 620, 55, 16))
        self.label_9.setObjectName("label_9")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(460, 470, 281, 31))
        self.progressBar_4.setProperty("value", 100)
        self.progressBar_4.setFormat("")
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(720, 480, 55, 16))
        self.label_10.setObjectName("label_10")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionSleep = QtWidgets.QAction(mainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Mariy\\Desktop\\V-Pet Game\\V-Pet Game/Sourses/sleep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSleep.setIcon(icon)
        self.actionSleep.setObjectName("actionSleep")
        self.actionplay = QtWidgets.QAction(mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Mariy\\Desktop\\V-Pet Game\\V-Pet Game/Sourses/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionplay.setIcon(icon1)
        self.actionplay.setObjectName("actionplay")
        self.actionWalk = QtWidgets.QAction(mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Mariy\\Desktop\\V-Pet Game\\V-Pet Game/Sourses/walk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWalk.setIcon(icon2)
        self.actionWalk.setObjectName("actionWalk")
        self.actionFood = QtWidgets.QAction(mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\Mariy\\Desktop\\V-Pet Game\\V-Pet Game/Sourses/food.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFood.setIcon(icon3)
        self.actionFood.setObjectName("actionFood")
        self.actionHelp = QtWidgets.QAction(mainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\Mariy\\Desktop\\V-Pet Game\\V-Pet Game/Sourses/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon4)
        self.actionHelp.setObjectName("actionHelp")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Virtual pet"))
        self.label_2.setText(_translate("mainWindow", "Feed"))
        self.label_3.setText(_translate("mainWindow", "Walk"))
        self.label_4.setText(_translate("mainWindow", "Play"))
        self.label_5.setText(_translate("mainWindow", "Doctor"))
        self.label_7.setText(_translate("mainWindow", "Hunger"))
        self.label_8.setText(_translate("mainWindow", "Mood"))
        self.label_9.setText(_translate("mainWindow", "Health"))
        self.label_10.setText(_translate("mainWindow", "Energy"))
        self.actionSleep.setText(_translate("mainWindow", "Sleep"))
        self.actionplay.setText(_translate("mainWindow", "play"))
        self.actionWalk.setText(_translate("mainWindow", "Walk"))
        self.actionFood.setText(_translate("mainWindow", "Food"))
        self.actionHelp.setText(_translate("mainWindow", "Help"))
