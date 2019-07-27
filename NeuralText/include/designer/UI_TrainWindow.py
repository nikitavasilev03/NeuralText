# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrainWindow(object):
    def setupUi(self, TrainWindow):
        TrainWindow.setObjectName("TrainWindow")
        TrainWindow.resize(943, 768)
        self.widget = QtWidgets.QWidget(TrainWindow)
        self.widget.setGeometry(QtCore.QRect(40, 40, 400, 400))
        self.widget.setObjectName("widget")

        self.retranslateUi(TrainWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainWindow)

    def retranslateUi(self, TrainWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainWindow.setWindowTitle(_translate("TrainWindow", "Form"))

