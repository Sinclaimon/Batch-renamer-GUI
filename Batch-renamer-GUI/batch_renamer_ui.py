# Form implementation generated from reading ui file 'batch_renamer.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 554)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ModeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ModeLabel.setObjectName("ModeLabel")
        self.horizontalLayout_2.addWidget(self.ModeLabel)
        self.RenameRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.RenameRadioButton.setEnabled(True)
        self.RenameRadioButton.setObjectName("RenameRadioButton")
        self.horizontalLayout_2.addWidget(self.RenameRadioButton, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.CopyRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.CopyRadioButton.setObjectName("CopyRadioButton")
        self.horizontalLayout_2.addWidget(self.CopyRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.FiletypesLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.FiletypesLabel.setObjectName("FiletypesLabel")
        self.horizontalLayout_2.addWidget(self.FiletypesLabel)
        self.FiletypesEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.FiletypesEdit.setObjectName("FiletypesEdit")
        self.horizontalLayout_2.addWidget(self.FiletypesEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.PrefixLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.PrefixLabel.setObjectName("PrefixLabel")
        self.horizontalLayout_2.addWidget(self.PrefixLabel)
        self.PrefixEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.PrefixEdit.setObjectName("PrefixEdit")
        self.horizontalLayout_2.addWidget(self.PrefixEdit)
        self.SufixLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SufixLabel.setObjectName("SufixLabel")
        self.horizontalLayout_2.addWidget(self.SufixLabel)
        self.SufixEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SufixEdit.setObjectName("SufixEdit")
        self.horizontalLayout_2.addWidget(self.SufixEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StringsToFindLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.StringsToFindLabel.setObjectName("StringsToFindLabel")
        self.horizontalLayout_3.addWidget(self.StringsToFindLabel)
        self.StringsToFindEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.StringsToFindEdit.setObjectName("StringsToFindEdit")
        self.horizontalLayout_3.addWidget(self.StringsToFindEdit)
        self.StringsToReplaceLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.StringsToReplaceLabel.setObjectName("StringsToReplaceLabel")
        self.horizontalLayout_3.addWidget(self.StringsToReplaceLabel)
        self.StringsToReplaceEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.StringsToReplaceEdit.setObjectName("StringsToReplaceEdit")
        self.horizontalLayout_3.addWidget(self.StringsToReplaceEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.FilesList = QtWidgets.QListView(parent=self.centralwidget)
        self.FilesList.setObjectName("FilesList")
        self.gridLayout.addWidget(self.FilesList, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FilePathLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.FilePathLabel.setObjectName("FilePathLabel")
        self.horizontalLayout.addWidget(self.FilePathLabel)
        self.FilePathEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.FilePathEdit.setObjectName("FilePathEdit")
        self.horizontalLayout.addWidget(self.FilePathEdit)
        self.BrowseButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BrowseButton.setObjectName("BrowseButton")
        self.horizontalLayout.addWidget(self.BrowseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.RunButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RunButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.RunButton.setObjectName("RunButton")
        self.gridLayout.addWidget(self.RunButton, 4, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ModeLabel.setText(_translate("MainWindow", "Mode"))
        self.RenameRadioButton.setText(_translate("MainWindow", "Rename"))
        self.CopyRadioButton.setText(_translate("MainWindow", "Copy"))
        self.FiletypesLabel.setText(_translate("MainWindow", "Filetypes"))
        self.PrefixLabel.setText(_translate("MainWindow", "Prefix"))
        self.SufixLabel.setText(_translate("MainWindow", "Sufix"))
        self.StringsToFindLabel.setText(_translate("MainWindow", "Strings to find"))
        self.StringsToReplaceLabel.setText(_translate("MainWindow", "Strings to Replace"))
        self.FilePathLabel.setText(_translate("MainWindow", "File Path"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.RunButton.setText(_translate("MainWindow", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
