# -*- coding: utf-8 -*-
#pylint: disable=no-name-in-module

import pickle
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt

from include.designer.UI_MainWindow import Ui_MainWindow
from include.CreateNewNeuralDialog import CreateNewNeuralDialog
from include.TrainDialog import TrainDialog
from include.TestDialog import TestDialog

from include.Neural import neuralNetwork

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Neural Text")

        self.bCreateNewNeural.clicked.connect(self.CreateNewNeural)
        self.bSaveNeural.clicked.connect(self.SaveNeural)
        self.bSaveAsNeural.clicked.connect(self.SaveAsNeural)
        self.bOpenNeural.clicked.connect(self.OpenNeural)
        self.bTestNeural.clicked.connect(self.TestNeural)

        self.Neural = None
        pass
    
    def CreateNewNeural(self):
        name, i_nodes, h_nodes, o_nodes, sh_nodes, lr = CreateNewNeuralDialog.getData(self)
        self.SetDataLabel(name, i_nodes, h_nodes, o_nodes, sh_nodes, lr, 0)
        self.Neural = neuralNetwork(name, i_nodes, h_nodes, o_nodes, sh_nodes, lr)
        pass
    
    def SaveNeural(self):
        if self.Neural is not None:
            f = open("Save\\" + self.Neural.Name +".neu", 'wb')
            pickle.dump(self.Neural, f)
            f.close()
        pass

    def SaveAsNeural(self):
        if self.Neural is not None:
            try:
                fname = QFileDialog.getSaveFileName(self, 'Save File', 'Save\\Neurals\\', 'Neural File (*.neu)')[0]
                f = open(fname, 'wb')
                pickle.dump(self.Neural, f)
                f.close()
            except:
                print("Error")
        pass

    def OpenNeural(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'Save\\Neurals\\')[0]  
            f = open(fname, 'rb')
            self.Neural = pickle.load(f)
            f.close()
            self.SetDataLabel(self.Neural.Name, self.Neural.InputNodes, self.Neural.HiddenNodes, self.Neural.OutputNodes, 
                            self.Neural.HiddenSloys, self.Neural.LearninGrate, self.Neural.examples)
        except:
            print("Error")
        pass

    def TestNeural(self):
        if self.Neural is not None:
            TestDialog.getData(self, self.Neural)
            self.SetDataLabel(self.Neural.Name, self.Neural.InputNodes, self.Neural.HiddenNodes, self.Neural.OutputNodes, 
                            self.Neural.HiddenSloys, self.Neural.LearninGrate, self.Neural.examples)
        pass

    def SetDataLabel(self, name, i_nodes, h_nodes, o_nodes, sh_nodes, lr, examples):
        self.lName.setText("Название: " + name)
        self.lCountInputNeuron.setText("Количество нейронов входного слоя: " + str(i_nodes))
        self.lCountHiddenNeuron.setText("Количество нейронов промежуточного слоя: " + str(h_nodes))
        self.lCountOutputNeuron.setText("Количество нейронов выходного слоя: " + str(o_nodes))
        self.lValueTraining.setText("Коэффицент обучения: " + str(lr))
        self.lCountHiddenNeural.setText("Количество нейронов промежуточного слоя: " + str(sh_nodes))
        self.lCountTraining.setText("Количество примеров обучения сети: " + str(examples))
        pass