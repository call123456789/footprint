# 原始导入部分保持不变
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QIODevice 
from provincebutton import ProvinceButton

class ChinaWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1200, 686)
        self.provinces = []
        with open("resources/province.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        list = content.split()

        for item in list:
            button = ProvinceButton(self, item)
            self.provinces.append(button)
            button.show()