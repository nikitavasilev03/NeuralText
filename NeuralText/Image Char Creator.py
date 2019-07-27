# -*- coding: utf-8 -*-
#pylint: disable=no-name-in-module

import sys
import pickle
from PIL import Image, ImageQt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QImage, QPixelFormat
from PyQt5.QtCore import Qt

from include.designer.UI_CreaterWindow import Ui_CreaterWindow
from include.PanelDrawWidget import PanelDraw
from include.wImage import ListDataImage, DataImage

class Creater(QMainWindow, Ui_CreaterWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Image Char Creator")

        self.bAdd.clicked.connect(self.AddChar)
        self.bSave.clicked.connect(self.Save)
        self.bClear.clicked.connect(self.Clear)
        self.bDeleteLast.clicked.connect(self.DeleteLast)
        self.bOpen.clicked.connect(self.Open)
        self.bChangeAll.clicked.connect(self.ChangeAll)

        self.panelDraw = PanelDraw(self)
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.panelDraw)
        
        self.panelDraw.penSize = 30
        self.listData = ListDataImage()
        self.dataImageLast = None
        pass
    
    def AddChar(self):
        if (self.lineEdit.text() != ""):
			# Создание элемента DataImage(название буквы, картинка)
            self.dataImageLast = DataImage(self.lineEdit.text(), ImageQt.fromqimage(self.panelDraw.Image))
            # Изменение размера изображения
            self.dataImageLast.image = self.dataImageLast.image.resize((self.spinWindth.value(), self.spinHeight.value()), Image.ANTIALIAS)
            # Добавление в общий список
            self.listData.Add(self.dataImageLast)
			# Обнавляем данные списка
            self.RefreshListWidget()
        pass

    def Save(self): #Сохранение списка изображений в файл
        try:
			#Вызов диалога сохранения в файла
            fname = QFileDialog.getSaveFileName(self, 'Save File', 'Save\\Examples\\', 'Training Neural File (*.mlr)')[0] 
            f = open(fname, 'wb') #открываем файл для записи
            self.listData.Mix() #перемешиваем список
            pickle.dump(self.listData, f) #записываем список в файл
            f.close() #закрываем файл
        except:
            print("File not save") #если не удалось
        pass
    
    def Open(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'Save\\Examples\\')[0]
            f = open(fname, 'rb')
            self.listData = pickle.load(f)
            f.close()
            self.RefreshListWidget()
        except:
            print("Error")
        pass

    def Clear(self):
        self.panelDraw.Clear()
        pass
    
    def DeleteLast(self):
        try:
            self.listData.Delete(self.dataImageLast)
        except:
            print("Error")
        self.RefreshListWidget()
        pass
    
    def ChangeAll(self):
        for i in self.listData.list:
            i.image = i.image.resize((self.spinWindth.value(), self.spinHeight.value()), Image.ANTIALIAS)
        pass

    def RefreshListWidget(self):
        self.listWidget.clear()
        for i in self.listData.GetCharWithCount():
            self.listWidget.addItem(str(i[0]) + ":  " + str(i[1])) 
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_E:
            self.AddChar()
        if event.key() == Qt.Key_C:
            self.Clear()
        if event.key() == Qt.Key_D:
            self.AddChar()
            self.Clear()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Creater()
    ex.show()
    sys.exit(app.exec_())
    pass