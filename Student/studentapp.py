from PyQt6.QtWidgets import QApplication, QMainWindow

from Student.ui.MainWindowExt import MainWindowExt

app = QApplication([])
MainWindow = QMainWindow()
myWindow = MainWindowExt()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()