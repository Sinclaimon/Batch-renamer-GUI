@echo off
REM This batch file converts the UI file created in Qt Designer into a Python file.

pyuic6 -x batch_renamer_ui.ui -o batch_renamer_ui.py

echo Conversion complete. The UI file has been successfully converted to Python.