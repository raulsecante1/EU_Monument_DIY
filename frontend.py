from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QScrollArea, QVBoxLayout, QApplication, QDialog, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from PIL import Image  #to convert .dds to format that QT supports
from PIL.ImageQt import ImageQt

import sys

import json

import os

path = r"./great_projects_pic/"


class MonumentItem(QWidget):  # each monument
    
    clicked = Signal(object)

    def __init__(self, name, image_path):
        super().__init__()
        self.setMouseTracking(True)

        self.name_text = name

        self.image = QLabel()
        self.image.setFixedSize(300, 150)  # official size
        self.image.setAlignment(Qt.AlignCenter)

        img = Image.open(image_path)
        qt_img = ImageQt(img)
        pixmap = QPixmap.fromImage(qt_img)
        self.image.setPixmap(pixmap)
        self.image.setMouseTracking(True)

        self.name = QLabel(name)
        self.name.setMouseTracking(True)    

        layout = QHBoxLayout(self)
        layout.addWidget(self.image)
        layout.addWidget(self.name)
        layout.addStretch()

    def mouseMoveEvent(self, event):
        '''
        only change hand cursor on the image
        
        :param self: Description
        :param event: Description
        '''
        pos = event.position().toPoint()
        if self.image.geometry().contains(pos):
            self.setCursor(Qt.PointingHandCursor)
        else:
            self.setCursor(Qt.ArrowCursor) 
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            if self.image.geometry().contains(pos):
                self.clicked.emit(self)
        super().mousePressEvent(event)


class MonumentList(QWidget):
    def __init__(self):
        super().__init__()

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)
        self.layout.setAlignment(Qt.AlignTop)

        self.scroll.setWidget(self.container)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll)

    def add_monument(self, name, image_path):
        item = MonumentItem(name, image_path)
        item.clicked.connect(self.open_edit_window)
        self.layout.addWidget(item)

    def open_edit_window(self, item):
        dlg = MonumentEditWindow(item.name_text)
        dlg.exec()


class MonumentEditWindow(QDialog):
    def __init__(self, monument_name):
        super().__init__()
        self.setWindowTitle(f"Edit {monument_name}")
        self.resize(300, 200)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Modify data for {monument_name}"))

        # Example: add buttons / fields
        layout.addWidget(QPushButton("Save"))
        layout.addWidget(QPushButton("Cancel"))


def main():
    app = QApplication(sys.argv)

    monuments = MonumentList()
    
    lang = "CN"

    with open('monuments.json', 'r', encoding='utf-8') as fl:
        datas = json.load(fl)
        for data in datas:
            monuments.add_monument(data[lang], os.path.join(path, data["relative_path"]))
        monuments.resize(300, 150)
        monuments.show()

    sys.exit(app.exec())

main()