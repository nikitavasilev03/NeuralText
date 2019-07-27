# -*- coding: utf-8 -*-
#pylint: disable=no-name-in-module

from PyQt5.QtWidgets import QDialog

from include.designer.UI_DialogCreateNewNeural import Ui_Dialog

class CreateNewNeuralDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

        self.resaut = False
        pass
    
    @staticmethod
    def getData(Parent):
        dialog = CreateNewNeuralDialog()
        dialog.show()
        dialog.exec_()
        return dialog.lineEdit.text(), dialog.spinBox.value(), dialog.spinBox_2.value(), dialog.spinBox_3.value(), dialog.spinBox_4.value(), float(dialog.lineEdit_2.text())

    def accept_data(self):
        self.resaut = True
        self.close()
        pass

    def reject_data(self):
        self.close()
        pass
