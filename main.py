import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from bism_app import Ui_ReportSplitter


class Window(QMainWindow, Ui_ReportSplitter):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())