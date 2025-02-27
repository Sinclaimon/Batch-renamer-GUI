import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
# You'll need to make this ui in QtDesigner
# And convert it to a .py file using the MakeUIPy.bat file
from batch_renamer_ui import Ui_MainWindow 
# Recommend you rename this
import batch_renamer_lib

class BatchRenamerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # UI Setup
        super().__init__()
        super(Ui_MainWindow).__init__()
        self.setupUi(self)
        # Instance the "back end"
        self.batch_renamer = batch_renamer_lib.BatchRenamer()
        # Use the logger from the batch_renamer
        self.logger = self.batch_renamer.logger
        # Connect the browse button to get_filepath function
        self.BrowseButton.clicked.connect(self.get_filepath)
        # Connect the Run button to the run_renamer function
        self.RunButton.clicked.connect(self.run_renamer)
        
        # Show UI normal vs maximized
        self.showNormal()

        # Set the "Rename" button checked by default
        self.RenameRadioButton.setChecked(True)

        # Add tooltips
        self.add_tooltips()

    def add_tooltips(self):
        """
        Add tooltips to UI elements
        """
        self.FilePathEdit.setToolTip("Enter the file path or browse to select a folder")
        self.BrowseButton.setToolTip("Browse to select a folder")
        self.FiletypesEdit.setToolTip("Enter the file types to include (e.g., .txt, .png)")
        self.PrefixEdit.setToolTip("Enter the prefix to add to file names")
        self.SufixEdit.setToolTip("Enter the suffix to add to file names")
        self.StringsToFindEdit.setToolTip("Enter the strings to find, separated by commas")
        self.StringsToReplaceEdit.setToolTip("Enter the string to replace the found strings")
        self.CopyRadioButton.setToolTip("Check to copy files instead of moving them")
        self.RunButton.setToolTip("Run the batch renamer")

    def get_filepath(self):
        """
        Open a file dialog for browsing to a folder
        """
        try:
            self.logger.info("Browse button clicked")
            self.filepath = QFileDialog().getExistingDirectory()
            self.logger.info(f"Selected filepath: {self.filepath}")
            self.set_filepath()
        except Exception as e:
            self.logger.error(f"Error in get_filepath: {e}")

    def set_filepath(self):
        """
        Set lineEdit text for filepath
        """
        try:
            self.logger.info("Setting filepath in FilePathEdit")
            self.FilePathEdit.setText(self.filepath)
            self.update_list()
        except Exception as e:
            self.logger.error(f"Error in set_filepath: {e}")

    def update_list(self):
        """
        Clear listwidget
        read files in filepath with os.walk
        Add files as new items
        """
        self.logger.info("Updating file list")
        try:
            self.FilesList.clear()
            for root, dirs, files in os.walk(self.filepath):
                self.FilesList.addItems(files)
        except Exception as e:
            self.logger.error(f"Error in update_list: {e}")

    def run_renamer(self):
        """
        Run back end batch renamer using self.batch_renamer
        self.batch_renamer is an instance of the BatchRenamer class
        """
        try:
            filepath = self.FilePathEdit.text()
            if isinstance(filepath, tuple):
                filepath = filepath[0]
            copy_files = self.CopyRadioButton.isChecked()
            filetypes = self.FiletypesEdit.text()
            strings_to_find = self.StringsToFindEdit.text().split(',')
            string_to_replace = self.StringsToReplaceEdit.text()
            prefix = self.PrefixEdit.text()
            suffix = self.SufixEdit.text()

            self.logger.info("Running batch renamer with the following parameters:")
            self.logger.info(f"Filepath: {filepath}")
            self.logger.info(f"Copy files: {copy_files}")
            self.logger.info(f"Filetypes: {filetypes}")
            self.logger.info(f"Strings to find: {strings_to_find}")
            self.logger.info(f"String to replace: {string_to_replace}")
            self.logger.info(f"Prefix: {prefix}")
            self.logger.info(f"Suffix: {suffix}")

            self.batch_renamer.filepath = filepath
            self.batch_renamer.copy_files = copy_files
            self.batch_renamer.filetypes = filetypes
            self.batch_renamer.strings_to_find = strings_to_find
            self.batch_renamer.string_to_replace = string_to_replace
            self.batch_renamer.prefix = prefix
            self.batch_renamer.suffix = suffix

            self.batch_renamer.rename_files_in_folder(filepath, filetypes, strings_to_find, string_to_replace, prefix, suffix, copy_files)

            # Update the file list after renaming
            self.update_list()
        except Exception as e:
            self.logger.error(f"Error in run_renamer: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BatchRenamerWindow()
    sys.exit(app.exec())
