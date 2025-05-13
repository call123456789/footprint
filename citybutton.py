from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QBitmap, QIcon
from PyQt5.QtCore import Qt
from spotwidget import SpotWidget

class CityButton(QPushButton):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name
        self.parent = parent
        imagename = f"resources/{name}.png"
        originalPixmap = QPixmap(imagename)
        # 获取原始图片的宽高
        originalWidth = originalPixmap.width()
        originalHeight = originalPixmap.height()
        # 计算目标高度（保持宽高比）
        if originalWidth*0.7 > originalHeight:
            targetWidth = 1000
            targetHeight = int(originalHeight * targetWidth / originalWidth)
        else:
            targetHeight = 600
            targetWidth = int(originalWidth * targetHeight / originalHeight)
        pixmap = originalPixmap.scaled(targetWidth, targetHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.setFixedSize(pixmap.size())
        mask = pixmap.createMaskFromColor(Qt.transparent, Qt.MaskInColor)
        self.setMask(mask)
        self.setIcon(QIcon(pixmap))
        self.setIconSize(pixmap.size())
        self.setStyleSheet("QPushButton{border:none; background:transparent;}")
        self.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        print(self.name)
        self.parent.hide()
        self.son = SpotWidget(pre = self.parent)
        self.son.show()