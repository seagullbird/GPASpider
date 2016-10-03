# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.usernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridLayout.addWidget(self.usernameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pwdEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdEdit.setObjectName("pwdEdit")
        self.gridLayout.addWidget(self.pwdEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.vCodeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.vCodeEdit.setMaxLength(4)
        self.vCodeEdit.setFrame(True)
        self.vCodeEdit.setObjectName("vCodeEdit")
        self.gridLayout.addWidget(self.vCodeEdit, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setObjectName("login")
        self.gridLayout_2.addWidget(self.login, 3, 0, 1, 2)
        self.openGradeFile = QtWidgets.QPushButton(self.centralwidget)
        self.openGradeFile.setObjectName("openGradeFile")
        self.gridLayout_2.addWidget(self.openGradeFile, 4, 1, 1, 1)
        self.getGpa = QtWidgets.QPushButton(self.centralwidget)
        self.getGpa.setObjectName("getGpa")
        self.gridLayout_2.addWidget(self.getGpa, 4, 0, 1, 1)
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 2)
        self.gpaLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.gpaLabel.setFont(font)
        self.gpaLabel.setObjectName("gpaLabel")
        self.gridLayout_2.addWidget(self.gpaLabel, 5, 0, 1, 1)
        self.getVCode = QtWidgets.QPushButton(self.centralwidget)
        self.getVCode.setObjectName("getVCode")
        self.gridLayout_2.addWidget(self.getVCode, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "验证码"))
        self.login.setText(_translate("MainWindow", "登录"))
        self.openGradeFile.setText(_translate("MainWindow", "打开成绩文件"))
        self.getGpa.setText(_translate("MainWindow", "计算GPA"))
        self.title.setText(_translate("MainWindow", "北邮GPA爬取&计算"))
        self.gpaLabel.setText(_translate("MainWindow", "Gpa:"))
        self.getVCode.setText(_translate("MainWindow", "获得验证码"))

