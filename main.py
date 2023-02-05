import sys
import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from bism_app import Ui_ReportSplitter

from PyQt5.uic import loadUi



class Window(QMainWindow, Ui_ReportSplitter):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    print("1")
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
"""from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5 import QtCore
import sys
from PyQt5.QtWidgets import *


def dialog():
    file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                              "", "PDF Files(*.pdf);;All Files (*);;Text Files (*.txt)")
    if check:
        print(file)

def getDirectory():
    dirlist, check = QFileDialog.getExistingDirectory(None,"Выбрать папку",".")

    if check:
        print(dirlist)




app = QApplication(sys.argv)
app.setStyle('Fusion')
win = QMainWindow()
win.setGeometry(700, 700, 600, 600)
win.setWindowTitle("File Splitter")

button = QPushButton(win)
button.setText("Choose file")
button.clicked.connect(dialog)
button.resize(120, 120)
button.move(250, 300)

button2 = QPushButton(win)
button2.setText("Choose directory")
button2.clicked.connect(getDirectory())
button2.resize(120, 120)
button2.move(120, 120)

win.show()
sys.exit(app.exec_())
""""""
app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)

engine.load('./UI/main.qml')

sys.exit(app.exec())
"""


