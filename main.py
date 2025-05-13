import sys
from PyQt5.QtWidgets import QApplication
from chinawidget import ChinaWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chinawidget = ChinaWidget()
    chinawidget.show()
    sys.exit(app.exec_())