# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreaterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreaterWindow(object):
    def setupUi(self, CreaterWindow):
        CreaterWindow.setObjectName("CreaterWindow")
        CreaterWindow.resize(882, 528)
        self.centralwidget = QtWidgets.QWidget(CreaterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 400, 400))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 430, 91, 16))
        self.label_2.setObjectName("label_2")
        self.bAdd = QtWidgets.QPushButton(self.centralwidget)
        self.bAdd.setGeometry(QtCore.QRect(20, 460, 121, 28))
        self.bAdd.setObjectName("bAdd")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 430, 61, 21))
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.bSave = QtWidgets.QPushButton(self.centralwidget)
        self.bSave.setGeometry(QtCore.QRect(770, 90, 101, 41))
        self.bSave.setObjectName("bSave")
        self.bOpen = QtWidgets.QPushButton(self.centralwidget)
        self.bOpen.setGeometry(QtCore.QRect(770, 40, 101, 41))
        self.bOpen.setObjectName("bOpen")
        self.bDeleteLast = QtWidgets.QPushButton(self.centralwidget)
        self.bDeleteLast.setGeometry(QtCore.QRect(20, 490, 121, 31))
        self.bDeleteLast.setObjectName("bDeleteLast")
        self.bClear = QtWidgets.QPushButton(self.centralwidget)
        self.bClear.setGeometry(QtCore.QRect(150, 460, 111, 61))
        self.bClear.setObjectName("bClear")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(510, 40, 256, 481))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 430, 191, 16))
        self.label_3.setObjectName("label_3")
        self.spinWindth = QtWidgets.QSpinBox(self.centralwidget)
        self.spinWindth.setGeometry(QtCore.QRect(270, 450, 91, 21))
        self.spinWindth.setAlignment(QtCore.Qt.AlignCenter)
        self.spinWindth.setMinimum(10)
        self.spinWindth.setMaximum(400)
        self.spinWindth.setProperty("value", 100)
        self.spinWindth.setObjectName("spinWindth")
        self.spinHeight = QtWidgets.QSpinBox(self.centralwidget)
        self.spinHeight.setGeometry(QtCore.QRect(270, 470, 91, 21))
        self.spinHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.spinHeight.setMinimum(10)
        self.spinHeight.setMaximum(400)
        self.spinHeight.setProperty("value", 100)
        self.spinHeight.setObjectName("spinHeight")
        self.bChangeAll = QtWidgets.QPushButton(self.centralwidget)
        self.bChangeAll.setGeometry(QtCore.QRect(370, 450, 131, 41))
        self.bChangeAll.setObjectName("bChangeAll")
        CreaterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreaterWindow)
        QtCore.QMetaObject.connectSlotsByName(CreaterWindow)

    def retranslateUi(self, CreaterWindow):
        _translate = QtCore.QCoreApplication.translate
        CreaterWindow.setWindowTitle(_translate("CreaterWindow", "MainWindow"))
        self.label.setText(_translate("CreaterWindow", "Созданные:"))
        self.label_2.setText(_translate("CreaterWindow", "Символ:"))
        self.bAdd.setText(_translate("CreaterWindow", "Добавить"))
        self.bSave.setText(_translate("CreaterWindow", "Сохранить"))
        self.bOpen.setText(_translate("CreaterWindow", "Открыть"))
        self.bDeleteLast.setText(_translate("CreaterWindow", "Удалить последний"))
        self.bClear.setText(_translate("CreaterWindow", "Очистить"))
        self.label_3.setText(_translate("CreaterWindow", "Итоговый размер изображения"))
        self.bChangeAll.setText(_translate("CreaterWindow", "Применить ко всем"))

