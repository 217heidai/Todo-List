# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 852)
        MainWindow.setStyleSheet("background-color: none;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1281, 851))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.day = QtWidgets.QWidget()
        self.day.setStyleSheet("border-radius: 15px;")
        self.day.setObjectName("day")
        self.frame = QtWidgets.QFrame(self.day)
        self.frame.setGeometry(QtCore.QRect(0, 0, 341, 861))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameapp = QtWidgets.QLabel(self.frame)
        self.nameapp.setGeometry(QtCore.QRect(20, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.nameapp.setFont(font)
        self.nameapp.setStyleSheet("color: rgb(91, 91, 91);")
        self.nameapp.setObjectName("nameapp")
        self.profile = QtWidgets.QLabel(self.frame)
        self.profile.setGeometry(QtCore.QRect(20, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.profile.setFont(font)
        self.profile.setStyleSheet("background-color: #00a300;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.profile.setAlignment(QtCore.Qt.AlignCenter)
        self.profile.setObjectName("profile")
        self.nameuser = QtWidgets.QLabel(self.frame)
        self.nameuser.setGeometry(QtCore.QRect(70, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(11)
        self.nameuser.setFont(font)
        self.nameuser.setObjectName("nameuser")
        self.myday1 = QtWidgets.QPushButton(self.frame)
        self.myday1.setGeometry(QtCore.QRect(0, 140, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.myday1.setFont(font)
        self.myday1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1.setStyleSheet("border: 0px;\n"
"color: #647783;\n"
"background-color: rgb(248, 249, 250);")
        self.myday1.setObjectName("myday1")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 140, 41, 61))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("background-color: none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/my day.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 21, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("color: #647783;\n"
"background-color: none;")
        self.label_2.setObjectName("label_2")
        self.myday1_2 = QtWidgets.QPushButton(self.frame)
        self.myday1_2.setGeometry(QtCore.QRect(0, 200, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.myday1_2.setFont(font)
        self.myday1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1_2.setStyleSheet("border: 0px;\n"
"color: #000000;\n"
"background-color: none;")
        self.myday1_2.setObjectName("myday1_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 41, 61))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("background-color: none;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/important.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.myday1_3 = QtWidgets.QPushButton(self.frame)
        self.myday1_3.setGeometry(QtCore.QRect(0, 260, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.myday1_3.setFont(font)
        self.myday1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1_3.setStyleSheet("border: 0px;\n"
"color: #000000;\n"
"background-color: none;")
        self.myday1_3.setObjectName("myday1_3")
        self.myday1_4 = QtWidgets.QPushButton(self.frame)
        self.myday1_4.setGeometry(QtCore.QRect(0, 320, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.myday1_4.setFont(font)
        self.myday1_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1_4.setStyleSheet("border: 0px;\n"
"color: #000000;\n"
"background-color: none;")
        self.myday1_4.setObjectName("myday1_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 41, 61))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("background-color: none;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/personal.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 41, 61))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("background-color: none;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/setting.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.day)
        self.label_6.setGeometry(QtCore.QRect(340, 0, 941, 851))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/bak_day.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.day)
        self.label_7.setGeometry(QtCore.QRect(380, 40, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(21)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.date = QtWidgets.QLabel(self.day)
        self.date.setGeometry(QtCore.QRect(380, 90, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setStyleSheet("color: rgb(255, 255, 255);")
        self.date.setObjectName("date")
        self.label_9 = QtWidgets.QLabel(self.day)
        self.label_9.setGeometry(QtCore.QRect(360, 220, 661, 391))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("images/bak_day.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.day)
        self.label_10.setGeometry(QtCore.QRect(650, 240, 331, 201))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("images/calender.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.day)
        self.label_11.setGeometry(QtCore.QRect(720, 430, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.day)
        self.label_12.setGeometry(QtCore.QRect(650, 500, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.day)
        self.label_13.setGeometry(QtCore.QRect(650, 530, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.addtask = QtWidgets.QLineEdit(self.day)
        self.addtask.setGeometry(QtCore.QRect(420, 750, 781, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.addtask.setFont(font)
        self.addtask.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(251, 226, 255);")
        self.addtask.setAlignment(QtCore.Qt.AlignCenter)
        self.addtask.setObjectName("addtask")
        self.close1 = QtWidgets.QPushButton(self.day)
        self.close1.setGeometry(QtCore.QRect(1240, 10, 31, 31))
        self.close1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close1.setStyleSheet("background-color: none;\n"
"")
        self.close1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close1.setIcon(icon)
        self.close1.setIconSize(QtCore.QSize(36, 37))
        self.close1.setObjectName("close1")
        self.mini1 = QtWidgets.QPushButton(self.day)
        self.mini1.setGeometry(QtCore.QRect(1200, 0, 31, 51))
        self.mini1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mini1.setStyleSheet("background-color: none;\n"
"")
        self.mini1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mini1.setIcon(icon1)
        self.mini1.setIconSize(QtCore.QSize(36, 37))
        self.mini1.setObjectName("mini1")
        self.label_14 = QtWidgets.QLabel(self.day)
        self.label_14.setGeometry(QtCore.QRect(420, 755, 55, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(29)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(113, 113, 113);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.submit = QtWidgets.QPushButton(self.day)
        self.submit.setGeometry(QtCore.QRect(1140, 750, 41, 61))
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet("background-color: none;\n"
"")
        self.submit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/submit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit.setIcon(icon2)
        self.submit.setIconSize(QtCore.QSize(36, 37))
        self.submit.setObjectName("submit")
        self.stackedWidget.addWidget(self.day)
        self.day_task = QtWidgets.QWidget()
        self.day_task.setStyleSheet("border-radius: 2px;")
        self.day_task.setObjectName("day_task")
        self.label_27 = QtWidgets.QLabel(self.day_task)
        self.label_27.setGeometry(QtCore.QRect(380, 40, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(21)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.day_task)
        self.label_29.setGeometry(QtCore.QRect(340, 0, 941, 851))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("images/bak_day.jpg"))
        self.label_29.setObjectName("label_29")
        self.mini2 = QtWidgets.QPushButton(self.day_task)
        self.mini2.setGeometry(QtCore.QRect(1200, 0, 31, 51))
        self.mini2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mini2.setStyleSheet("background-color: none;\n"
"")
        self.mini2.setText("")
        self.mini2.setIcon(icon1)
        self.mini2.setIconSize(QtCore.QSize(36, 37))
        self.mini2.setObjectName("mini2")
        self.addtask_3 = QtWidgets.QLineEdit(self.day_task)
        self.addtask_3.setGeometry(QtCore.QRect(420, 750, 781, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.addtask_3.setFont(font)
        self.addtask_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(251, 226, 255);")
        self.addtask_3.setAlignment(QtCore.Qt.AlignCenter)
        self.addtask_3.setObjectName("addtask_3")
        self.label_30 = QtWidgets.QLabel(self.day_task)
        self.label_30.setGeometry(QtCore.QRect(420, 755, 55, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(29)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(113, 113, 113);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.frame_3 = QtWidgets.QFrame(self.day_task)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 341, 861))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.nameapp_3 = QtWidgets.QLabel(self.frame_3)
        self.nameapp_3.setGeometry(QtCore.QRect(20, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.nameapp_3.setFont(font)
        self.nameapp_3.setStyleSheet("color: rgb(91, 91, 91);")
        self.nameapp_3.setObjectName("nameapp_3")
        self.profile2 = QtWidgets.QLabel(self.frame_3)
        self.profile2.setGeometry(QtCore.QRect(20, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.profile2.setFont(font)
        self.profile2.setStyleSheet("background-color: #00a300;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.profile2.setAlignment(QtCore.Qt.AlignCenter)
        self.profile2.setObjectName("profile2")
        self.nameuser2 = QtWidgets.QLabel(self.frame_3)
        self.nameuser2.setGeometry(QtCore.QRect(70, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(11)
        self.nameuser2.setFont(font)
        self.nameuser2.setObjectName("nameuser2")
        self.myday1_9 = QtWidgets.QPushButton(self.frame_3)
        self.myday1_9.setGeometry(QtCore.QRect(0, 140, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.myday1_9.setFont(font)
        self.myday1_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1_9.setStyleSheet("border: 0px;\n"
"color: #647783;\n"
"background-color: rgb(248, 249, 250);")
        self.myday1_9.setObjectName("myday1_9")
        self.label_34 = QtWidgets.QLabel(self.frame_3)
        self.label_34.setGeometry(QtCore.QRect(20, 140, 41, 61))
        self.label_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_34.setStyleSheet("background-color: none;")
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("images/my day.png"))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_3)
        self.label_35.setGeometry(QtCore.QRect(10, 140, 21, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_35.setStyleSheet("color: #647783;\n"
"background-color: none;")
        self.label_35.setObjectName("label_35")
        self.myday1_10 = QtWidgets.QPushButton(self.frame_3)
        self.myday1_10.setGeometry(QtCore.QRect(0, 200, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.myday1_10.setFont(font)
        self.myday1_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1_10.setStyleSheet("border: 0px;\n"
"color: #000000;\n"
"background-color: none;")
        self.myday1_10.setObjectName("myday1_10")
        self.label_36 = QtWidgets.QLabel(self.frame_3)
        self.label_36.setGeometry(QtCore.QRect(20, 200, 41, 61))
        self.label_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_36.setStyleSheet("background-color: none;")
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("images/important.png"))
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.myday1_11 = QtWidgets.QPushButton(self.frame_3)
        self.myday1_11.setGeometry(QtCore.QRect(0, 260, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.myday1_11.setFont(font)
        self.myday1_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1_11.setStyleSheet("border: 0px;\n"
"color: #000000;\n"
"background-color: none;")
        self.myday1_11.setObjectName("myday1_11")
        self.myday1_12 = QtWidgets.QPushButton(self.frame_3)
        self.myday1_12.setGeometry(QtCore.QRect(0, 320, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.myday1_12.setFont(font)
        self.myday1_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.myday1_12.setStyleSheet("border: 0px;\n"
"color: #000000;\n"
"background-color: none;")
        self.myday1_12.setObjectName("myday1_12")
        self.label_37 = QtWidgets.QLabel(self.frame_3)
        self.label_37.setGeometry(QtCore.QRect(20, 260, 41, 61))
        self.label_37.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_37.setStyleSheet("background-color: none;")
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap("images/personal.png"))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_3)
        self.label_38.setGeometry(QtCore.QRect(20, 320, 41, 61))
        self.label_38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_38.setStyleSheet("background-color: none;")
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("images/setting.png"))
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.date2 = QtWidgets.QLabel(self.day_task)
        self.date2.setGeometry(QtCore.QRect(380, 90, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.date2.setFont(font)
        self.date2.setStyleSheet("color: rgb(255, 255, 255);")
        self.date2.setObjectName("date2")
        self.close2 = QtWidgets.QPushButton(self.day_task)
        self.close2.setGeometry(QtCore.QRect(1240, 10, 31, 31))
        self.close2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close2.setStyleSheet("background-color: none;\n"
"")
        self.close2.setText("")
        self.close2.setIcon(icon)
        self.close2.setIconSize(QtCore.QSize(36, 37))
        self.close2.setObjectName("close2")
        self.task1 = QtWidgets.QLabel(self.day_task)
        self.task1.setGeometry(QtCore.QRect(380, 130, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task1.setFont(font)
        self.task1.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task1.setText("")
        self.task1.setAlignment(QtCore.Qt.AlignCenter)
        self.task1.setObjectName("task1")
        self.task2 = QtWidgets.QLabel(self.day_task)
        self.task2.setGeometry(QtCore.QRect(380, 200, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task2.setFont(font)
        self.task2.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task2.setText("")
        self.task2.setAlignment(QtCore.Qt.AlignCenter)
        self.task2.setObjectName("task2")
        self.task4 = QtWidgets.QLabel(self.day_task)
        self.task4.setGeometry(QtCore.QRect(380, 340, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task4.setFont(font)
        self.task4.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task4.setText("")
        self.task4.setAlignment(QtCore.Qt.AlignCenter)
        self.task4.setObjectName("task4")
        self.task3 = QtWidgets.QLabel(self.day_task)
        self.task3.setGeometry(QtCore.QRect(380, 270, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task3.setFont(font)
        self.task3.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task3.setText("")
        self.task3.setAlignment(QtCore.Qt.AlignCenter)
        self.task3.setObjectName("task3")
        self.task6 = QtWidgets.QLabel(self.day_task)
        self.task6.setGeometry(QtCore.QRect(380, 480, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task6.setFont(font)
        self.task6.setStyleSheet("background-color: rgb(255, 213, 246, 180);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task6.setText("")
        self.task6.setAlignment(QtCore.Qt.AlignCenter)
        self.task6.setObjectName("task6")
        self.task8 = QtWidgets.QLabel(self.day_task)
        self.task8.setGeometry(QtCore.QRect(380, 620, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task8.setFont(font)
        self.task8.setStyleSheet("background-color: rgb(255, 213, 246, 180);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task8.setText("")
        self.task8.setAlignment(QtCore.Qt.AlignCenter)
        self.task8.setObjectName("task8")
        self.task7 = QtWidgets.QLabel(self.day_task)
        self.task7.setGeometry(QtCore.QRect(380, 550, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task7.setFont(font)
        self.task7.setStyleSheet("background-color: rgb(255, 213, 246, 180);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task7.setText("")
        self.task7.setAlignment(QtCore.Qt.AlignCenter)
        self.task7.setObjectName("task7")
        self.task5 = QtWidgets.QLabel(self.day_task)
        self.task5.setGeometry(QtCore.QRect(380, 410, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.task5.setFont(font)
        self.task5.setStyleSheet("background-color: rgb(255, 213, 246, 150);\n"
"color: rgb(10, 10, 10);\n"
"border-radius: 7px;")
        self.task5.setText("")
        self.task5.setAlignment(QtCore.Qt.AlignCenter)
        self.task5.setObjectName("task5")
        self.sub1 = QtWidgets.QPushButton(self.day_task)
        self.sub1.setGeometry(QtCore.QRect(390, 130, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub1.setFont(font)
        self.sub1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub1.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub1.setIconSize(QtCore.QSize(36, 37))
        self.sub1.setObjectName("sub1")
        self.sub2 = QtWidgets.QPushButton(self.day_task)
        self.sub2.setGeometry(QtCore.QRect(390, 200, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub2.setFont(font)
        self.sub2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub2.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub2.setIconSize(QtCore.QSize(36, 37))
        self.sub2.setObjectName("sub2")
        self.sub4 = QtWidgets.QPushButton(self.day_task)
        self.sub4.setGeometry(QtCore.QRect(390, 340, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub4.setFont(font)
        self.sub4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub4.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub4.setIconSize(QtCore.QSize(36, 37))
        self.sub4.setObjectName("sub4")
        self.sub3 = QtWidgets.QPushButton(self.day_task)
        self.sub3.setGeometry(QtCore.QRect(390, 270, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub3.setFont(font)
        self.sub3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub3.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub3.setIconSize(QtCore.QSize(36, 37))
        self.sub3.setObjectName("sub3")
        self.sub7 = QtWidgets.QPushButton(self.day_task)
        self.sub7.setGeometry(QtCore.QRect(390, 550, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub7.setFont(font)
        self.sub7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub7.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub7.setIconSize(QtCore.QSize(36, 37))
        self.sub7.setObjectName("sub7")
        self.sub5 = QtWidgets.QPushButton(self.day_task)
        self.sub5.setGeometry(QtCore.QRect(390, 410, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub5.setFont(font)
        self.sub5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub5.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub5.setIconSize(QtCore.QSize(36, 37))
        self.sub5.setObjectName("sub5")
        self.sub6 = QtWidgets.QPushButton(self.day_task)
        self.sub6.setGeometry(QtCore.QRect(390, 480, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub6.setFont(font)
        self.sub6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub6.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub6.setIconSize(QtCore.QSize(36, 37))
        self.sub6.setObjectName("sub6")
        self.sub8 = QtWidgets.QPushButton(self.day_task)
        self.sub8.setGeometry(QtCore.QRect(390, 620, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        self.sub8.setFont(font)
        self.sub8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub8.setStyleSheet("background-color: none;\n"
"color: rgb(127, 127, 127);\n"
"")
        self.sub8.setIconSize(QtCore.QSize(36, 37))
        self.sub8.setObjectName("sub8")
        self.submit_2 = QtWidgets.QPushButton(self.day_task)
        self.submit_2.setGeometry(QtCore.QRect(1140, 750, 41, 61))
        self.submit_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_2.setStyleSheet("background-color: none;")
        self.submit_2.setText("")
        self.submit_2.setIcon(icon2)
        self.submit_2.setIconSize(QtCore.QSize(36, 37))
        self.submit_2.setObjectName("submit_2")
        self.delete1 = QtWidgets.QPushButton(self.day_task)
        self.delete1.setGeometry(QtCore.QRect(1190, 130, 41, 51))
        self.delete1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete1.setStyleSheet("background-color: none;")
        self.delete1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete1.setIcon(icon3)
        self.delete1.setIconSize(QtCore.QSize(36, 37))
        self.delete1.setObjectName("delete1")
        self.delete2 = QtWidgets.QPushButton(self.day_task)
        self.delete2.setGeometry(QtCore.QRect(1190, 200, 41, 51))
        self.delete2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete2.setStyleSheet("background-color: none;")
        self.delete2.setText("")
        self.delete2.setIcon(icon3)
        self.delete2.setIconSize(QtCore.QSize(36, 37))
        self.delete2.setObjectName("delete2")
        self.delete3 = QtWidgets.QPushButton(self.day_task)
        self.delete3.setGeometry(QtCore.QRect(1190, 270, 41, 51))
        self.delete3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete3.setStyleSheet("background-color: none;")
        self.delete3.setText("")
        self.delete3.setIcon(icon3)
        self.delete3.setIconSize(QtCore.QSize(36, 37))
        self.delete3.setObjectName("delete3")
        self.delete4 = QtWidgets.QPushButton(self.day_task)
        self.delete4.setGeometry(QtCore.QRect(1190, 340, 41, 51))
        self.delete4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete4.setStyleSheet("background-color: none;")
        self.delete4.setText("")
        self.delete4.setIcon(icon3)
        self.delete4.setIconSize(QtCore.QSize(36, 37))
        self.delete4.setObjectName("delete4")
        self.delete7 = QtWidgets.QPushButton(self.day_task)
        self.delete7.setGeometry(QtCore.QRect(1190, 550, 41, 51))
        self.delete7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete7.setStyleSheet("background-color: none;")
        self.delete7.setText("")
        self.delete7.setIcon(icon3)
        self.delete7.setIconSize(QtCore.QSize(36, 37))
        self.delete7.setObjectName("delete7")
        self.delete5 = QtWidgets.QPushButton(self.day_task)
        self.delete5.setGeometry(QtCore.QRect(1190, 410, 41, 51))
        self.delete5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete5.setStyleSheet("background-color: none;")
        self.delete5.setText("")
        self.delete5.setIcon(icon3)
        self.delete5.setIconSize(QtCore.QSize(36, 37))
        self.delete5.setObjectName("delete5")
        self.delete8 = QtWidgets.QPushButton(self.day_task)
        self.delete8.setGeometry(QtCore.QRect(1190, 620, 41, 51))
        self.delete8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete8.setStyleSheet("background-color: none;")
        self.delete8.setText("")
        self.delete8.setIcon(icon3)
        self.delete8.setIconSize(QtCore.QSize(36, 37))
        self.delete8.setObjectName("delete8")
        self.delete6 = QtWidgets.QPushButton(self.day_task)
        self.delete6.setGeometry(QtCore.QRect(1190, 480, 41, 51))
        self.delete6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete6.setStyleSheet("background-color: none;")
        self.delete6.setText("")
        self.delete6.setIcon(icon3)
        self.delete6.setIconSize(QtCore.QSize(36, 37))
        self.delete6.setObjectName("delete6")
        self.label_29.raise_()
        self.mini2.raise_()
        self.addtask_3.raise_()
        self.label_30.raise_()
        self.frame_3.raise_()
        self.date2.raise_()
        self.close2.raise_()
        self.label_27.raise_()
        self.task1.raise_()
        self.task2.raise_()
        self.task4.raise_()
        self.task3.raise_()
        self.task6.raise_()
        self.task8.raise_()
        self.task7.raise_()
        self.task5.raise_()
        self.sub1.raise_()
        self.sub2.raise_()
        self.sub4.raise_()
        self.sub3.raise_()
        self.sub7.raise_()
        self.sub5.raise_()
        self.sub6.raise_()
        self.sub8.raise_()
        self.submit_2.raise_()
        self.delete1.raise_()
        self.delete2.raise_()
        self.delete3.raise_()
        self.delete4.raise_()
        self.delete7.raise_()
        self.delete5.raise_()
        self.delete8.raise_()
        self.delete6.raise_()
        self.task1.hide()
        self.task2.hide()
        self.task3.hide()
        self.task4.hide()
        self.task5.hide()
        self.task6.hide()
        self.task7.hide()
        self.task8.hide()
        self.sub1.hide()
        self.sub2.hide()
        self.sub3.hide()
        self.sub4.hide()
        self.sub5.hide()
        self.sub6.hide()
        self.sub7.hide()
        self.sub8.hide()
        self.delete1.hide()
        self.delete2.hide()
        self.delete3.hide()
        self.delete4.hide()
        self.delete5.hide()
        self.delete6.hide()
        self.delete7.hide()
        self.delete8.hide()
        self.stackedWidget.addWidget(self.day_task)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.close1.clicked.connect(MainWindow.close)
        self.mini1.clicked.connect(MainWindow.showMinimized)
        self.close2.clicked.connect(MainWindow.close)
        self.mini2.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameapp.setText(_translate("MainWindow", "To Do List"))
        self.profile.setText(_translate("MainWindow", "A"))
        self.nameuser.setText(_translate("MainWindow", "Amir Abbas Ataei"))
        self.myday1.setText(_translate("MainWindow", "     My Day                             "))
        self.label_2.setText(_translate("MainWindow", "|"))
        self.myday1_2.setText(_translate("MainWindow", "    Important                             "))
        self.myday1_3.setText(_translate("MainWindow", " Personal                             "))
        self.myday1_4.setText(_translate("MainWindow", "Setting                             "))
        self.label_7.setText(_translate("MainWindow", "My Day"))
        self.date.setText(_translate("MainWindow", "Thursday , September 9"))
        self.label_11.setText(_translate("MainWindow", "Focus on your day"))
        self.label_12.setText(_translate("MainWindow", "Get things done with My Day, a list that"))
        self.label_13.setText(_translate("MainWindow", "refireshes every day"))
        self.label_14.setText(_translate("MainWindow", "+"))
        self.label_27.setText(_translate("MainWindow", "My Day"))
        self.label_30.setText(_translate("MainWindow", "+"))
        self.nameapp_3.setText(_translate("MainWindow", "To Do List"))
        self.profile2.setText(_translate("MainWindow", "A"))
        self.nameuser2.setText(_translate("MainWindow", "Amir Abbas Ataei"))
        self.myday1_9.setText(_translate("MainWindow", "     My Day                             "))
        self.label_35.setText(_translate("MainWindow", "|"))
        self.myday1_10.setText(_translate("MainWindow", "    Important                             "))
        self.myday1_11.setText(_translate("MainWindow", " Personal                             "))
        self.myday1_12.setText(_translate("MainWindow", "Setting                             "))
        self.date2.setText(_translate("MainWindow", "Thursday , September 9"))
        self.sub1.setText(_translate("MainWindow", "O"))
        self.sub2.setText(_translate("MainWindow", "O"))
        self.sub4.setText(_translate("MainWindow", "O"))
        self.sub3.setText(_translate("MainWindow", "O"))
        self.sub7.setText(_translate("MainWindow", "O"))
        self.sub5.setText(_translate("MainWindow", "O"))
        self.sub6.setText(_translate("MainWindow", "O"))
        self.sub8.setText(_translate("MainWindow", "O"))
