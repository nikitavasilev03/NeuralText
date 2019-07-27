# -*- coding: utf-8 -*-
#pylint: disable=no-name-in-module

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPainter, QImage, QPixmap, QPen
from PyQt5.QtCore import Qt, QPoint

from include.designer.UI_WidgetPanelDraw import Ui_PanelDraw
from PIL.ImageQt import ImageQt

class PanelDraw(QWidget, Ui_PanelDraw):
    def __init__(self, Parent):
        QWidget.__init__(self)
        self.setupUi(self)

        self.Image = QImage(self.size(), QImage.Format_RGB32)
        self.Image.fill(Qt.white)
        
        self.dx = Parent.widget.x() / 2
        self.dy = Parent.widget.y() / 2
        
        self.readOnly = False
        self.drawing = False
        self.penSize = 2
        self.penColor = Qt.black
        pass

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton) & (not self.readOnly):
            self.drawing = True
            
            self.lastPoint = event.pos()
            self.lastPoint.setX(self.lastPoint.x() + self.dx)
            self.lastPoint.setY(self.lastPoint.y() + self.dy)
        pass

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.Image)
            painter.setPen(QPen(self.penColor, self.penSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            
            pos = event.pos()
            pos.setX(pos.x() + self.dx)
            pos.setY(pos.y() + self.dy)
            painter.drawLine(self.lastPoint, pos)
            self.lastPoint = pos
            
            self.update()
        pass
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
        pass
    
    def paintEvent(self, event):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.Image, self.Image.rect())
        pass
    
    def DrawImage(self, image):
        self.Image = ImageQt(image)
        self.update()
        pass

    def Clear(self):
        self.Image.fill(Qt.white)
        self.update()
        pass
