from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QBitmap, QIcon
from PyQt5.QtCore import Qt
from provincewidget import ProvinceWidget

class ProvinceButton(QPushButton):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name
        self.parent = parent
        self.son = None
        imagename = f"resources/{name}.png"
        originalPixmap = QPixmap(imagename)
        targetSize = (1000, 686)
        pixmap = originalPixmap.scaled(targetSize[0], targetSize[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setFixedSize(pixmap.size())
        mask = pixmap.createMaskFromColor(Qt.transparent, Qt.MaskInColor)
        self.setMask(mask)
        self.setIcon(QIcon(pixmap))
        self.setIconSize(pixmap.size())
        self.setStyleSheet("QPushButton{border:none; background:transparent;}")
        self.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        print(self.name)
        self.son = ProvinceWidget(None, self.name, self.parent)
        self.son.show()
        self.parent.hide()