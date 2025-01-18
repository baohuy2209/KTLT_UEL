from PyQt6.QtWidgets import QApplication, QMainWindow

from ShopGroceries.ui.home.MainWindowExt import MainWindowExt


def HomePage():
    app = QApplication([])
    myWindow = MainWindowExt()
    MainWindow = QMainWindow()
    myWindow.setupUi(MainWindow)
    myWindow.show()
    app.exec()