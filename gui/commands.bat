@echo off
pyuic5 -x ui\MainWindow.ui -o .\src\ui\mainwindow.py
pyrcc5 assets\icon.qrc -o icon_rc.py
python main.py