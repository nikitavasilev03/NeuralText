# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogTrainNeural.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogTrainNeural(object):
    def setupUi(self, DialogTrainNeural):
        DialogTrainNeural.setObjectName("DialogTrainNeural")
        DialogTrainNeural.resize(441, 499)
        self.widget = QtWidgets.QWidget(DialogTrainNeural)
        self.widget.setGeometry(QtCore.QRect(20, 20, 400, 400))
        self.widget.setObjectName("widget")
        self.bOpen = QtWidgets.QPushButton(DialogTrainNeural)
        self.bOpen.setGeometry(QtCore.QRect(130, 430, 161, 28))
        self.bOpen.setObjectName("bOpen")
        self.bTrain = QtWidgets.QPushButton(DialogTrainNeural)
        self.bTrain.setGeometry(QtCore.QRect(130, 460, 161, 28))
        self.bTrain.setObjectName("bTrain")

        self.retranslateUi(DialogTrainNeural)
        QtCore.QMetaObject.connectSlotsByName(DialogTrainNeural)

    def retranslateUi(self, DialogTrainNeural):
        _translate = QtCore.QCoreApplication.translate
        DialogTrainNeural.setWindowTitle(_translate("DialogTrainNeural", "Dialog"))
        self.bOpen.setText(_translate("DialogTrainNeural", "Выбрать файл обучения"))
        self.bTrain.setText(_translate("DialogTrainNeural", "Обучть"))

