import traceback

from PyQt6.QtWidgets import QApplication, QMainWindow

from Fraction.ui.MainWindowExt import MainWindowExt
try:
    app = QApplication([])
    myWindow = MainWindowExt()
    MainWindow = QMainWindow()
    myWindow.setupUi(MainWindow)
    myWindow.show()
    app.exec()
except:
    traceback.print_exc()