from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QScrollArea, QVBoxLayout, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from PIL import Image  #to convert .dds to format that QT supports
from PIL.ImageQt import ImageQt

import sys

import json

import os

path = r"./great_projects/"

class MonumentItem(QWidget):
    def __init__(self, name, image_path):
        super().__init__()

        self.image = QLabel()
        self.image.setFixedSize(300, 150)  #  official size
        self.image.setAlignment(Qt.AlignCenter)

        img = Image.open(image_path)
        qt_img = ImageQt(img)
        pixmap = QPixmap.fromImage(qt_img)
        self.image.setPixmap(pixmap)

        self.name = QLabel(name)

        layout = QHBoxLayout(self)
        layout.addWidget(self.image)
        layout.addWidget(self.name)
        layout.addStretch()


class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
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
        self.layout.addWidget(item)


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