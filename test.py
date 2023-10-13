# Initial Setup
from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pyshine.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.mw  = MainWindow

if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
