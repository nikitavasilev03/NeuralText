# -*- coding: utf-8 -*-
#pylint: disable=no-name-in-module

import pickle, numpy
from PIL import Image, ImageQt
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QImage, QPainter, QImage, QPixmap, QPen
from PyQt5.QtCore import Qt, QPoint

from include.designer.UI_TestDialog import Ui_TestDialog
from include.PanelDrawWidget import PanelDraw
from include.wImage import ListDataImage, DataImage, ImageToArray

class TestDialog(QDialog, Ui_TestDialog):
    def __init__(self, Parent, Neural):
        QDialog.__init__(self)
        self.setupUi(self)

        self.bClear.clicked.connect(self.Clear)
        self.bGetChar.clicked.connect(self.GetChar)
        self.bOpenFileTrain.clicked.connect(self.TrainFromFile)
        self.bOpenFileTest.clicked.connect(self.OpenFileTest)
        self.bTest1.clicked.connect(self.TestOne)
        self.bOpen2.clicked.connect(self.OpenNeuralTwo)
        self.bTest2.clicked.connect(self.TestTwo)

        self.panelDraw = PanelDraw(self)
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.panelDraw)
        self.panelDraw.penSize = 30

        self.testData = None
        self.Neural = Neural
        self.Neural2 = None
        self.lName1.setText("Название: " + Neural.Name)
        pass

    def Clear(self):
        self.panelDraw.Clear()
        pass

    def OpenNeuralTwo(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'Save\\Neurals\\')[0]
            f = open(fname, 'rb')
            self.Neural2 = pickle.load(f)
            f.close()
            self.lName2.setText("Название: " + self.Neural2.Name)
        except:
            print("Error")
            return None
        pass

    def TrainFromFile(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'Save\\Examples\\')[0]
            f = open(fname, 'rb')
            listData = pickle.load(f)
            f.close()
        except:
            print("Error")
            return None
        
        if listData is not None:
            
            self.lStatusTrain.setText("Идет обучение...")
            self.repaint()    
            ls = listData.GetAllChar()
            dc = dict.fromkeys(ls, 0)
            for i in ls:
                dc[i] = listData.GetChatPos(i)
            self.Neural.dc = dc # Словарь сети
            for i in range(self.spinBox.value()): # Количество повторений обучения
                for i in listData.list: # Перебираем все экземпляры материала обучения 
                    all_values = ImageToArray(i.image)
                    inputs = (all_values / 255.0 * 0.99) + 0.01 
                    targets = numpy.zeros(len(ls)) + 0.01
                    targets[dc[i.name]] = 0.99
                    self.Neural.Train(inputs, targets)
            self.lStatusTrain.setText("Готово!")
        pass

    def OpenFileTest(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'Save\\Examples\\')[0]
            f = open(fname, 'rb')
            self.testData = pickle.load(f)
            f.close()
            self.lCountExamples.setText("Количество примеров - " + str(len(self.testData.list)))
        except:
            print("Error")
            return None
        pass
    
    def GetChar(self):
        image = ImageQt.fromqimage(self.panelDraw.Image).resize((32, 32), Image.ANTIALIAS)
        all_values = ImageToArray(image)
        inputs = (all_values / 255.0 * 0.99) + 0.01
        outputs = self.Neural.Query(inputs)
        resuat = numpy.argmax(outputs)
        answer = None
        for name, value in self.Neural.dc.items():  
            if value == resuat:
                self.lResult.setText(name)
                answer = name
        if ((self.lineEditRes.text() != "") & (self.lineEditRes.text() != answer)):
            targets = numpy.zeros(len(self.Neural.dc)) + 0.01
            targets[self.Neural.dc[self.lineEditRes.text()]] = 0.99
            self.Neural.Train(inputs, targets)
        pass

    def TestOne(self):
        if self.testData is not None:
            ls = self.testData.list
            countTrue = 0
            countFalse = 0
            self.lStatusTest.setText("Идет тестирование...")
            self.repaint()
            for i in ls:
                all_values = ImageToArray(i.image)
                inputs = (all_values / 255.0 * 0.99) + 0.01
                outputs = self.Neural.Query(inputs)
                resuat = numpy.argmax(outputs)
                answer = None
                for name, value in self.Neural.dc.items():  
                    if value == resuat:
                        answer = name    
                if (answer == i.name):
                    countTrue += 1
                else:
                    countFalse += 1
                    if (self.checkBox.isChecked()):
                        targets = numpy.zeros(len(self.Neural.dc)) + 0.01
                        targets[self.Neural.dc[i.name]] = 0.99
                        self.Neural.Train(inputs, targets)

            self.lTrue1.setText("Верно - " + str(countTrue))
            self.lFalse1.setText("Неверно - " + str(countFalse))
            self.lStatusTest.setText("Готово!")
        pass

    def TestTwo(self):
        if self.testData is not None:
            ls = self.testData.list
            countTrue = 0
            countFalse = 0
            self.lStatusTest.setText("Идет тестирование...")
            self.repaint()
            for i in ls:
                all_values = ImageToArray(i.image)
                inputs = (all_values / 255.0 * 0.99) + 0.01
                outputs = self.Neural2.Query(inputs)
                resuat = numpy.argmax(outputs)
                answer = None
                for name, value in self.Neural2.dc.items():  
                    if value == resuat:
                        answer = name    
                if (answer == i.name):
                    countTrue += 1
                else:
                    countFalse += 1
                    if (self.checkBox.isChecked()):
                        targets = numpy.zeros(len(self.Neural2.dc)) + 0.01
                        targets[self.Neural2.dc[i.name]] = 0.99
                        self.Neural2.Train(inputs, targets)

            self.lTrue2.setText("Верно - " + str(countTrue))
            self.lFalse2.setText("Неверно - " + str(countFalse))
            self.lStatusTest.setText("Готово!")
        pass


    @staticmethod
    def getData(Parent, Neural):
        dialog = TestDialog(Parent, Neural)
        dialog.show()
        dialog.exec_()
        pass