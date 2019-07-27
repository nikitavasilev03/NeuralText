# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCreateNewNeural.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 373)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 330, 391, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 391, 16))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 391, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(20, 90, 391, 22))
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000000)
        self.spinBox.setObjectName("spinBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 391, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(20, 190, 391, 22))
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(1000000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 391, 16))
        self.label_5.setObjectName("label_5")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(20, 240, 391, 22))
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(1000000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 391, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 391, 16))
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(20, 140, 391, 22))
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(1000000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 290, 391, 22))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 391, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Коэффицент обучения:"))
        self.label_2.setText(_translate("Dialog", "Количество нейронов входного слоя:"))
        self.label_5.setText(_translate("Dialog", "Количество промежуточных слоев слоев:"))
        self.label.setText(_translate("Dialog", "Название нейроной сети:"))
        self.label_3.setText(_translate("Dialog", "Количество нейронов промежуточного слоя:"))
        self.lineEdit_2.setText(_translate("Dialog", "0.1"))
        self.label_4.setText(_translate("Dialog", "Количество нейронов выходного слоя:"))

