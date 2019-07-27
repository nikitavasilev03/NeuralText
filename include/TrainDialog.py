# -*- coding: utf-8 -*-
#pylint: disable=no-name-in-module

import pickle, numpy
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QImage, QPainter, QImage, QPixmap, QPen
from PyQt5.QtCore import Qt, QPoint

from include.designer.UI_DialogTrainNeural import Ui_DialogTrainNeural
from include.PanelDrawWidget import PanelDraw
from include.wImage import ListDataImage, DataImage, ImageToArray


class TrainDialog(QDialog, Ui_DialogTrainNeural):
    def __init__(self, Parent, Neural):
        QDialog.__init__(self)
        self.setupUi(self)

        self.bOpen.clicked.connect(self.Open)
        self.bTrain.clicked.connect(self.Train)

        self.panelDraw = PanelDraw(self)
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.panelDraw)
        self.panelDraw.penSize = 30

        self.panelDraw.readOnly = True
        self.listData = None
        self.Neural = Neural
        pass

    def Open(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'Save\\Examples\\')[0]
            f = open(fname, 'rb')
            self.listData = pickle.load(f)
            f.close()
        except:
            print("Error")
        pass
    
    def Train(self):
        if self.listData is not None:
            ls = self.listData.GetAllChar()
            dc = dict.fromkeys(ls, 0)
            for i in ls:
                dc[i] = self.listData.GetChatPos(i)
            self.Neural.dc = dc
            for i in self.listData.list:
                all_values = ImageToArray(i.image)
                inputs = (all_values / 255.0 * 0.99) + 0.01 
                targets = numpy.zeros(len(ls)) + 0.01
                targets[dc[i.name]] = 0.99
                self.Neural.Train(inputs, targets)
        pass

    @staticmethod
    def getData(Parent, Neural):
        dialog = TrainDialog(Parent, Neural)
        dialog.show()
        dialog.exec_()
        pass

