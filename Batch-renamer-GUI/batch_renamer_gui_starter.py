import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from batch_renamer_ui import Ui_MainWindow 
import batch_renamer_lib

class BatchRenamerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.browseBtn.clicked.connect(self.get_filepath)
        self.batch_renamer = batch_renamer_lib.BatchRenamer()
        self.showNormal()

    def get_filepath(self):
        self.filepath = QFileDialog().getExistingDirectory()
        self.set_filepath()

    def set_filepath(self):
        self.filepathEdit.setText(self.filepath)
        self.update_list()

    def update_list(self):
        self.listWidget.clear()
        for root, dirs, files in os.walk(self.filepath):
            self.listWidget.addItems(files)

    def run_renamer(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BatchRenamerWindow()
    sys.exit(app.exec())