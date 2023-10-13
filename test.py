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

# UI Definition
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 4)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName("pushButton_22")
        # ... (include code for defining UI elements)

# Omit the button click handling code for now.

# Button Click Handling
        self.mw  = MainWindow
        self.text=''
        self.textEdit.setFontPointSize(24)
        self.processed=False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_12.clicked.connect(self.show) 
        self.pushButton.clicked.connect(self.show) 
        self.pushButton_3.clicked.connect(self.show)
        # ... (include code that connects button click events and defines functions)

# Button Actions
    def process(self):
        try:
            inp=self.text
            inp = re.sub(r"\.(?![0-9])","", inp)
            val = eval(inp, {'_builtins_':None})
            self.text=str(val)
        except Exception as e:
            self.text = str(e)
        self.processed = True

    def show(self):
        self.textEdit.setFontPointSize(24)
        self.text = self.textEdit.toPlainText()
        num_list = [str(num) for num in [0,1,2,3,4,5,6,7,8,9,'.']]
        op_list = ['+','-','*','/','%']
        c_or_ce_list = ['AC']
        func_list=['1/x','x^2','sqrt','+/-','x^3']
        if self.mw.sender().text()!='Backspace':
            if self.mw.sender().text() in num_list :
                if self.processed == True:
                    self.text=''
                self.text+=self.mw.sender().text()
                self.processed = False
            if self.mw.sender().text() in op_list :
                self.text+=self.mw.sender().text()
                self.processed = False
            if self.mw.sender().text() =='=':
                self.process()
            if self.mw.sender().text() in c_or_ce_list:
                self.text=''
                self.processed = False
            if self.mw.sender().text() in func_list:
                if self.mw.sender().text() == func_list[0]:
                    try:
                        self.text= str(1/eval(self.text))
                    except Exception as e: 
                        self.text=str(e)
                    self.processed = False
                if self.mw.sender().text() == func_list[1]:
                    self.text= str(eval(self.text)**2)
                    self.processed = False
                if self.mw.sender().text() == func_list[2]:
                    self.text= str(eval(self.text)**0.5)
                    self.processed = False
                if self.mw.sender().text() == func_list[3]:
                    self.text= str(-1*eval(self.text))	
                    self.processed = False
                if self.mw.sender().text() == func_list[4]:
                    self.text= str(eval(self.text)**3)
                    self.processed = False
        else:
            self.text = self.text[0:len(self.text)-1]
        self.textEdit.setText(self.text)

# Finishing Touches
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pyshine.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionitem1 = QtWidgets.QAction(MainWindow)
        self.actionitem1.setObjectName("actionitem1")
        self.actionitem2 = QtWidgets.QAction(MainWindow)
        self.actionitem2.setObjectName("actionitem2")
        self.actionaa = QtWidgets.QAction(MainWindow)
        self.actionaa.setObjectName("actionaa")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
