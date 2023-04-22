from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from splitter_logic import *

class Ui_ReportSplitter(object):
    filename = ""
    directory = ""
    file_type = ""

    def set_report_type(self):
        self.file_type = "mok"
        self.listWidget.addItem("file type - " + self.file_type)

    def set_mok_type(self):
        self.file_type = "report"
        self.listWidget.addItem("file type - " + self.file_type)

    def getFileName(self):
        self.filename, check = QFileDialog.getOpenFileName(None,
                                                         "Choose File",
                                                         ".",
                                                         "PDF Files(*.pdf)")
        if check:
            self.listWidget.addItem("Filename - " + self.filename)

        if self.directory == "":
            self.listWidget.addItem("Please select the output folder")


    def getDirectory(self):  # <-----
        self.directory = QFileDialog.getExistingDirectory(None, "Choose Folder", ".")

        if self.directory:
            self.listWidget.addItem("Output folder - " + self.directory)

    def split(self):  # <-----
        if self.filename == "":
            self.listWidget.addItem("Please select the main report file")
            return

        if self.directory == "":
            self.listWidget.addItem("Please select the output folder")
            return

        if self.file_type == "":
            self.listWidget.addItem("Please set the file type")
            return
        print(self.file_type)
        separate_all(self.filename, self.directory, self.listWidget, self.file_type)

    def setupUi(self, ReportSplitter):
        ReportSplitter.setObjectName("ReportSplitter")
        ReportSplitter.setWindowModality(QtCore.Qt.WindowModal)
        ReportSplitter.resize(797, 600)
        ReportSplitter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        ReportSplitter.setAutoFillBackground(False)
        ReportSplitter.setStyleSheet("font: 8pt \"Noto Sans Lisu\";")
        ReportSplitter.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(ReportSplitter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 220, 211, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.FileButton.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.FileButton.setObjectName("FileButton")
        self.verticalLayout.addWidget(self.FileButton)
        self.FolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.FolderButton.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.FolderButton.setObjectName("FolderButton")
        self.verticalLayout.addWidget(self.FolderButton)
        self.SplitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SplitButton.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.SplitButton.setObjectName("SplitButton")
        self.verticalLayout.addWidget(self.SplitButton)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(180, 0, 81, 681))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\FirstApplicationTest\\UI\\images/bism3.bmp"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(235, 11, 541, 551))
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 500, 211, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sample_1_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sample_1_button.setObjectName("sample_1_button")
        self.horizontalLayout.addWidget(self.sample_1_button)
        self.sample_2_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sample_2_button.setObjectName("sample_2_button")
        self.horizontalLayout.addWidget(self.sample_2_button)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 470, 221, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        ReportSplitter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReportSplitter)
        self.statusbar.setObjectName("statusbar")
        ReportSplitter.setStatusBar(self.statusbar)
        self.FolderButton_2 = QtWidgets.QAction(ReportSplitter)
        self.FolderButton_2.setCheckable(False)
        self.FolderButton_2.setObjectName("FolderButton_2")

        self.FileButton.clicked.connect(self.getFileName)
        self.FolderButton.clicked.connect(self.getDirectory)
        self.SplitButton.clicked.connect(self.split)

        self.sample_1_button.clicked.connect(self.set_report_type)
        self.sample_2_button.clicked.connect(self.set_mok_type)

        self.retranslateUi(ReportSplitter)
        QtCore.QMetaObject.connectSlotsByName(ReportSplitter)

    def retranslateUi(self, ReportSplitter):
        _translate = QtCore.QCoreApplication.translate
        ReportSplitter.setWindowTitle(_translate("ReportSplitter", "Report Splitter"))
        self.FileButton.setText(_translate("ReportSplitter", "Choose File"))
        self.FolderButton.setText(_translate("ReportSplitter", "Choose Output Folder"))
        self.SplitButton.setText(_translate("ReportSplitter", "Split"))
        self.label.setToolTip(_translate("ReportSplitter", "<html><head/><body><p><img src=\":/newPrefix/bism.png\"/></p></body></html>"))
        self.listWidget.setAccessibleDescription(_translate("ReportSplitter", "logs"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("ReportSplitter", "Program started\nPlease select the main file report(Press button: 'Choose File')"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.sample_1_button.setText(_translate("ReportSplitter", "moks sample"))
        self.sample_2_button.setText(_translate("ReportSplitter", "reports sample"))
        self.FolderButton_2.setText(_translate("ReportSplitter", "Choose Folder"))


