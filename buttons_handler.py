from PyQt5.QtWidgets import *

def getFileName(self):
    filename, filetype = QFileDialog.getOpenFileName(None,
                                                     "Choose File",
                                                     ".",
                                                     "PDF Files(*.pdf)")
    self.listWidget.addItem("Filename !" + filename)


def getDirectory(self):  # <-----
    directory = QFileDialog.getExistingDirectory(None, "Choose Folder", ".")

    if directory:
        self.listWidget.addItem("Output folder - " + directory)