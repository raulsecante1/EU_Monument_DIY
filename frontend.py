from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QScrollArea, QVBoxLayout, QApplication, QComboBox, QLineEdit, QGroupBox, QPushButton, QMessageBox, QInputDialog, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from PIL import Image  #to convert .dds to format that QT supports
from PIL.ImageQt import ImageQt

import backend

import sys

import json

import os

path = r"./great_projects_pic/"

with open("attrs.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    LOCALIZATION = {item["code"]: item for item in data}

with open("buffs.json", "r", encoding="utf-8") as f:
    MODIFIER_NAMES = {item["code"]: item for item in json.load(f)}


def get_localization(code, lang):
    if code not in LOCALIZATION:
        return code  # show code if missing
    return LOCALIZATION[code].get(lang, code)


def localize_modifier(code, lang):
    if code not in MODIFIER_NAMES:
        return code  # show code if missing
    return MODIFIER_NAMES[code].get(lang, code)


class MonumentItem(QWidget):  # each monument
    
    clicked = Signal(object)

    def __init__(self, names:dict, image_path, monument_data:backend.Monument, lang):
        super().__init__()
        self.setMouseTracking(True)

        self.name_dict = names

        self.image = QLabel()
        self.image.setFixedSize(300, 150)  # official size
        self.image.setAlignment(Qt.AlignCenter)

        img = Image.open(image_path)
        qt_img = ImageQt(img)
        pixmap = QPixmap.fromImage(qt_img)
        self.image.setPixmap(pixmap)
        self.image.setMouseTracking(True)

        self.name = QLabel()
        self.name.setMouseTracking(True)
        self.set_language(lang)

        self.monument_data = monument_data

        self.lang = lang

        layout = QHBoxLayout(self)
        layout.addWidget(self.image)
        layout.addWidget(self.name)
        layout.addStretch()

    def mouseMoveEvent(self, event):
        '''
        only change to hand cursor on the image
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

    def set_language(self, lang):
        self.lang = lang
        self.name.setText(self.name_dict.get(lang, ""))


class MonumentList(QWidget):
    def __init__(self, path):
        super().__init__()

        self.file_path = path

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()
        self.layout = QVBoxLayout(self.container)
        self.layout.setAlignment(Qt.AlignTop)

        self.scroll.setWidget(self.container)

        main_layout = QVBoxLayout(self)

        header = QWidget()
        header_layout = QHBoxLayout(header)

        header_layout.addWidget(QLabel("Language / 语言"))

        self.current_lang = "CN"
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["CN", "EN", "ES"])
        self.lang_combo.setCurrentText(self.current_lang)
        self.lang_combo.currentTextChanged.connect(self.on_language_changed)
        header_layout.addWidget(self.lang_combo)

        header_layout.addSpacing(20)

        # --- NEW BUTTONS ---
        self.btn_set_start = QPushButton(self.helper_loc("btn_set_start"))
        self.btn_toggle_no_limit = QPushButton(self.helper_loc("btn_toggle_no_limit"))
        self.btn_toggle_can_be_moved = QPushButton(self.helper_loc("btn_toggle_can_be_moved"))
        self.btn_build_all = QPushButton(self.helper_loc("btn_build_all"))

        header_layout.addWidget(self.btn_set_start)
        header_layout.addWidget(self.btn_toggle_no_limit)
        header_layout.addWidget(self.btn_toggle_can_be_moved)
        header_layout.addWidget(self.btn_build_all)

        header_layout.addStretch()
        main_layout.addWidget(header)

        main_layout.addWidget(self.scroll)

        # Button logic
        self.btn_set_start.clicked.connect(self.set_all_start)
        self.btn_toggle_no_limit.clicked.connect(self.toggle_no_limit)
        self.btn_toggle_can_be_moved.clicked.connect(self.toggle_can_be_moved)
        self.btn_build_all.clicked.connect(self.build_all_monuments)

        self.edit_windows = []


    def add_monument(self, names, image_path, monument):
        item = MonumentItem(names, image_path, monument, self.current_lang)
        item.clicked.connect(self.open_edit_window)
        self.layout.addWidget(item)

    def open_edit_window(self, item):
        dlg = MonumentEditWindow(item)
        dlg.show()
        self.edit_windows.append(dlg)

    def on_language_changed(self, lang):
        self.current_lang = lang
        self.update_button_texts()
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i).widget()
            if isinstance(item, MonumentItem):
                item.set_language(lang)
    
    def update_button_texts(self):
        self.btn_set_start.setText(self.helper_loc("btn_set_start"))
        self.btn_toggle_no_limit.setText(self.helper_loc("btn_toggle_no_limit"))
        self.btn_toggle_can_be_moved.setText(self.helper_loc("btn_toggle_can_be_moved"))
        self.btn_build_all.setText(self.helper_loc("btn_build_all"))


    def all_items(self):
        for i in range(self.layout.count()):
            w = self.layout.itemAt(i).widget()
            if isinstance(w, MonumentItem):
                yield w

    def set_all_start(self):
        value, ok = QInputDialog.getText(
            self,
            self.helper_loc("btn_set_start"),
            self.helper_loc("info_set_start")
        )
        if not ok or value == "":
            return

        for item in self.all_items():
            item.monument_data.start = value

        QMessageBox.information(self,
                                self.helper_loc("btn_set_start"),
                                self.helper_loc("info_finished_set_start"))

    def toggle_no_limit(self):
        items = list(self.all_items())
        if not items:
            return

        current = items[0].monument_data.no_limit_tag
        new_value = not current

        for item in items:
            item.monument_data.no_limit_tag = new_value

        QMessageBox.information(
            self,
            self.helper_loc("btn_toggle_no_limit"),
            f"{self.helper_loc("info_toggle_no_limit")}{new_value}"
        )

    def toggle_can_be_moved(self):
        items = list(self.all_items())
        if not items:
            return

        current = items[0].monument_data.can_be_moved
        new_value = "no" if current == "yes" else "yes"

        for item in items:
            item.monument_data.can_be_moved = new_value

        QMessageBox.information(
            self,
            self.helper_loc("btn_toggle_can_be_moved"),
            f"can_be_moved → {new_value}"
        )

    def build_all_monuments(self):
        monuments_dict = {i: item.monument_data for i, item in enumerate(self.all_items())}

        try:
            backend.output(monuments_dict, self.file_path)
            QMessageBox.information(
                self,
                self.helper_loc("btn_build_all"),
                self.helper_loc("info_build_all")
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to write file:\n{str(e)}")

    def helper_loc(self, code):
        return get_localization(code, self.current_lang)



class MonumentEditWindow(QWidget):
    def __init__(self, monument:MonumentItem):
        super().__init__()

        self.monument = monument
        TITLE_MAP = {"CN": "编辑奇观",
                     "ES": "Editar Monumento",
                     "EN": "Edit Monument"
                     }

        self.setWindowTitle(TITLE_MAP.get(self.monument.lang, "Edit Monument"))
        self.resize(1200, 800)

        # Main layout
        self.main_layout = QVBoxLayout(self)

        # # Header
        # self.header = QWidget()
        # header_layout = QHBoxLayout(self.header)
        # save_btn = QPushButton("Save")
        # header_layout.addWidget(save_btn)
        # header_layout.addStretch()
        # self.main_layout.addWidget(self.header)

        # Scroll area + container
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.container)
        self.main_layout.addWidget(self.scroll)

        # Image
        self.image_label = QLabel()
        self.image_label.setPixmap(monument.image.pixmap())
        self.image_label.setAlignment(Qt.AlignCenter)
        self.container_layout.addWidget(self.image_label)

        # Editable fields
        self.info_ui()

    def info_ui(self):
        for attr in ["start", "date", "time", "build_cost", "can_be_moved", "move_days_per_unit_distance", 
                     "starting_tier", "type"]:
            self.container_layout.addWidget(QLabel(self.helper_loc(attr)))

            line = QLineEdit()
            line.setText(str(getattr(self.monument.monument_data, attr)))
            line.textChanged.connect(lambda v, a=attr: setattr(self.monument.monument_data, a, v))

            self.container_layout.addWidget(line)
        
        for tier in range(4):
            self.add_tier_block(tier)

    def add_tier_block(self, tier_number):
        tier_box = QGroupBox(
            f"{self.helper_loc('tier')} {tier_number}"
        )
        tier_layout = QVBoxLayout(tier_box)
        tier_layout.setContentsMargins(10, 5, 5, 5)

        # Map attributes for this tier
        data = self.monument.monument_data
        tier_fields = {
            "upgrade_time": getattr(data, f"tier_{tier_number}_upgrade_time"),
            "cost_to_upgrade": getattr(data, f"tier_{tier_number}_cost_to_upgrade"),
            "province_modifiers": getattr(data, f"tier_{tier_number}_province_modifiers"),
            "area_modifier": getattr(data, f"tier_{tier_number}_area_modifier"),
            "region_modifier": getattr(data, f"tier_{tier_number}_region_modifier"),
            "country_modifiers": getattr(data, f"tier_{tier_number}_country_modifiers")
        }

        for key in ["upgrade_time", "cost_to_upgrade"]:  # Editable simple fields
            tier_layout.addWidget(QLabel(self.helper_loc(key)))
            line = QLineEdit(str(tier_fields[key]))
            line.textChanged.connect(lambda v, attr=key: setattr(data, f"tier_{tier_number}_{attr}", v))
            tier_layout.addWidget(line)

        for key in ["province_modifiers", "area_modifier", "region_modifier", "country_modifiers"]:  # Editable modifier lists
            self.add_modifier_list(tier_layout, key, tier_fields[key])

        self.container_layout.addWidget(tier_box)

    def add_modifier_list(self, parent_layout, title, modifier_list):

        initializing = True

        group = QGroupBox(self.helper_loc(title))
        layout = QVBoxLayout(group)
        layout.setContentsMargins(15, 5, 5, 5)

        rows = []  # UI rows

        def sync_backend():
            if initializing:
                return
            modifier_list.clear()
            for row in rows:
                modifier_list.append((row["name"], row["value"]))

        def add_row(name="", value=""):
            row_data = {"name": name, "value": value}
            rows.append(row_data)

            row = QWidget()
            row_layout = QHBoxLayout(row)
            row_layout.setContentsMargins(0, 0, 0, 0)

            # --- Modifier name combo ---
            name_combo = QComboBox()
            for code in MODIFIER_NAMES:
                name_combo.addItem(
                    localize_modifier(code, self.monument.lang),
                    code
                )

            idx = name_combo.findData(name)
            if idx >= 0:
                name_combo.setCurrentIndex(idx)

            def on_name_changed(i):
                row_data["name"] = name_combo.itemData(i)
                sync_backend()

            name_combo.currentIndexChanged.connect(on_name_changed)

            # --- Value ---
            value_edit = QLineEdit(str(value))

            def on_value_changed(v):
                row_data["value"] = v
                sync_backend()

            value_edit.textChanged.connect(on_value_changed)

            # --- Delete button ---
            del_btn = QPushButton("❌")
            del_btn.setFixedWidth(30)

            def delete_row():
                rows.remove(row_data)
                row.setParent(None)
                row.deleteLater()
                sync_backend()

            del_btn.clicked.connect(delete_row)

            # --- Layout ---
            row_layout.addWidget(QLabel(self.helper_loc("modifier_name")))
            row_layout.addWidget(name_combo)
            row_layout.addWidget(QLabel(self.helper_loc("modifier_value")))
            row_layout.addWidget(value_edit)
            row_layout.addWidget(del_btn)

            layout.insertWidget(layout.count() - 1, row)

            initializing = False

            sync_backend()

        # Existing modifiers
        for name, value in list(modifier_list):
            add_row(name, value)

        # Add button
        add_btn = QPushButton(self.helper_loc("add_modifier"))
        add_btn.clicked.connect(lambda: add_row("", ""))
        layout.addWidget(add_btn)

        parent_layout.addWidget(group)


    def helper_loc(self, code):
        return get_localization(code, self.monument.lang)


def main():
    app = QApplication(sys.argv)

        # --- NEW: Ask user to select JSON file ---
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Select Monument JSON File",
        "",          # initial directory
        "TXT Files (*.txt)"
    )

    if not file_path:  # user canceled
        print("No file selected. Exiting.")
        sys.exit(0)

    monuments = MonumentList(file_path)
    monuments_info = backend.read_monuments(file_path)

    with open('monuments.json', 'r', encoding='utf-8') as fl:
        datas = json.load(fl)
        for data in datas:
            monument_key = data["relative_path"].split("_", 2)[2].split(".")[0]
            monuments.add_monument(
                names={
                    "CN": data["CN"],
                    "EN": data.get("EN", ""),
                    "ES": data.get("ES", "")
                },
                image_path=os.path.join(path, data["relative_path"]),
                monument=monuments_info[monument_key]
            )
        monuments.resize(300, 150)
        monuments.show()

    sys.exit(app.exec())

main()